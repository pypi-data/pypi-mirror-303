#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import time

from PyQt5.QtCore import QObject, QTimer, pyqtBoundSignal
from PyQt5.QtWidgets import QStyle, QWidget
from tunit.unit import Milliseconds, Seconds

from kast.interface.qt5.UiServices import UiServices
from kast.interface.qt5.service.UiEvent import UiEvent, UiState
from kast.interface.qt5.utils.QtHelper import QtHelper
from kast.interface.qt5.view.MediaControlView import Ui_MediaControlView
from kast.interface.qt5.viewModel.ViewModelBase import ViewBase, ViewModelBase
from kast.media.casting.model.CastPlayerState import CastPlayerState
from kast.media.casting.model.CastState import CastMediaState


class View(ViewBase, QWidget, Ui_MediaControlView):
    pass


class MediaControlViewModel(ViewModelBase[View]):

    class Signals(QObject):
        signalOnVolumeMutedChange: pyqtBoundSignal = QtHelper.declareSignal()
        signalOnVolumeLevelChange: pyqtBoundSignal = QtHelper.declareSignal(float)

    def __init__(
        self,
        parent: QWidget,
        uiServices: UiServices
    ) -> None:
        super().__init__(uiServices=uiServices, view=View.createView(parent=parent))
        self.uiServices.uiEventObserver.register(self, self._onUiEvent)

        self._signals = MediaControlViewModel.Signals(parent=self.view)

        self.view.buttonPlayPause.setIcon(self.view.style().standardIcon(QStyle.SP_MediaPlay))
        self.view.buttonStop.setIcon(self.view.style().standardIcon(QStyle.SP_MediaStop))
        self.view.buttonSeekFront.setIcon(self.view.style().standardIcon(QStyle.SP_MediaSeekForward))
        self.view.buttonSeekBack.setIcon(self.view.style().standardIcon(QStyle.SP_MediaSeekBackward))
        self.view.buttonMuteRemote.setIcon(self.view.style().standardIcon(QStyle.SP_MediaVolume))
        self.view.buttonMuteLocal.setIcon(self.view.style().standardIcon(QStyle.SP_MediaVolume))

        self._videoPositionUpdater = QTimer()
        self._videoPositionUpdater.setInterval(int(Milliseconds(Seconds(1))))
        self._videoPositionUpdater.timeout.connect(self._signalVideoPositionUpdate)
        self._videoPositionUpdater.start()

        self.view.buttonDisconnect.clicked.connect(self._signalClickedDisconnect)
        self.view.buttonPlayPause.clicked.connect(self._signalClickedPlayPause)
        self.view.buttonStop.clicked.connect(self._signalClickedStop)
        self.view.buttonSeekFront.clicked.connect(self._signalClickedSeekForward)
        self.view.buttonSeekBack.clicked.connect(self._signalClickedSeekBackward)
        self.view.buttonMuteRemote.clicked.connect(self._signalClickedMuteRemote)
        self.view.buttonMuteLocal.clicked.connect(self._signalClickedMuteLocal)

        self.view.sliderSeek.sliderReleased.connect(self._signalSeekPosition)
        self.view.sliderVolumeRemote.sliderReleased.connect(self._signalSetVolumeRemote)
        self.view.sliderVolumeLocal.sliderReleased.connect(self._signalSetVolumeLocal)

        self.view.setVisible(False)

    @property
    def _mediaState(self) -> CastMediaState:
        return self.uiServices.uiStateService.castState.mediaState

    @property
    def signalOnVolumeMutedChange(self) -> pyqtBoundSignal:
        return self._signals.signalOnVolumeMutedChange

    @property
    def signalOnVolumeLevelChange(self) -> pyqtBoundSignal:
        return self._signals.signalOnVolumeLevelChange

    def setLocalMute(self, muted: bool) -> None:
        iconMuted = QStyle.SP_MediaVolumeMuted if muted else QStyle.SP_MediaVolume
        self.view.buttonMuteLocal.setIcon(self.view.style().standardIcon(iconMuted))

    def setLocalVolume(self, volume: float) -> None:
        self.view.sliderVolumeLocal.setValue(int(100 * volume))

    def _onUiEvent(self, uiEvent: UiEvent) -> None:
        self.view.setVisible(uiEvent.state == UiState.Streaming)

        iconPlayPause = QStyle.SP_MediaPause if self._mediaState.playerState.isPlaying() else QStyle.SP_MediaPlay
        self.view.buttonPlayPause.setIcon(self.view.style().standardIcon(iconPlayPause))

        self._updateVideoPosition(position=self._mediaState.currentPosition, duration=self._mediaState.duration)

        volumeLevel = int(round(self._mediaState.volumeLevel * 100))
        self.view.sliderVolumeRemote.setSliderPosition(volumeLevel)

        iconMuted = QStyle.SP_MediaVolumeMuted if self._mediaState.volumeMuted or volumeLevel == 0 else QStyle.SP_MediaVolume
        self.view.buttonMuteRemote.setIcon(self.view.style().standardIcon(iconMuted))

    def _updateVideoPosition(self, position: Milliseconds, duration: Milliseconds) -> None:
        def formatTime(value: Milliseconds) -> str:
            return time.strftime('%H:%M:%S', time.gmtime(int(Seconds(value))))

        self.view.labelTime.setText(f"{formatTime(position)} / {formatTime(duration)}")

        if not self.view.sliderSeek.isSliderDown():
            self.view.sliderSeek.setRange(0, int(duration))
            self.view.sliderSeek.setSliderPosition(int(position))

    def _signalVideoPositionUpdate(self) -> None:
        if self._mediaState.playerState == CastPlayerState.Playing:
            self._updateVideoPosition(
                position=self._mediaState.currentPosition,
                duration=self._mediaState.duration
            )

    def _signalClickedDisconnect(self) -> None:
        self.services.castController.disconnect()

    def _signalClickedPlayPause(self) -> None:
        self.uiServices.mediaControlService.playOrPause()

    def _signalClickedStop(self) -> None:
        self.uiServices.mediaControlService.stop()

    def _signalClickedSeekForward(self) -> None:
        self.uiServices.mediaControlService.seekForward()

    def _signalClickedSeekBackward(self) -> None:
        self.uiServices.mediaControlService.seekBackward()

    def _signalSeekPosition(self) -> None:
        self.uiServices.mediaControlService.seek(Milliseconds(self.view.sliderSeek.value()))

    def _signalClickedMuteRemote(self) -> None:
        self.uiServices.mediaControlService.setMute(not self._mediaState.volumeMuted)

    def _signalSetVolumeRemote(self) -> None:
        self.uiServices.mediaControlService.setVolume(self.view.sliderVolumeRemote.value()/100)

    def _signalClickedMuteLocal(self) -> None:
        self.signalOnVolumeMutedChange.emit()

    def _signalSetVolumeLocal(self) -> None:
        self.signalOnVolumeLevelChange.emit(self.view.sliderVolumeLocal.value()/100)
