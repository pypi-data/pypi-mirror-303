#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from collections.abc import Callable

from PyQt5.QtWidgets import QMessageBox

from kast.interface.qt5.utils.dialog.DialogQuestion import DialogQuestion
from kast.interface.qt5.utils.threading.Schedulable import Schedulable
from kast.interface.qt5.utils.threading.foreground.ForegroundSchedulable import ForegroundSchedulable
from kast.interface.qt5.utils.threading.foreground.ForegroundThreadContext import ForegroundThreadContext
from kast.utils.functional import Runnable

DialogResultCallback = Callable[[bool], None]


class DialogService(ForegroundSchedulable):

    TITLE_CRITICAL = 'Critical'
    TITLE_ERROR = 'Error'
    TITLE_WARNING = 'Warning'

    def __init__(self, foregroundThreadContext: ForegroundThreadContext) -> None:
        super().__init__(foregroundThreadContext=foregroundThreadContext)

    @Schedulable.foregroundTask
    def warning(
        self,
        message: str,
        onClose: Runnable = lambda: None
    ) -> None:
        self._dialogInformation(
            title=DialogService.TITLE_WARNING,
            message=message,
            icon=QMessageBox.Warning
        )
        onClose()

    @Schedulable.foregroundTask
    def error(
        self,
        message: str,
        onClose: Runnable = lambda: None
    ) -> None:
        self._dialogInformation(
            title=DialogService.TITLE_ERROR,
            message=message,
            icon=QMessageBox.Critical
        )
        onClose()

    @Schedulable.foregroundTask
    def critical(
        self,
        message: str,
        onClose: Runnable = lambda: None
    ) -> None:
        self._dialogInformation(
            title=DialogService.TITLE_CRITICAL,
            message=message,
            icon=QMessageBox.Critical
        )
        onClose()

    @Schedulable.foregroundTask
    def questionOkCancel(
        self,
        title: str,
        message: str,
        default: bool = False,
        onResult: DialogResultCallback = lambda result: None
    ) -> None:
        onResult(DialogQuestion(
            title=title,
            message=message,
            default=default
        ).display())

    @Schedulable.foregroundTask
    def questionYesNo(
        self,
        title: str,
        message: str,
        default: bool = False,
        onResult: DialogResultCallback = lambda result: None
    ) -> None:
        onResult(DialogQuestion(
            title=title,
            message=message,
            default=default,
            positiveButton=QMessageBox.Yes,
            negativeButton=QMessageBox.No
        ).display())

    def _dialogInformation(self, title: str, message: str, icon: QMessageBox.Icon = QMessageBox.Information) -> None:
        msgBox = QMessageBox()
        msgBox.setIcon(icon)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.exec()
