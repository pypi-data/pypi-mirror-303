#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import threading
import time
from threading import Event, Thread

from tunit.unit import Milliseconds, Seconds

from kast.utils.FifoBuffer import FifoBuffer
from kast.utils.Maybe import Maybe
from kast.utils.functional import ErrorHandler
from kast.utils.log.Loggable import Loggable
from kast.utils.threading.Task import Task


class Executor(Loggable):

    _SLEEP_ON_WAITING: Milliseconds = Milliseconds(500)
    _SLEEP_ON_COOLDOWN: Milliseconds = Milliseconds(20)

    def __init__(
        self,
        executorId: str,
        fifoBuffer: FifoBuffer[Task],
        errorHandler: ErrorHandler | None = None
    ) -> None:
        self._executorId: str = executorId
        self._fifoBuffer: FifoBuffer[Task] = fifoBuffer
        self._errorHandler: ErrorHandler | None = errorHandler

        self._stopEvent: Event = Event()
        self._thread: Thread | None = None

    def start(self) -> None:
        if self._thread is not None:
            return

        thread = Thread(
            target=self._run,
            name=f"{self.__class__.__name__}({self._executorId})",
            daemon=True
        )
        self._stopEvent.clear()
        thread.start()
        self._thread = thread

    def stop(self) -> None:
        if self._thread is None:
            return

        self._stopEvent.set()
        self._thread.join()
        self._thread = None

    def _run(self) -> None:
        self.log.info(f"{threading.current_thread().name} started.")
        try:
            self._loop()
        finally:
            self.log.info(f"{threading.current_thread().name} stopped.")

    def _loop(self) -> None:
        while not self._stopEvent.wait(timeout=self._SLEEP_ON_COOLDOWN.toRawUnit(Seconds)):
            try:
                Maybe(self._fifoBuffer.tryGet(timeout=self._SLEEP_ON_WAITING)).ifPresent(self._executeTask)
            except Exception as ex:
                self._onError(ex=ex)

    def _executeTask(self, task: Task) -> None:
        if float(task.scheduledTimestamp) > time.time():
            self._fifoBuffer.tryPut(item=task)
            return

        task.runnable()

    def _onError(self, ex: Exception) -> None:
        try:
            Maybe(self._errorHandler).ifPresent(lambda errorHandler: errorHandler(ex))
        except Exception:
            self.log.critical(f"{threading.current_thread().name} caught exception in error handler!", exc_info=True)
