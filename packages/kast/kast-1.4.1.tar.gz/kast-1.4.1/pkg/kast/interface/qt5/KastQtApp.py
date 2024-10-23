#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import inspect
import sys

from PyQt5.Qt import PYQT_VERSION_STR, QT_VERSION_STR
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from kast.Services import Services
from kast.interface.qt5.UiServices import UiServices
from kast.interface.qt5.utils.QtHelper import QtHelper
from kast.interface.qt5.viewModel.MainWindowViewModel import MainWindowViewModel
from kast.utils.OsInfo import OsInfo, OsName
from kast.utils.log.Loggable import Loggable


class KastQtApp(Loggable):

    def __init__(self, services: Services) -> None:
        self._app = QApplication(sys.argv)
        self._uiServices = UiServices(services=services, onBackgroundError=self._onBackgroundError)

        self._app.setWindowIcon(QIcon(str(services.appInfo.appIconPath)))
        if OsInfo.name == OsName.Linux:
            self._app.setDesktopFileName(self._uiServices.services.appInfo.desktopFileName)

        self._mainWindowViewModel = MainWindowViewModel(uiServices=self._uiServices)

        QTimer.singleShot(0, self._onStartup)
        self._app.aboutToQuit.connect(self._onShutdown)

    def run(self) -> int:
        self.log.info(f"PyQt: {PYQT_VERSION_STR}, Qt: {QT_VERSION_STR}")
        self.log.info(f"Qt platform plugin: {QtHelper.getApp().platformName()}")
        return self._app.exec()

    def exit(self, returnCode: int = 0) -> None:
        self._app.closeAllWindows()
        self._app.exit(returnCode)

    def _onStartup(self) -> None:
        self.log.info("User interface startup...")
        self._uiServices.backgroundScheduler.start()
        self._uiServices.appLifecycleService.notifyStartup()
        self.log.info("User interface startup success!")

    def _onShutdown(self) -> None:
        self.log.info("User interface shutdown...")
        self._uiServices.appLifecycleService.notifyShutdown()
        self._uiServices.backgroundScheduler.stop()
        self.log.info("User interface shutdown success!")

    def _onBackgroundError(self, ex: Exception) -> None:
        self.log.critical(f"Unhandled error in background task! Exception: {ex}", exc_info=True)
        message = inspect.cleandoc("""
            Application encountered a CRITICAL error!
            (Shutting down due to high severity.)
            """)
        self._uiServices.dialogService.critical(
            message=message,
            onClose=lambda: self._app.exit(1)
        )
