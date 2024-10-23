#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from collections.abc import Callable
from enum import IntEnum, auto
from typing import cast

from PyQt5.QtCore import QObject, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from tunit.unit import Milliseconds

from kast.interface.qt5.utils.mediaPlayer.MediaPlayerState import MediaPlayerState
from kast.interface.qt5.utils.mediaPlayer.backend.common.MediaPlayerBase import MediaPlayerBase
from kast.interface.qt5.utils.mediaPlayer.frontend.VideoSurface import VideoSurface
from kast.utils.Maybe import Maybe
from kast.utils.OsInfo import OsInfo, OsName

QVolume = int
Volume = float


class QtMediaPlayer(MediaPlayerBase):

    class EnumBase(IntEnum):
        def __str__(self) -> str:
            return f"{self.name}[{self.value}]"

    class Error(EnumBase):
        NoError = QMediaPlayer.NoError
        ResourceError = QMediaPlayer.ResourceError
        FormatError = QMediaPlayer.FormatError
        NetworkError = QMediaPlayer.NetworkError
        AccessDeniedError = QMediaPlayer.AccessDeniedError
        ServiceMissingError = QMediaPlayer.ServiceMissingError

    class MediaState(EnumBase):
        UnknownMediaStatus = QMediaPlayer.MediaStatus.UnknownMediaStatus
        NoMedia = QMediaPlayer.MediaStatus.NoMedia
        LoadingMedia = QMediaPlayer.MediaStatus.LoadingMedia
        LoadedMedia = QMediaPlayer.MediaStatus.LoadedMedia
        StalledMedia = QMediaPlayer.MediaStatus.StalledMedia
        BufferingMedia = QMediaPlayer.MediaStatus.BufferingMedia
        BufferedMedia = QMediaPlayer.MediaStatus.BufferedMedia
        EndOfMedia = QMediaPlayer.MediaStatus.EndOfMedia
        InvalidMedia = QMediaPlayer.MediaStatus.InvalidMedia

    class PlayerState(EnumBase):
        StoppedState = QMediaPlayer.State.StoppedState
        PlayingState = QMediaPlayer.State.PlayingState
        PausedState = QMediaPlayer.State.PausedState

    class SeekPhase(IntEnum):
        DelayConcluded = auto()
        PositionAdjusted = auto()
        FrameLoaded = auto()

    _Q_MAX_VOLUME: QVolume = 100

    _LOADED_MEDIA_THRESHOLD: MediaState = MediaState.LoadedMedia

    _STATE_MAPPING = {
        QMediaPlayer.State.PlayingState: MediaPlayerState.Playing,
        QMediaPlayer.State.PausedState: MediaPlayerState.Paused,
        QMediaPlayer.State.StoppedState: MediaPlayerState.Stopped,
    }

    def __init__(
        self,
        surface: VideoSurface,
        parent: QObject | None = None
    ) -> None:
        super().__init__(
            surface=surface,
            parent=parent
        )

        self._coreMediaState: QtMediaPlayer.MediaState = QtMediaPlayer.MediaState.NoMedia

        self._maybeCore: Maybe[QMediaPlayer] = Maybe()

    def shutdown(self) -> None:
        super().shutdown()
        self._shutdownCore()

    def _onStateChange(self, state: MediaPlayerState) -> None:
        super()._onStateChange(state)

        coreState = self._maybeCore.map(lambda core: core.state())\
            .orElse(QMediaPlayer.State.StoppedState)
        if state == self._STATE_MAPPING[coreState]:
            return

        self._handleState(state=state)

    def _handleState(self, state: MediaPlayerState) -> None:
        self._initCore()

        actions = {
            MediaPlayerState.Seeking: self._handleSeek,
            MediaPlayerState.Playing: self._handlePlay,
            MediaPlayerState.Paused: self._handlePause,
            MediaPlayerState.Stopped: self._handleStop,
        }
        actions.get(state, lambda: None)()

    def _handleSeek(self) -> None:
        self._handleStopWatchUpdate(state=MediaPlayerState.Seeking)
        self._maybeCore.filter(lambda core: self._isMediaLoaded())\
            .ifPresent(lambda core: core.setPosition(int(self._mediaDetails.startPosition)))

    def _handlePlay(self) -> None:
        self._maybeCore.ifPresent(lambda core: core.play())

    def _handlePause(self) -> None:
        self._maybeCore.ifPresent(lambda core: core.pause())

    def _handleStop(self) -> None:
        self._shutdownCore()

    def _handleStopWatchUpdate(self, state: MediaPlayerState) -> None:
        actions = {
            MediaPlayerState.Playing: lambda: self._stopWatch.start(),
            MediaPlayerState.Paused: lambda: self._stopWatch.pause(),
            MediaPlayerState.Buffering: lambda: self._stopWatch.pause(),
            MediaPlayerState.Seeking: lambda: self._stopWatch.stop(),
            MediaPlayerState.Stopped: lambda: self._stopWatch.stop(),
        }
        actions.get(state, lambda: None)()

    def _onCoreStateChange(self, qState: QMediaPlayer.State) -> None:
        state = self._STATE_MAPPING[qState]
        nativeWrapper = QtMediaPlayer.PlayerState(qState)
        self.log.info(f'Core state changed to: {state.name} (native={nativeWrapper})')

        self._handleStopWatchUpdate(state=state)

        if state == MediaPlayerState.Playing:
            self._onCoreSeek(phase=QtMediaPlayer.SeekPhase.FrameLoaded)

    def _onCorePositionChange(self, position: int) -> None:
        self.log.debug(f'Core position changed: {position}')
        self._onCoreSeek(phase=QtMediaPlayer.SeekPhase.PositionAdjusted)

    def _onCoreDurationChange(self, duration: int) -> None:
        self.log.info(f'Core detected duration: {duration}')
        self._mediaDetails.duration = Milliseconds(duration)

    def _onCoreMediaStateChange(self, mediaState: QMediaPlayer.MediaStatus) -> None:
        self._coreMediaState = coreMediaState = QtMediaPlayer.MediaState(mediaState)
        self.log.info(f"Core media state changed: {coreMediaState}]")

        if coreMediaState == self._LOADED_MEDIA_THRESHOLD:
            self._onCoreSeek(phase=QtMediaPlayer.SeekPhase.DelayConcluded)

    def _onVolumeMutedChange(self, value: bool) -> None:
        self._maybeCore.ifPresent(lambda core: core.setMuted(value))

    def _onVolumeLevelChange(self, value: float) -> None:
        self._maybeCore.ifPresent(lambda core: core.setVolume(self._volumeToQVolume(value)))

    def _onCoreError(self, core: QMediaPlayer) -> None:
        errorMessage = self._errorToStr(cast(Callable[[], QMediaPlayer.Error], core.error)())
        self.log.error(f"Media player error: {errorMessage}")
        self._surface.reportError(errorMessage=f'Error: {errorMessage}')

    def _onCoreSeek(self, phase: SeekPhase) -> None:
        if self._mediaDetails.state != MediaPlayerState.Seeking:
            return
        if not self._isMediaLoaded():
            return

        if phase == QtMediaPlayer.SeekPhase.DelayConcluded:
            self.log.info("[Seek] Starting delayed media seek!")
            self._handleSeek()
            return

        startState = self._mediaDetails.startState
        if(
            OsInfo.name == OsName.Windows and
            phase == QtMediaPlayer.SeekPhase.PositionAdjusted and
            startState == MediaPlayerState.Paused
        ):
            self.log.info(f'[Seek] Delaying requested start state application to load frame.')
            self._maybeCore.ifPresent(lambda core: core.play())
            return

        self.log.info(f'[Seek] Applying requested start state: {startState.name}')
        self._mediaDetails.state = startState

    def _isMediaLoaded(self) -> bool:
        return self._coreMediaState >= self._LOADED_MEDIA_THRESHOLD

    def _initCore(self) -> None:
        if self._maybeCore.isPresent():
            return

        mediaFilePath = self._mediaDetails.mediaFilePath
        if mediaFilePath is None:
            self.log.error('Cannot init player core without media file path!')
            return

        core = QMediaPlayer(self, QMediaPlayer.VideoSurface)

        core.setVideoOutput(self._surface)

        core.error.connect(lambda: self._onCoreError(core=core))
        core.stateChanged.connect(self._onCoreStateChange)
        core.mediaStatusChanged.connect(self._onCoreMediaStateChange)
        core.durationChanged.connect(self._onCoreDurationChange)
        core.positionChanged.connect(self._onCorePositionChange)

        core.setMuted(self._mediaDetails.volumeMuted)
        core.setVolume(self._volumeToQVolume(self._mediaDetails.volumeLevel))

        mediaContent = QMediaContent(QUrl.fromLocalFile(str(mediaFilePath)))
        core.setMedia(mediaContent)

        self._maybeCore = Maybe(core)

    def _shutdownCore(self) -> None:
        maybeCore = self._maybeCore
        if maybeCore.isEmpty():
            return

        self._maybeCore = Maybe()
        core = cast(QMediaPlayer, maybeCore.value)

        core.stop()

        core.setMedia(QMediaContent(None))  # type: ignore
        core.setVideoOutput(None)  # type: ignore

        core.error.disconnect()
        core.stateChanged.disconnect()
        core.mediaStatusChanged.disconnect()
        core.durationChanged.disconnect()
        core.positionChanged.disconnect()

        core.disconnect()
        core.deleteLater()

        self._surface.stop()

    @classmethod
    def _volumeToQVolume(cls, volume: Volume) -> QVolume:
        return QVolume(volume * cls._Q_MAX_VOLUME)

    @classmethod
    def _qVolumeToVolume(cls, qVolume: QVolume) -> Volume:
        return Volume(qVolume / cls._Q_MAX_VOLUME)

    @classmethod
    def _errorToStr(cls, errorCode: int) -> str:
        return str(cls.Error(errorCode)) if errorCode in [er.value for er in cls.Error]\
            else f'Unknown[{errorCode}]'
