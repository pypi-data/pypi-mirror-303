#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from threading import Event

from tunit.unit import Milliseconds, Seconds

from kast.utils.functional import Runnable
from kast.utils.threading.Scheduler import Scheduler


class PeriodicRunner:

    def __init__(
        self,
        scheduler: Scheduler,
        interval: Seconds,
        runnable: Runnable
    ) -> None:
        self._scheduler: Scheduler = scheduler
        self._interval: Seconds = interval
        self._runnable: Runnable = runnable

        self._stopEvent: Event = Event()
        self._stopEvent.set()

    def start(self) -> None:
        if not self._stopEvent.is_set():
            return

        self._stopEvent.clear()
        self._schedule()

    def stop(self) -> None:
        self._stopEvent.set()

    def _execute(self) -> None:
        if self._stopEvent.is_set():
            return

        self._schedule()
        self._runnable()

    def _schedule(self) -> None:
        self._scheduler.schedule(
            runnable=self._execute,
            delay=Milliseconds(self._interval)
        )
