#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from kast.interface.qt5.utils.threading.ThreadContext import ThreadContext
from kast.interface.qt5.utils.threading.background.BackgroundSchedulable import BackgroundSchedulable
from kast.interface.qt5.utils.threading.foreground.ForegroundSchedulable import ForegroundSchedulable


class Schedulable(ForegroundSchedulable, BackgroundSchedulable):

    def __init__(self, threadContext: ThreadContext) -> None:
        ForegroundSchedulable.__init__(self, foregroundThreadContext=threadContext)
        BackgroundSchedulable.__init__(self, backgroundThreadContext=threadContext)
