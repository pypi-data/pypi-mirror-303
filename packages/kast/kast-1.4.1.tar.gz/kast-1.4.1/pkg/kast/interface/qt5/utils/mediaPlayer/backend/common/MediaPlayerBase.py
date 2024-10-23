#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from abc import abstractmethod
from pathlib import Path
from typing import cast

from PyQt5.QtCore import QObject, QTimer
from tunit.unit import Milliseconds, Seconds

from kast.interface.qt5.utils.QtAbc import QtAbc
from kast.interface.qt5.utils.mediaPlayer.IMediaPlayer import IMediaPlayer
from kast.interface.qt5.utils.mediaPlayer.MediaPlayerSignals import MediaPlayerSignals
from kast.interface.qt5.utils.mediaPlayer.MediaPlayerState import MediaPlayerState
from kast.interface.qt5.utils.mediaPlayer.backend.common.core.MediaDetails import MediaDetails
from kast.interface.qt5.utils.mediaPlayer.backend.common.subtitle.SubtitleEngine import SubtitleEngine
from kast.interface.qt5.utils.mediaPlayer.frontend.VideoSurface import VideoSurface
from kast.utils.StopWatch import StopWatch
from kast.utils.log.Loggable import Loggable


class MediaPlayerBase(QtAbc, QObject, IMediaPlayer, Loggable):

    POSITION_UPDATE_INTERVAL = Milliseconds(Seconds(1))

    def __init__(
        self,
        surface: VideoSurface,
        parent: QObject | None = None
    ) -> None:
        super().__init__(parent=parent)
        self._surface = surface

        self._signals = MediaPlayerSignals(self)
        self._stopWatch = StopWatch()
        self._mediaDetails = MediaDetails(
            signals=self._signals,
            positionTracker=self._stopWatch,
            parent=self
        )

        self._subtitleEngine: SubtitleEngine = SubtitleEngine(
            surface=surface,
            positionSupplier=lambda: self._mediaDetails.position
        )

        self._signals.signalOnVolumeMutedChange.connect(self._onVolumeMutedChange)
        self._signals.signalOnVolumeLevelChange.connect(self._onVolumeLevelChange)
        self._signals.signalOnStateChange.connect(self._onStateChange)

        self._videoPositionUpdater = QTimer(self)
        self._videoPositionUpdater.setInterval(int(self.POSITION_UPDATE_INTERVAL))
        self._videoPositionUpdater.timeout.connect(self._mediaDetails.notifyPositionChanged)
        self._videoPositionUpdater.start()

    @property
    def signals(self) -> MediaPlayerSignals:
        return self._signals

    def init(self) -> None:
        self._subtitleEngine.init()

    def shutdown(self) -> None:
        self._subtitleEngine.shutdown()

    def getVolumeMuted(self) -> bool:
        return self._mediaDetails.volumeMuted

    def setVolumeMuted(self, value: bool) -> None:
        self._mediaDetails.volumeMuted = value

    def getVolumeLevel(self) -> float:
        return self._mediaDetails.volumeLevel

    def setVolumeLevel(self, value: float) -> None:
        self._mediaDetails.volumeLevel = value

    def getMediaFile(self) -> Path | None:
        return self._mediaDetails.mediaFilePath

    def setMediaFile(self, mediaFilePath: Path | None = None) -> None:
        self.setSubtitleFile(None)
        self._mediaDetails.mediaFilePath = mediaFilePath

    def getSubtitleFile(self) -> Path | None:
        return self._subtitleEngine.getSubtitleFile()

    def setSubtitleFile(self, subtitleFilePath: Path | None = None) -> None:
        self._subtitleEngine.setSubtitleFile(subtitleFilePath)

    def getState(self) -> MediaPlayerState:
        return self._mediaDetails.state

    def getDuration(self) -> Milliseconds:
        return self._mediaDetails.duration

    def getPosition(self) -> Milliseconds:
        return self._mediaDetails.position

    def play(self) -> None:
        if self._mediaDetails.state not in [
            MediaPlayerState.Stopped,
            MediaPlayerState.Paused,
        ]:
            return

        if self._mediaDetails.mediaFilePath is None:
            return

        self._mediaDetails.state = MediaPlayerState.Playing

    def pause(self) -> None:
        if self._mediaDetails.state not in [
            MediaPlayerState.Stopped,
            MediaPlayerState.Playing,
        ]:
            return

        self._mediaDetails.state = MediaPlayerState.Paused

    def stop(self) -> None:
        if self._mediaDetails.state not in [
            MediaPlayerState.Playing,
            MediaPlayerState.Paused,
        ]:
            return

        self._mediaDetails.state = MediaPlayerState.Stopped

    def seek(
        self,
        position: Milliseconds,
        play: bool | None = None
    ) -> None:
        if self._mediaDetails.state not in [
            MediaPlayerState.Stopped,
            MediaPlayerState.Playing,
            MediaPlayerState.Paused,
        ]:
            return

        state = {
            True: lambda: MediaPlayerState.Playing,
            False: lambda: MediaPlayerState.Paused,
        }.get(cast(bool, play), lambda: self._mediaDetails.state)()

        self._mediaDetails.startPosition = position
        self._mediaDetails.startState = state

        self._mediaDetails.state = MediaPlayerState.Seeking

    def _onStateChange(self, state: MediaPlayerState) -> None:
        self._subtitleEngine.setState(state=state)

    @abstractmethod
    def _onVolumeMutedChange(self, value: bool) -> None:
        pass

    @abstractmethod
    def _onVolumeLevelChange(self, value: float) -> None:
        pass
