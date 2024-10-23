#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import time
from abc import ABC

from tunit.unit import Milliseconds, Seconds

from kast.interface.qt5.utils.mediaPlayer.backend.pyav.Frame import Frame
from kast.interface.qt5.utils.mediaPlayer.backend.common.utils.FrameDropTracker import FrameDropTracker
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.workers.IWorker import IWorker
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.core.LifecycleMonitor import LifecycleMonitor
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.core.MPConstant import MPConstant
from kast.interface.qt5.utils.mediaPlayer.backend.common.core.MediaDetails import MediaDetails
from kast.utils.log.Loggable import Loggable


class FrameHandlingWorkerBase(IWorker, Loggable, ABC):

    DELAY_THRESHOLD = Milliseconds(500)

    def __init__(
        self,
        mediaDetails: MediaDetails,
        lifecycleMonitor: LifecycleMonitor,
        frameDropTracker: FrameDropTracker
    ) -> None:
        self._mediaDetails = mediaDetails
        self._lifecycleMonitor: LifecycleMonitor = lifecycleMonitor
        self._frameDropTracker = frameDropTracker

    def _shouldPlayFrame(self, frame: Frame, offset: Milliseconds = Milliseconds()) -> bool:
        def position() -> Milliseconds:
            return self._mediaDetails.position + offset

        while position() < frame.timePos:
            self._lifecycleMonitor.verifyNotStopped()
            time.sleep(MPConstant.SLEEP_TO_COOL_DOWN.toRawUnit(unit=Seconds))

        delay = position() - frame.timePos
        if delay >= self.DELAY_THRESHOLD:
            self._frameDropTracker.increment(currentDelay=delay)
            return False

        self._frameDropTracker.clear()
        return True
