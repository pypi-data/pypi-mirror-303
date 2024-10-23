#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from pathlib import Path

import av
from av.stream import Stream
from av.audio.stream import AudioStream
from av.container.input import InputContainer
from av.subtitles.stream import SubtitleStream
from av.video.stream import VideoStream

from kast.media.processing.MetaData import AudioStreamInfo, MediaStreamInfo, MetaData, StreamInfo, SubtitleStreamInfo, \
    SubtitleStreamType, VideoStreamInfo
from kast.media.processing.Resolution import Resolution
from kast.media.processing.common import StreamId
from kast.utils.log.Loggable import Loggable
from kast.utils.pathUtils import fileExtension


class MediaInfoExtractor(Loggable):

    @classmethod
    def extractMetaData(cls, inputFile: Path) -> MetaData:  # type: ignore
        with av.open(str(inputFile)) as f:
            return MetaData(
                title=inputFile.stem,
                containerType=fileExtension(filePath=inputFile).lower(),
                videoStreams=[cls._extractVideoStreamInfo(streamId=idx, stream=stream) for idx, stream in enumerate(f.streams.video)],
                audioStreams=[cls._extractAudioStreamInfo(streamId=idx, stream=stream) for idx, stream in enumerate(f.streams.audio)],
                subtitleStreams=[cls._extractSubtitleStreamInfo(streamId=idx, stream=stream, container=f) for idx, stream in enumerate(f.streams.subtitles)]
            )

    @classmethod
    def _extractVideoStreamInfo(cls, streamId: StreamId, stream: VideoStream) -> VideoStreamInfo:
        streamInfo = cls._extractMediaStreamInfo(streamId=streamId, stream=stream)
        return VideoStreamInfo(
            **vars(streamInfo),
            resolution=Resolution(width=stream.width, height=stream.height)
        )

    @classmethod
    def _extractAudioStreamInfo(cls, streamId: StreamId, stream: AudioStream) -> AudioStreamInfo:
        streamInfo = cls._extractMediaStreamInfo(streamId=streamId, stream=stream)
        return AudioStreamInfo(**vars(streamInfo))

    @classmethod
    def _extractMediaStreamInfo(cls, streamId: StreamId, stream: Stream) -> MediaStreamInfo:
        streamInfo = cls._extractStreamInfo(streamId=streamId, stream=stream)
        return MediaStreamInfo(
            **vars(streamInfo),
            codecName=stream.codec_context.name
        )

    @classmethod
    def _extractSubtitleStreamInfo(cls, streamId: StreamId, stream: SubtitleStream, container: InputContainer) -> SubtitleStreamInfo:
        streamInfo = cls._extractStreamInfo(streamId=streamId, stream=stream)
        return SubtitleStreamInfo(
            **vars(streamInfo),
            type=cls._extractSubtitleStreamType(stream=stream, container=container)
        )

    @staticmethod
    def _extractStreamInfo(streamId: StreamId, stream: Stream) -> StreamInfo:
        return StreamInfo(
            id=streamId,
            language=stream.language,
            title=stream.metadata.get('title')
        )

    @classmethod
    def _extractSubtitleStreamType(cls, stream: SubtitleStream, container: InputContainer) -> SubtitleStreamType:
        try:
            for frame in container.decode(stream):
                if not len(frame.rects):  # type: ignore
                    continue

                subtitleStreamTypeStr = frame.rects[0].type.decode('ascii')  # type: ignore
                return SubtitleStreamType(subtitleStreamTypeStr)

        except ValueError as ex:
            cls.log.exception("Failed to detect subtitle stream type! (Will mark as unknown.) Reason:", ex)

        return SubtitleStreamType.Unknown
