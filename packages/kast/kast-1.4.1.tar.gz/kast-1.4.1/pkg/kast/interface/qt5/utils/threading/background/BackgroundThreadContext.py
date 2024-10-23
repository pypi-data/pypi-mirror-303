#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from collections.abc import Callable
from functools import wraps
from typing import Any, cast

from kast.interface.qt5.utils.QtHelper import QtHelper
from kast.utils.functional import ErrorHandler
from kast.utils.threading.Scheduler import Scheduler


class BackgroundThreadContext:

    def __init__(self, backgroundScheduler: Scheduler) -> None:
        self._backgroundScheduler: Scheduler = backgroundScheduler

    def backgroundTask(
        self,
        funcOpt: Callable | None = None,
        *,
        forceSchedule: bool = False,
        errorHandler: ErrorHandler | None = None
    ) -> Callable:
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> None:
                def callback() -> None:
                    try:
                        func(*args, **kwargs)

                    except Exception as ex:
                        if errorHandler is None:
                            raise ex
                        errorHandler(ex)

                if not forceSchedule and not QtHelper.isMainThread():
                    callback()
                    return

                self._backgroundScheduler.schedule(callback)

            return wrapper

        decoratedFunction = decorator if funcOpt is None \
            else decorator(funcOpt)
        return cast(Callable, decoratedFunction)
