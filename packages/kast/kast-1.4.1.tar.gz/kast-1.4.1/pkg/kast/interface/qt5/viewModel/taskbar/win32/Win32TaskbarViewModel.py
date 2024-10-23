#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import math
from dataclasses import dataclass

from PyQt5.QtWidgets import QMainWindow, QStyle, QWidget
from PyQt5.QtWinExtras import QWinTaskbarButton, QWinThumbnailToolBar, QWinThumbnailToolButton

from kast.interface.qt5.UiServices import UiServices
from kast.interface.qt5.service.UiEvent import UiEvent, UiState
from kast.interface.qt5.viewModel.taskbar.common.TaskbarViewModelBase import TaskbarViewModelBase


@dataclass
class _PercentageInfo:
    vCur: int
    vMax: int
    vMin: int


class Win32TaskbarViewModel(TaskbarViewModelBase):

    def __init__(
        self,
        parent: QMainWindow,
        uiServices: UiServices
    ) -> None:
        super().__init__(parent, uiServices)
        self.uiServices.uiEventObserver.register(self, self._onUiEvent)

        self._mediaControls: list[QWidget] = []
        mediaControls = self._mediaControls

        self._taskbarToolbar = taskbarToolbar = QWinThumbnailToolBar(parent)
        taskbarToolbar.setWindow(parent.windowHandle())

        self._taskbarButtonPlayOrPause = buttonPlayOrPause = QWinThumbnailToolButton(taskbarToolbar)
        buttonPlayOrPause.setToolTip('Play/Pause')
        buttonPlayOrPause.setIcon(parent.style().standardIcon(QStyle.SP_MediaPlay))
        mediaControls.append(buttonPlayOrPause)

        self._taskbarButtonStop = buttonStop = QWinThumbnailToolButton(taskbarToolbar)
        buttonStop.setToolTip('Stop')
        buttonStop.setIcon(parent.style().standardIcon(QStyle.SP_MediaStop))
        mediaControls.append(buttonStop)

        self._taskbarButtonSeekForward = buttonSeekForward = QWinThumbnailToolButton(taskbarToolbar)
        buttonSeekForward.setToolTip('Seek forward')
        buttonSeekForward.setIcon(parent.style().standardIcon(QStyle.SP_MediaSeekForward))
        mediaControls.append(buttonSeekForward)

        self._taskbarButtonSeekBackward = buttonSeekBackward = QWinThumbnailToolButton(taskbarToolbar)
        buttonSeekBackward.setToolTip('Seek backward')
        buttonSeekBackward.setIcon(parent.style().standardIcon(QStyle.SP_MediaSeekBackward))
        mediaControls.append(buttonSeekBackward)

        self._taskbarIcon = taskbarIcon = QWinTaskbarButton(parent)
        taskbarIcon.setWindow(parent.windowHandle())
        self._taskbarProgress = taskbarIcon.progress()

        taskbarToolbar.addButton(buttonSeekBackward)
        taskbarToolbar.addButton(buttonPlayOrPause)
        taskbarToolbar.addButton(buttonStop)
        taskbarToolbar.addButton(buttonSeekForward)

        self._enableControls(False)

        buttonPlayOrPause.clicked.connect(self._signalButtonPlayOrPause)
        buttonStop.clicked.connect(self._signalButtonStop)
        buttonSeekForward.clicked.connect(self._signalButtonSeekForward)
        buttonSeekBackward.clicked.connect(self._signalButtonSeekBackward)

    def _onUiEvent(self, uiEvent: UiEvent) -> None:
        isStreaming = uiEvent.state == UiState.Streaming
        self._enableControls(isStreaming)

        iconPlayPause = QStyle.SP_MediaPause if self._mediaState.playerState.isPlaying() else QStyle.SP_MediaPlay
        self._taskbarButtonPlayOrPause.setIcon(self._parent.style().standardIcon(iconPlayPause))

        self._updateProgress(uiEvent)

    def _signalButtonPlayOrPause(self) -> None:
        self.uiServices.mediaControlService.playOrPause()

    def _signalButtonStop(self) -> None:
        self.uiServices.mediaControlService.stop()

    def _signalButtonSeekForward(self) -> None:
        self.uiServices.mediaControlService.seekForward()

    def _signalButtonSeekBackward(self) -> None:
        self.uiServices.mediaControlService.seekBackward()

    def _enableControls(self, enable: bool = True) -> None:
        for control in self._mediaControls:
            control.setEnabled(enable)

    def _displayProgress(self, display: bool, percentage: float = 0.0) -> None:
        if display:
            percentageInfo = self._convertPercentage(percentage=percentage)
            self._taskbarProgress.setRange(percentageInfo.vMin, percentageInfo.vMax)
            self._taskbarProgress.setValue(percentageInfo.vCur)

        self._taskbarProgress.setVisible(display)

    @staticmethod
    def _convertPercentage(percentage: float) -> _PercentageInfo:
        return _PercentageInfo(
            vCur=math.ceil(percentage * 100) if percentage > 0.0 else 0,
            vMax=100 if percentage > 0.0 else 0,
            vMin=0
        )
