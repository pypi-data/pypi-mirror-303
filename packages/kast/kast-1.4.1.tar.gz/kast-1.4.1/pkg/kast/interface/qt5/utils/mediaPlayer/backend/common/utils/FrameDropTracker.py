#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from tunit.unit import Milliseconds

from kast.utils.log.Loggable import Loggable


class FrameDropTracker(Loggable):

    _LOG_THRESHOLD_STEP = 100

    def __init__(self, frameTypeName: str) -> None:
        self._frameTypeName = frameTypeName
        self._counter: int = 0
        self._logThreshold: int = self._LOG_THRESHOLD_STEP
        self._averageDelay: Milliseconds | None = None

    def increment(self, currentDelay: Milliseconds) -> None:
        self._counter += 1
        self._averageDelay = self._calcAverageDelay(newDelay=currentDelay)

        if self._counter == 1:
            self.log.info(f"{self._frameTypeName} frames dropping started.")

        if self._counter >= self._logThreshold:
            self._logDroppedFrameCount()
            self._logThreshold += self._LOG_THRESHOLD_STEP

    def clear(self) -> None:
        if self._counter > 0:
            self._logDroppedFrameCount()
            self.log.info(f"{self._frameTypeName} frames are being played again.")

            self._counter = 0
            self._logThreshold = self._LOG_THRESHOLD_STEP
            self._averageDelay = None

    def _calcAverageDelay(self, newDelay: Milliseconds) -> Milliseconds:
        if self._averageDelay is None:
            return newDelay
        return (self._averageDelay + newDelay)/2

    def _getAverageDelayMessage(self) -> str:
        if self._averageDelay is None:
            return ''
        return f" (Average delay: {self._averageDelay})"

    def _logDroppedFrameCount(self) -> None:
        self.log.info(f"{self._frameTypeName} frames dropped since last played: {self._counter}" + self._getAverageDelayMessage())
