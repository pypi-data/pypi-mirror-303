#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from kast.interface.qt5.utils.threading.background.BackgroundThreadContext import BackgroundThreadContext
from kast.interface.qt5.utils.threading.foreground.ForegroundScheduler import ForegroundScheduler
from kast.interface.qt5.utils.threading.foreground.ForegroundThreadContext import ForegroundThreadContext
from kast.utils.threading.Scheduler import Scheduler


class ThreadContext(ForegroundThreadContext, BackgroundThreadContext):

    def __init__(
        self,
        foregroundScheduler: ForegroundScheduler,
        backgroundScheduler: Scheduler
    ) -> None:
        ForegroundThreadContext.__init__(self, foregroundScheduler=foregroundScheduler)
        BackgroundThreadContext.__init__(self, backgroundScheduler=backgroundScheduler)
