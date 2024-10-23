#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from typing import Any, cast

from PyQt5.QtDBus import QDBusConnection, QDBusMessage
from PyQt5.QtWidgets import QMainWindow

from kast.interface.qt5.UiServices import UiServices
from kast.interface.qt5.service.UiEvent import UiEvent
from kast.interface.qt5.viewModel.taskbar.common.TaskbarViewModelBase import TaskbarViewModelBase


class UnityTaskbarViewModel(TaskbarViewModelBase):

    def __init__(self, parent: QMainWindow, uiServices: UiServices) -> None:
        super().__init__(parent, uiServices)
        self.uiServices.uiEventObserver.register(self, self._onUiEvent)

        self._displayProgress(False)

    def _onUiEvent(self, uiEvent: UiEvent) -> None:
        self._updateProgress(uiEvent)

    def _displayProgress(self, display: bool, percentage: float = 0.0) -> None:
        self._sendMessage({
            'progress': percentage,
            'progress-visible': display
        })

    def _sendMessage(self, parameters: dict) -> None:
        message: QDBusMessage = QDBusMessage.createSignal('/', 'com.canonical.Unity.LauncherEntry', 'Update')
        message << cast(Any, f'application://{self.services.appInfo.desktopFileName}')
        message << cast(Any, parameters)
        QDBusConnection.sessionBus().send(message)
