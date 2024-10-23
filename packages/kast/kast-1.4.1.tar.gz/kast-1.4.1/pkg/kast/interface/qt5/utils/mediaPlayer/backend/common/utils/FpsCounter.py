#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from PyQt5.QtCore import QObject, pyqtBoundSignal
from tunit.unit import Seconds

from kast.interface.qt5.utils.QtHelper import QtHelper
from kast.utils.StopWatch import StopWatch


class FpsCounter(QObject):

    signalFps: pyqtBoundSignal = QtHelper.declareSignal(int)

    def __init__(self) -> None:
        super().__init__()
        self._stopWatch = StopWatch()
        self._fpsCounter: int = 0
        self._fpsCurrent: int = 0

    @property
    def fps(self) -> int:
        return self._fpsCurrent

    def reset(self) -> None:
        self._reset()

    def tick(self) -> None:
        if self._stopWatch.elapsed >= Seconds(1):
            self._reset(value=self._fpsCounter)
            self.signalFps.emit(self._fpsCurrent)

        self._stopWatch.start()
        self._fpsCounter += 1

    def _reset(self, value: int = 0) -> None:
        self._stopWatch.stop()
        self._fpsCounter = 0
        self._fpsCurrent = value
