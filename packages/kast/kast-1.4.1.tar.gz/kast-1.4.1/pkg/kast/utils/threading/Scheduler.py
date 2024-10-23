#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from abc import ABC
from collections.abc import Callable
from functools import wraps
from itertools import count
from typing import Any, cast

from tunit.unit import Milliseconds

from kast.utils.FifoBuffer import FifoBuffer
from kast.utils.functional import ErrorHandler, Runnable
from kast.utils.log.Loggable import Loggable
from kast.utils.threading.Executor import Executor
from kast.utils.threading.Task import Task
from kast.utils.timeUtils import getTimestampMsNow


class _IScheduler(Loggable, ABC):
    _schedulerId: str
    _executors: list[Executor]


def _logSchedulerLifecycle(
    startActionName: str,
    stopActionName: str
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(self: _IScheduler, *args: Any, **kwargs: Any) -> None:
            self.log.info(f"{self.__class__.__name__}({self._schedulerId}) {startActionName} ({len(self._executors)}) executors...")
            try:
                func(self, *args, **kwargs)
            finally:
                self.log.info(f"{self.__class__.__name__}({self._schedulerId}) {stopActionName}!")

        return wrapper

    return cast(Callable, decorator)


class Scheduler(_IScheduler):
    _idGenerator = count(0)

    def __init__(
        self,
        executorCount: int = 1,
        errorHandler: ErrorHandler | None = None
    ) -> None:
        self._schedulerId: str = f'sched-{next(self._idGenerator)}'
        self._fifoBuffer: FifoBuffer[Task] = FifoBuffer()
        self._executors: list[Executor] = [
            Executor(
                executorId=f'{self._schedulerId}/exec-{executorNumber}',
                fifoBuffer=self._fifoBuffer,
                errorHandler=errorHandler
            )
            for executorNumber in range(0, executorCount)
        ]

    def clear(self) -> None:
        self._fifoBuffer.clear()

    @_logSchedulerLifecycle(startActionName='starting', stopActionName='started')
    def start(self) -> None:
        for executor in self._executors:
            executor.start()

    @_logSchedulerLifecycle(startActionName='stopping', stopActionName='stopped')
    def stop(self) -> None:
        for executor in self._executors:
            executor.stop()

    def schedule(
        self,
        runnable: Runnable,
        delay: Milliseconds = Milliseconds()
    ) -> None:
        scheduledTimestamp = getTimestampMsNow() + delay if delay > 0 else delay
        task = Task(
            runnable=runnable,
            scheduledTimestamp=scheduledTimestamp
        )
        self._fifoBuffer.tryPut(item=task)
