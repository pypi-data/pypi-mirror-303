#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import math
import threading
import time
from collections.abc import Callable, Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import cast

import av
from av import AudioFrame
from av import VideoFrame
from av.audio.stream import AudioStream
from av.container import OutputContainer
from av.packet import Packet
from av.video.stream import VideoStream

from kast.media.processing.Resolution import FULL_HD, Resolution
from kast.media.processing.common import CodecName, StreamId
from kast.utils.log.Loggable import Loggable
from kast.utils.pathUtils import fileExtension

AvStream = AudioStream | VideoStream
AvFrame = AudioFrame | VideoFrame


@dataclass(frozen=True)
class Streams:
    video: StreamId = 0
    audio: StreamId = 0


@dataclass(frozen=True)
class Codecs:
    video: CodecName
    audio: CodecName


@dataclass(frozen=True)
class TranscodeParams:
    inputFile: Path
    inputStreamIds: Streams
    outputCodecNames: Codecs
    maxResolution: Resolution = FULL_HD


ProgressCallback = Callable[[int, bool], None]


class Transcoder(Loggable):

    PROGRESS_UPDATE_DELAY = 1

    def __init__(
        self,
        params: TranscodeParams,
        outputFile: Path,
        progressCallback: ProgressCallback | None = None,
        cancelEvent: threading.Event | None = None
    ) -> None:
        self._params = params
        self._outputFile = outputFile
        self._progressCallback = progressCallback

        self._inputCodeNames = self._extractInputCodecs(
            inputFile=self._params.inputFile,
            inputStreams=self._params.inputStreamIds
        )

        self._inputResolution = self._extractInputResolution(
            inputFile=self._params.inputFile,
            videoStreamId=self._params.inputStreamIds.video
        )
        self._outputResolution = self._inputResolution.shrinkToFit(self._params.maxResolution)

        self._remuxContainer = (fileExtension(outputFile) not in self._getFormatExtensions(self._params.inputFile))
        self._transcodeAudio = (self._params.outputCodecNames.audio != self._inputCodeNames.audio)
        self._transcodeVideo = (self._params.outputCodecNames.video != self._inputCodeNames.video) or \
           (self._inputResolution > self._params.maxResolution)

        self._cancelEvent = cancelEvent if cancelEvent else threading.Event()
        self._complete = False
        self._lastPos = 0

    @property
    def requireProcessing(self) -> bool:
        return self._remuxContainer or self._transcodeAudio or self._transcodeVideo

    @property
    def inputFile(self) -> Path:
        return self._params.inputFile

    @property
    def outputFile(self) -> Path:
        return self._outputFile if self.requireProcessing else self._params.inputFile

    @property
    def complete(self) -> bool:
        return self._complete

    @property
    def lastPos(self) -> int:
        return self._lastPos

    @property
    def inputCodecNames(self) -> Codecs:
        return self._inputCodeNames

    @property
    def outputCodecNames(self) -> Codecs:
        return self._params.outputCodecNames

    @property
    def maxResolution(self) -> Resolution:
        return self._params.maxResolution

    @property
    def inputResolution(self) -> Resolution:
        return self._inputResolution

    @property
    def outputResolution(self) -> Resolution:
        return self._outputResolution

    @property
    def params(self) -> TranscodeParams:
        return self._params

    @property
    def cancelEvent(self) -> threading.Event:
        return self._cancelEvent

    def run(self) -> bool:
        if self._complete:
            return self._complete
        if not self.requireProcessing:
            self._complete = True
            self._notifyProgress(100)
            return self._complete

        with av.open(str(self._params.inputFile)) as fInput,\
                av.open(str(self._outputFile), 'w') as fOutput:

            inStreamVideo = fInput.streams.video[self._params.inputStreamIds.video]
            inStreamAudio = fInput.streams.audio[self._params.inputStreamIds.audio]

            self.log.info(f"Remuxing: {fileExtension(self.inputFile)} -> {fileExtension(self.outputFile)}")
            self.log.info(f"Transcoding: {self.inputCodecNames} -> {self.outputCodecNames}")
            self.log.info(f"Resizing: {self.inputResolution} -> {self.outputResolution}")

            def createOutputVideoStream() -> VideoStream:
                if not self._transcodeVideo:
                    return cast(VideoStream, fOutput.add_stream(template=inStreamVideo))

                vStream = cast(VideoStream, fOutput.add_stream(
                    self._params.outputCodecNames.video,
                    inStreamVideo.average_rate
                ))
                vStream.width = self.outputResolution.width
                vStream.height = self.outputResolution.height
                vStream.options = {'crf': '23'}  # type: ignore # TODO: Find out if its still needed!
                return vStream

            def createOutputAudioStream() -> AudioStream:
                if not self._transcodeAudio:
                    return cast(AudioStream, fOutput.add_stream(template=inStreamAudio))
                return cast(AudioStream, fOutput.add_stream(self._params.outputCodecNames.audio))

            outStreamVideo = createOutputVideoStream()
            outStreamAudio = createOutputAudioStream()

            last_update = 0.0
            for packet in fInput.demux([inStreamAudio, inStreamVideo]):
                if self._cancelEvent.is_set():
                    return False

                if packet is not None and packet.pos is not None:
                    self._lastPos = packet.pos
                    if (time.time() - last_update) > self.PROGRESS_UPDATE_DELAY:
                        self._notifyProgress(math.floor((packet.pos/fInput.size)*100))
                        last_update = time.time()

                if packet.stream.type == 'video':
                    self._processPacket(packet, outStreamVideo, fOutput, self._transcodeVideo)
                else:
                    self._processPacket(packet, outStreamAudio, fOutput, self._transcodeAudio)

            self._flushStream(outStreamVideo, fOutput, self._transcodeVideo)
            self._flushStream(outStreamAudio, fOutput, self._transcodeAudio)

        self._complete = True
        self._notifyProgress(100)

        return self._complete

    def _notifyProgress(self, progress: int) -> None:
        if self._progressCallback:
            self._progressCallback(progress, self._complete)

    def _processPacket(
        self,
        packet: Packet,
        stream: AvStream,
        outContainer: av.container.OutputContainer,
        doTranscode: bool
    ) -> None:
        if doTranscode:
            self._transcode(packet, stream, outContainer)
            return
        self._remux(packet, stream, outContainer)

    @staticmethod
    def _transcode(
        packet: Packet,
        stream: AvStream,
        outContainer: OutputContainer
    ) -> None:
        for frame in cast(Iterator[AvFrame], packet.decode()):
            frame.pts = None
            frame.time_base = None  # type: ignore # TODO: Check if zero Fraction will have the same effect!
            outContainer.mux(stream.encode(frame))  # type: ignore

    @staticmethod
    def _remux(
        packet: Packet,
        stream: AvStream,
        outContainer: OutputContainer
    ) -> None:
        packet.stream = stream
        if packet.dts:
            outContainer.mux(packet)  # type: ignore # TODO: Check if list wrapped will have the same effect!

    @staticmethod
    def _flushStream(
        stream: AvStream,
        outContainer: OutputContainer,
        doTranscode: bool
    ) -> None:
        if doTranscode:
            outContainer.mux(stream.encode())

    @staticmethod
    def _getFormatExtensions(filePath: Path) -> list[str]:  # type: ignore
        with av.open(str(filePath)) as fInput:
            return fInput.format.extensions  # type: ignore

    @staticmethod
    def _extractInputResolution(inputFile: Path, videoStreamId: StreamId) -> Resolution:  # type: ignore
        with av.open(str(inputFile)) as fInput:
            stream = fInput.streams.video[videoStreamId]
            return Resolution(width=stream.width, height=stream.height)

    @staticmethod
    def _extractInputCodecs(inputFile: Path, inputStreams: Streams) -> Codecs: # type: ignore
        with av.open(str(inputFile)) as fInput:
            return Codecs(
                audio=fInput.streams.audio[inputStreams.audio].codec_context.name,
                video=fInput.streams.video[inputStreams.video].codec_context.name
            )
