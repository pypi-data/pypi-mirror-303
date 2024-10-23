#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from PyQt5.QtCore import pyqtBoundSignal
from PyQt5.QtWidgets import QWidget
from tunit.unit import Milliseconds, Seconds

from kast.core.settings.SettingsKeys import SettingsKeys
from kast.interface.qt5.UiServices import UiServices
from kast.interface.qt5.service.UiEvent import UiEvent, UiState
from kast.interface.qt5.utils.mediaPlayer.MediaPlayerFacade import MediaPlayerFacade
from kast.interface.qt5.utils.mediaPlayer.MediaPlayerFactory import MediaPlayerBackend
from kast.interface.qt5.utils.mediaPlayer.frontend.VideoWidget import VideoWidget
from kast.interface.qt5.view.VideoPreviewView import Ui_VideoPreviewView
from kast.interface.qt5.viewModel.ViewModelBase import ViewBase, ViewModelBase
from kast.media.casting.model.CastPlayerState import CastPlayerState
from kast.media.casting.model.CastState import CastMediaState
from kast.utils.log.Loggable import Loggable


class View(ViewBase, QWidget, Ui_VideoPreviewView):
    pass


class VideoPreviewViewModel(Loggable, ViewModelBase[View]):

    POSITION_DELTA = Milliseconds(Seconds(2))

    def __init__(self, parent: QWidget, uiServices: UiServices) -> None:
        super().__init__(uiServices=uiServices, view=View.createView(parent=parent))
        self.uiServices.uiEventObserver.register(self, self._onUiEvent)

        self._videoWidget: VideoWidget = VideoWidget(logoPath=self.services.appInfo.appIconPath, parent=self.view)

        self.view.layoutPreview.addWidget(self._videoWidget)

        self._mediaPlayer: MediaPlayerFacade = MediaPlayerFacade(
            backend=MediaPlayerBackend(self.services.settingsFacade.get(SettingsKeys.MediaPreviewBackendEngine)),
            surface=self._videoWidget.surface,
            feignMode=self.services.appRuntimeFlags.recovery,
            parent=self.view
        )

        self.services.settingsFacade.subscribe(
            key=SettingsKeys.MediaPreviewBackendEngine,
            callback=lambda backend: self._onBackendChange(MediaPlayerBackend(backend))
        )

    @property
    def _mediaState(self) -> CastMediaState:
        return self.uiServices.uiStateService.castState.mediaState

    @property
    def signalOnVolumeMutedChange(self) -> pyqtBoundSignal:
        return self._mediaPlayer.signals.signalOnVolumeMutedChange

    @property
    def signalOnVolumeLevelChange(self) -> pyqtBoundSignal:
        return self._mediaPlayer.signals.signalOnVolumeLevelChange

    def triggerMuted(self) -> None:
        self._mediaPlayer.volumeMuted = not self._mediaPlayer.volumeMuted

    def setVolume(self, value: float) -> None:
        self._mediaPlayer.volumeLevel = value

    def _onStartup(self) -> None:
        self._mediaPlayer.init()

    def _onShutdown(self) -> None:
        self._mediaPlayer.shutdown()

    def _onUiEvent(self, uiEvent: UiEvent) -> None:
        state = uiEvent.state
        if state in [UiState.Idle, UiState.Streaming]:
            self._updateMediaFiles(disconnected=(state == UiState.Idle))

        if state == UiState.Streaming:
            self._updatePlayerState(state=self._mediaState.playerState)
            self._updateVideoPosition(position=self._mediaState.currentPosition)

    def _updateMediaFiles(self, disconnected: bool) -> None:
        self._mediaPlayer.mediaFile = self.services.mediaServer.mediaContent.movieFile if not disconnected else None
        self._mediaPlayer.subtitleFile = self.services.mediaServer.mediaContent.subtitlesFile if not disconnected else None

    def _updatePlayerState(self, state: CastPlayerState) -> None:
        actions = {
            CastPlayerState.Playing: self._mediaPlayer.play,
            CastPlayerState.Paused: self._mediaPlayer.pause,
            CastPlayerState.Buffering: self._mediaPlayer.pause,
            CastPlayerState.Idle: self._mediaPlayer.stop,
            CastPlayerState.Unknown: self._mediaPlayer.stop,
        }

        actions.get(state, lambda: None)()

    def _updateVideoPosition(self, position: Milliseconds) -> None:
        if self._mediaState.playerState in [CastPlayerState.Idle, CastPlayerState.Unknown]:
            return

        previewPosition = self._mediaPlayer.position
        if int(previewPosition) not in self._acceptablePositionRange(position):
            self.log.info(f"Updating preview position: {previewPosition} -> {position}")
            self._mediaPlayer.seek(position=position)

    def _acceptablePositionRange(self, position: Milliseconds) -> range:
        return range(
            int(position) - int(self.POSITION_DELTA),
            int(position) + int(self.POSITION_DELTA)
        )

    def _onBackendChange(self, backend: MediaPlayerBackend) -> None:
        self._mediaPlayer.setBackend(backend=backend)

        if self._mediaState.playerState not in [CastPlayerState.Idle, CastPlayerState.Unknown]:
            self._mediaPlayer.seek(position=self._mediaState.currentPosition)
