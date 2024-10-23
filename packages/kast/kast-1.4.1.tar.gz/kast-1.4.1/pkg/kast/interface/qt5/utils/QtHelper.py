#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from typing import Any, cast

from PyQt5.QtCore import QThread, pyqtBoundSignal, pyqtSignal
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QApplication

from kast.interface.qt5.utils.QtException import QtException


class QtHelper:

    @staticmethod
    def getApp() -> QGuiApplication:
        app = QApplication.instance()
        if app is None:
            raise QtException("Qt app is null!")
        if not isinstance(app, QGuiApplication):
            raise QtException("Qt app does not support GUI!")
        return app

    @staticmethod
    def declareSignal(*args: Any, **kwargs: Any) -> pyqtBoundSignal:
        return cast(pyqtBoundSignal, pyqtSignal(*args, **kwargs))

    @classmethod
    def isMainThread(cls) -> bool:
        return QThread.currentThread() == cls.getApp().thread()
