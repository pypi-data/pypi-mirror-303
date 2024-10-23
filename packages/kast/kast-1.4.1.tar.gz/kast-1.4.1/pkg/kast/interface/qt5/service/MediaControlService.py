#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import dataclasses
import threading
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import TypeVar

from PyQt5.QtCore import QObject, pyqtBoundSignal
from tunit.unit import Milliseconds

from kast.Services import Services
from kast.core.settings.SettingsKeys import SettingsKeys
from kast.interface.qt5.service.UiEvent import Progress, UiEvent, UiState
from kast.interface.qt5.service.UiStateService import UiStateService
from kast.interface.qt5.utils.QtAbc import QtAbc
from kast.interface.qt5.utils.QtHelper import QtHelper
from kast.interface.qt5.utils.dialog.DialogService import DialogService
from kast.interface.qt5.utils.threading.Schedulable import Schedulable
from kast.interface.qt5.utils.threading.ThreadContext import ThreadContext
from kast.media.casting.CastException import CastException
from kast.media.casting.model.CastState import CastMediaState, CastState
from kast.media.casting.model.DeviceInfo import DeviceInfo
from kast.media.processing.MetaData import MetaData, StreamInfo, SubtitleStreamInfo, SubtitleStreamType
from kast.media.processing.Resolution import Resolution
from kast.media.processing.SubtitleUtils import SubtitleException
from kast.media.processing.SubtitlesSource import SubtitlesFromFile, SubtitlesFromStream
from kast.media.processing.SubtitlesSourceList import SubtitlesSourceList
from kast.media.processing.Transcoder import Codecs, Streams, TranscodeParams, Transcoder
from kast.media.processing.common import StreamId
from kast.utils.Maybe import Maybe
from kast.utils.functional import Supplier
from kast.utils.log.Loggable import Loggable
from kast.utils.pathUtils import fileExtension
from kast.utils.typeUtils import castNotNull

_T = TypeVar('_T')


class SubtitleFileProvider:

    def __init__(self, supplier: Supplier[Path | None]) -> None:
        self._supplier: Supplier[Path | None] = supplier
        self._value: Path | None = None

    def resolve(self) -> Path | None:
        self._value = self._supplier()
        return self._value

    def get(self) -> Path | None:
        return self._value if self._value is not None\
            else self.resolve()


@dataclass
class StreamParams:
    videoFilePath: Path
    streamIds: Streams
    subtitleFileProvider: SubtitleFileProvider | None

    containerFormat: str
    codecs: Codecs
    maxResolution: Resolution

    deviceName: str


class StreamParamsMissingException(Exception):
    pass


class MediaControlService(QtAbc, QObject, Loggable, Schedulable):

    signalOnVideoFilePathChange: pyqtBoundSignal = QtHelper.declareSignal()
    signalOnVideoStreamIdChange: pyqtBoundSignal = QtHelper.declareSignal()
    signalOnAudioStreamIdChange: pyqtBoundSignal = QtHelper.declareSignal()
    signalOnSubtitleIdChange: pyqtBoundSignal = QtHelper.declareSignal()
    signalOnCastDeviceChange: pyqtBoundSignal = QtHelper.declareSignal()

    signalOnMetaDataChange: pyqtBoundSignal = QtHelper.declareSignal()
    signalOnSubtitleListChange: pyqtBoundSignal = QtHelper.declareSignal()

    _SUPPORTED_SUBTITLE_STREAM_TYPES: list[SubtitleStreamType] = [
        SubtitleStreamType.Text,
        SubtitleStreamType.Ass,
    ]

    def __init__(
        self,
        services: Services,
        threadContext: ThreadContext,
        dialogService: DialogService,
        uiStateService: UiStateService
    ) -> None:
        QObject.__init__(self, parent=None)
        Schedulable.__init__(self, threadContext=threadContext)

        self._services = services
        self._dialogService = dialogService
        self._uiStateService = uiStateService

        self._videoFilePath: Path | None = None
        self._videoStreamId: StreamId | None = None
        self._audioStreamId: StreamId | None = None
        self._subtitleId: int | None = None

        self._castDeviceInfo: DeviceInfo | None = None
        self._castContainerFormat: str | None = None
        self._castCodecs: Codecs | None = None
        self._castMaxResolution: Resolution | None = None

        self._metaData: MetaData | None = None
        self._subtitlesSourceList = SubtitlesSourceList()

        self.__streamParams: StreamParams | None = None
        self._lastStreamParams: StreamParams | None = None
        self._lastTranscodeParams: TranscodeParams | None = None

    @property
    def videoFilePath(self) -> Path | None:
        return self._videoFilePath

    @videoFilePath.setter
    def videoFilePath(self, value: Path | None) -> None:
        self._videoFilePath = value
        self._saveLastMediaDir(value)
        self.signalOnVideoFilePathChange.emit()

        self._extractMetaData(value)

    @property
    def videoStreamId(self) -> StreamId | None:
        return self._videoStreamId

    @videoStreamId.setter
    def videoStreamId(self, value: StreamId | None) -> None:
        self._videoStreamId = value
        self.signalOnVideoStreamIdChange.emit()

    @property
    def audioStreamId(self) -> StreamId | None:
        return self._audioStreamId

    @audioStreamId.setter
    def audioStreamId(self, value: StreamId | None) -> None:
        self._audioStreamId = value
        self.signalOnAudioStreamIdChange.emit()

    @property
    def subtitleId(self) -> int | None:
        return self._subtitleId

    @subtitleId.setter
    def subtitleId(self, value: int | None) -> None:
        self._subtitleId = value
        self.signalOnSubtitleIdChange.emit()

    @property
    def castDeviceInfo(self) -> DeviceInfo | None:
        return self._castDeviceInfo

    @castDeviceInfo.setter
    def castDeviceInfo(self, value: DeviceInfo | None) -> None:
        self._castDeviceInfo = value
        self.signalOnCastDeviceChange.emit()

    @property
    def castContainerFormat(self) -> str | None:
        return self._castContainerFormat

    @castContainerFormat.setter
    def castContainerFormat(self, value: str | None) -> None:
        self._castContainerFormat = value
        # TODO: Emit?

    @property
    def castCodecs(self) -> Codecs | None:
        return self._castCodecs

    @castCodecs.setter
    def castCodecs(self, value: Codecs | None) -> None:
        self._castCodecs = value
        # TODO: Emit?

    @property
    def castMaxResolution(self) -> Resolution | None:
        return self._castMaxResolution

    @castMaxResolution.setter
    def castMaxResolution(self, value: Resolution | None) -> None:
        self._castMaxResolution = value
        # TODO: Emit?

    @property
    def metaData(self) -> MetaData | None:
        return self._metaData

    @property
    def videoStreamList(self) -> list[str]:
        return Maybe(self._metaData)\
            .map(lambda metaData: self._getStreamNames(metaData.videoStreams))\
            .orElseGet(list)

    @property
    def audioStreamList(self) -> list[str]:
        return Maybe(self._metaData)\
            .map(lambda metaData: self._getStreamNames(metaData.audioStreams))\
            .orElseGet(list)

    @property
    def subtitleList(self) -> list[str]:
        return [subtitleSource.name for subtitleSource in self._subtitlesSourceList]

    @property
    def _castState(self) -> CastState:
        return self._uiStateService.castState

    @property
    def _mediaState(self) -> CastMediaState:
        return self._castState.mediaState

    @property
    def _streamParams(self) -> StreamParams:
        return Maybe(self.__streamParams)\
            .orThrow(lambda: StreamParamsMissingException("Stream params should not be null at this point!"))

    def hasStreamParamsChanged(self) -> bool:
        return (
            self._lastStreamParams is None or
            self._videoFilePath != self._lastStreamParams.videoFilePath or
            self._castContainerFormat != self._lastStreamParams.containerFormat or
            self._castMaxResolution != self._lastStreamParams.maxResolution or
            self._castCodecs != self._lastStreamParams.codecs or
            self._videoStreamId != self._lastStreamParams.streamIds.video or
            self._audioStreamId != self._lastStreamParams.streamIds.audio or
            Maybe(self._castDeviceInfo)
                .map(lambda device: device.name)
                .value != self._lastStreamParams.deviceName
        )

    def playOrPause(self) -> None:
        if self._mediaState.playerState.isStopped():
            self._startStreaming()
            return
        if self._mediaState.playerState.isPlaying():
            self._services.castController.pause()
            return
        self._services.castController.play()

    def stop(self) -> None:
        self._services.castController.stop()

    def seekForward(self) -> None:
        self._services.castController.seekForward()

    def seekBackward(self) -> None:
        self._services.castController.seekBackward()

    def seek(self, position: Milliseconds) -> None:
        self._services.castController.seek(position)

    def setMute(self, mute: bool = True) -> None:
        self._services.castController.setMute(mute)

    def setVolume(self, value: float) -> None:
        self._services.castController.setVolume(value)

    def addSubtitles(self, filePath: Path) -> None:
        self._saveLastMediaDir(filePath)

        self._subtitlesSourceList.append(SubtitlesFromFile(subtitlesFile=filePath))
        self.signalOnSubtitleIdChange.emit()

    def startStream(self) -> None:
        errors = []
        if self._videoFilePath is None:
            errors.append("No video file selected!")
        if self._videoStreamId is None:
            errors.append("No video stream selected!")
        if self._audioStreamId is None:
            errors.append("No audio stream selected!")
        if self._castDeviceInfo is None:
            errors.append("No cast device selected!")
        if self._castContainerFormat is None:
            errors.append("No media container format selected!")
        if self._castCodecs is None:
            errors.append("No codecs selected!")
        if self._castMaxResolution is None:
            errors.append("No max resolution specified!")

        if errors:
            errors = ["Could not start streaming! Preconditions that failed:"] + errors
            errorMessage = '\n - '.join(errors)
            self.log.error(errorMessage)
            self._dialogService.error(message=errorMessage)
            self._uiStateService.dispatch(UiEvent(state=UiState.Idle))
            return

        subtitleFileProvider = Maybe(self._subtitleId)\
            .map(lambda subId: SubtitleFileProvider(supplier=lambda: self._subtitlesSourceList[subId]
                    .toVtt(mediaProcessingService=self._services.mediaProcessingService)
            ))\
            .value
        self.__streamParams = StreamParams(
            videoFilePath=castNotNull(self._videoFilePath),
            streamIds=Streams(
                video=castNotNull(self._videoStreamId),
                audio=castNotNull(self._audioStreamId)
            ),
            subtitleFileProvider=subtitleFileProvider,
            containerFormat=castNotNull(self._castContainerFormat),
            codecs=castNotNull(self._castCodecs),
            maxResolution=castNotNull(self._castMaxResolution),
            deviceName=castNotNull(self._castDeviceInfo).name
        )

        self._initTranscoding()

    @Schedulable.backgroundTask
    def _extractMetaData(self, filePath: Path) -> None:
        self._uiStateService.dispatch(UiEvent(state=UiState.VideoProbe, progress=Progress(complete=False)))

        metaData = self._services.mediaProcessingService.extractMetaData(inputFile=filePath)
        filteredSubtitleStreams = self._extractSupportedSubtitleStreams(metaData=metaData)
        self._metaData = metaData = dataclasses.replace(metaData, subtitleStreams=filteredSubtitleStreams)
        self.signalOnMetaDataChange.emit()

        self._subtitlesSourceList.clear()
        for streamInfo in metaData.subtitleStreams:
            self._subtitlesSourceList.append(SubtitlesFromStream(
                mediaFile=filePath,
                streamInfo=streamInfo
            ))
        self.signalOnSubtitleListChange.emit()

        self._uiStateService.dispatch(UiEvent(state=UiState.Idle))

    @Schedulable.backgroundTask
    def _initTranscoding(self) -> None:
        streamParams = self._streamParams

        if streamParams.subtitleFileProvider is not None:
            self._uiStateService.dispatch(UiEvent(state=UiState.ConvertingSubtitles, progress=Progress(complete=False)))
            streamParams.subtitleFileProvider.resolve()

        self._uiStateService.dispatch(UiEvent(state=UiState.ConvertingMedia, progress=Progress(complete=False)))
        cancelEvent = threading.Event()

        def progressCallback(percent: int, complete: bool) -> None:
            self.log.info(f"Transcoding progress: {percent}% ({'Complete' if complete else 'Running'})")
            self._uiStateService.dispatch(UiEvent(state=UiState.ConvertingMedia, progress=Progress(
                complete=complete, percentage=percent, cancelEvent=cancelEvent
            )))

        transcoder = self._services.mediaProcessingService.createTranscoder(
            inputFile=streamParams.videoFilePath,
            inputStreamIds=streamParams.streamIds,
            outputCodecNames=streamParams.codecs,
            containerFormat=streamParams.containerFormat,
            maxResolution=streamParams.maxResolution,
            progressCallback=progressCallback,
            cancelEvent=cancelEvent
        )
        self.log.info(
            "Input file: "
            f"container='{fileExtension(streamParams.videoFilePath).lower()}', "
            f"codecs={transcoder.inputCodecNames}, "
            f"resolution={transcoder.inputResolution}"
        )
        self.log.info(
            "Output file: "
            f"container='{streamParams.containerFormat}', "
            f"codecs={transcoder.outputCodecNames}, "
            f"resolution={transcoder.outputResolution}"
        )
        if transcoder.requireProcessing and self._lastTranscodeParams != transcoder.params:
            self._startTranscoding(transcoder)
            return

        self._startStreaming(transcoder.outputFile)

    @Schedulable.backgroundTask
    def _startTranscoding(self, transcoder: Transcoder) -> None:
        if not transcoder.run():
            self._cancelAction()
            return

        self._lastTranscodeParams = transcoder.params

        self._confirmStreaming(transcoder.outputFile)

    @Schedulable.foregroundTask
    def _confirmStreaming(self, videoFile: Path) -> None:
        message = "Media processing finished!\n\nProceed with streaming?\n"

        self._dialogService.questionOkCancel(
            title="Streaming",
            message=message,
            onResult=lambda result: self._startStreaming(videoFile) if result else self._cancelAction()
        )

    @Schedulable.backgroundTask
    def _startStreaming(self, videoFile: Path | None = None) -> None:
        streamParams = self._streamParams
        self._lastStreamParams = streamParams

        if videoFile is not None:
            mediaContent = self._services.mediaServer.mediaContent
            mediaContent.movieFile = videoFile
            mediaContent.subtitlesFile = Maybe(streamParams.subtitleFileProvider)\
                .map(lambda holder: holder.get())\
                .value

        self._uiStateService.dispatch(UiEvent(state=UiState.Connecting, progress=Progress(complete=False)))

        self._services.castController.connect(name=streamParams.deviceName)
        movieUrl = self._services.mediaServer.movieUrl
        if movieUrl is None:
            raise Exception('Movie URL cannot be null!')
        self._services.castController.stream(
            movieUrl=movieUrl,
            subtitlesUrl=self._services.mediaServer.subtitleUrl,
            thumbnailUrl=self._services.mediaServer.thumbnailUrl,
            title=Maybe(self._metaData).map(lambda metaData: metaData.title)
                .orThrow(lambda: Exception("Meta data missing!"))
        )

        self._uiStateService.dispatch(UiEvent(state=UiState.Streaming))

    @classmethod
    def _extractSupportedSubtitleStreams(cls, metaData: MetaData) -> list[SubtitleStreamInfo]:
        filteredStreams = []
        for stream in metaData.subtitleStreams:
            if stream.type not in cls._SUPPORTED_SUBTITLE_STREAM_TYPES:
                cls.log.warning(f"Unsupported subtitle stream detected! Stream: {stream}")
                continue
            filteredStreams.append(stream)

        return filteredStreams

    def _cancelAction(self) -> None:
        self._uiStateService.dispatch(UiEvent(state=UiState.Idle))

    @Schedulable.backgroundTask
    def _saveLastMediaDir(self, filePath: Path | None) -> None:
        if filePath is not None:
            self._services.settingsFacade.set(key=SettingsKeys.BrowseMediaPath, value=str(filePath.parent))

    @Schedulable.foregroundTask
    def _reportError(self, message: str) -> None:
        self._dialogService.error(message=message)
        self._uiStateService.dispatch(UiEvent(state=UiState.Idle))

    @staticmethod
    def _getStreamNames(streams: Iterable[StreamInfo]) -> list[str]:
        return [stream.name for stream in streams]

    def _onBackgroundException(self, ex: Exception) -> None:
        try:
            raise ex
        except (SubtitleException, CastException) as ex:
            self.log.exception(ex)
            self._reportError(str(ex))
