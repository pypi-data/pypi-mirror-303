#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from pathlib import Path

from PyQt5.QtCore import QObject
from tunit.unit import Milliseconds

from kast.interface.qt5.utils.QtAbc import QtAbc
from kast.interface.qt5.utils.mediaPlayer.IMediaPlayer import IMediaPlayer
from kast.interface.qt5.utils.mediaPlayer.MediaPlayerFactory import MediaPlayerBackend, MediaPlayerFactory
from kast.interface.qt5.utils.mediaPlayer.MediaPlayerSignals import MediaPlayerSignals
from kast.interface.qt5.utils.mediaPlayer.MediaPlayerState import MediaPlayerState
from kast.interface.qt5.utils.mediaPlayer.frontend.VideoSurface import VideoSurface
from kast.utils.log.Loggable import Loggable


class MediaPlayerFacade(QtAbc, QObject, IMediaPlayer, Loggable):

    def __init__(
        self,
        backend: MediaPlayerBackend,
        surface: VideoSurface,
        feignMode: bool = False,
        parent: QObject | None = None
     ) -> None:
        super().__init__(parent=parent)

        self._feignMode: bool = feignMode

        self._backend: MediaPlayerBackend = backend
        self._surface: VideoSurface = surface

        self._signals: MediaPlayerSignals = MediaPlayerSignals(parent=self)

        self._mediaPlayers: dict[MediaPlayerBackend, IMediaPlayer] = {}
        self._mediaPlayer: IMediaPlayer = self._getMediaPlayer(backend=backend)

        self._connectSignals(mediaPlayer=self._mediaPlayer)

    @property
    def signals(self) -> MediaPlayerSignals:
        return self._signals

    def getState(self) -> MediaPlayerState:
        return self._mediaPlayer.getState()

    def getDuration(self) -> Milliseconds:
        return self._mediaPlayer.getDuration()

    def getPosition(self) -> Milliseconds:
        return self._mediaPlayer.getPosition()

    def getVolumeMuted(self) -> bool:
        return self._mediaPlayer.getVolumeMuted()

    def setVolumeMuted(self, value: bool) -> None:
        self._mediaPlayer.setVolumeMuted(value)

    def getVolumeLevel(self) -> float:
        return self._mediaPlayer.getVolumeLevel()

    def setVolumeLevel(self, value: float) -> None:
        self._mediaPlayer.setVolumeLevel(value)

    def getBackend(self) -> MediaPlayerBackend:
        return self._backend

    def setBackend(self, backend: MediaPlayerBackend) -> None:
        if backend == self._backend:
            return

        self.log.info(f"Switching backend: '{self._backend.name}' -> '{backend.name}'")

        oldPlayer = self._mediaPlayer

        state = oldPlayer.getState()
        position = oldPlayer.getPosition()

        mediaFile = oldPlayer.getMediaFile()
        subtitleFile = oldPlayer.getSubtitleFile()
        volumeMuted = oldPlayer.getVolumeMuted()
        volumeLevel = oldPlayer.getVolumeLevel()

        self._disconnectSignals(mediaPlayer=oldPlayer)

        oldPlayer.shutdown()

        newPlayer = self._getMediaPlayer(backend=backend)
        newPlayer.init()

        self._connectSignals(mediaPlayer=newPlayer)

        newPlayer.setMediaFile(mediaFile)
        newPlayer.setSubtitleFile(subtitleFile)
        newPlayer.setVolumeMuted(volumeMuted)
        newPlayer.setVolumeLevel(volumeLevel)

        self._backend = backend
        self._mediaPlayer = newPlayer

        if state != MediaPlayerState.Stopped:
            newPlayer.seek(position=position, play=(state == MediaPlayerState.Playing))

    def init(self) -> None:
        self.log.info(f"Using surface renderer: '{self._surface.renderer}'")
        if not self._feignMode:
            self.log.info(f"Using backend: '{self._backend.name}'")
        else:
            self.log.info("Running in feign mode! (Only null backend will be used.)")
        self._mediaPlayer.init()

    def shutdown(self) -> None:
        self.log.info("Shutting down!")
        self._mediaPlayer.shutdown()

    def getMediaFile(self) -> Path | None:
        return self._mediaPlayer.getMediaFile()

    def setMediaFile(self, mediaFilePath: Path | None = None) -> None:
        self._mediaPlayer.setMediaFile(mediaFilePath)

    def getSubtitleFile(self) -> Path | None:
        return self._mediaPlayer.getSubtitleFile()

    def setSubtitleFile(self, subtitleFilePath: Path | None = None) -> None:
        self._mediaPlayer.setSubtitleFile(subtitleFilePath)

    def play(self) -> None:
        self._mediaPlayer.play()

    def pause(self) -> None:
        self._mediaPlayer.pause()

    def stop(self) -> None:
        self._mediaPlayer.stop()

    def seek(
        self,
        position: Milliseconds,
        play: bool | None = None
    ) -> None:
        self._mediaPlayer.seek(position=position, play=play)

    def _onSignalOnStateChange(self, state: MediaPlayerState) -> None:
        self._signals.signalOnStateChange.emit(state)

    def _onSignalOnDurationChange(self, duration: int) -> None:
        self._signals.signalOnDurationChange.emit(duration)

    def _onSignalOnPositionChange(self, position: int) -> None:
        self._signals.signalOnPositionChange.emit(position)

    def _onSignalOnVolumeMutedChange(self, muted: bool) -> None:
        self._signals.signalOnVolumeMutedChange.emit(muted)

    def _onSignalOnVolumeLevelChange(self, level: float) -> None:
        self._signals.signalOnVolumeLevelChange.emit(level)

    def _getMediaPlayer(self, backend: MediaPlayerBackend) -> IMediaPlayer:
        mediaPlayer = self._mediaPlayers.get(backend)
        return mediaPlayer if mediaPlayer is not None \
            else MediaPlayerFactory.create(
                backend=backend,
                surface=self._surface,
                feignMode=self._feignMode,
                parent=self
            )

    def _connectSignals(self, mediaPlayer: IMediaPlayer) -> None:
        mediaPlayer.signals.signalOnStateChange.connect(self._onSignalOnStateChange)
        mediaPlayer.signals.signalOnDurationChange.connect(self._onSignalOnDurationChange)
        mediaPlayer.signals.signalOnPositionChange.connect(self._onSignalOnPositionChange)
        mediaPlayer.signals.signalOnVolumeMutedChange.connect(self._onSignalOnVolumeMutedChange)
        mediaPlayer.signals.signalOnVolumeLevelChange.connect(self._onSignalOnVolumeLevelChange)

    @staticmethod
    def _disconnectSignals(mediaPlayer: IMediaPlayer) -> None:
        mediaPlayer.signals.signalOnStateChange.disconnect()
        mediaPlayer.signals.signalOnDurationChange.disconnect()
        mediaPlayer.signals.signalOnPositionChange.disconnect()
        mediaPlayer.signals.signalOnVolumeMutedChange.disconnect()
        mediaPlayer.signals.signalOnVolumeLevelChange.disconnect()
