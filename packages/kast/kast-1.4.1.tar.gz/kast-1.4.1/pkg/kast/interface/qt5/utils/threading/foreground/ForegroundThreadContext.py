#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from collections.abc import Callable
from functools import wraps
from typing import Any, cast

from kast.interface.qt5.utils.threading.foreground.ForegroundScheduler import ForegroundScheduler
from kast.interface.qt5.utils.QtHelper import QtHelper


class ForegroundThreadContext:

    def __init__(self, foregroundScheduler: ForegroundScheduler) -> None:
        self._foregroundScheduler: ForegroundScheduler = foregroundScheduler

    def foregroundTask(
        self,
        funcOpt: Callable | None = None,
        *,
        forceSchedule: bool = False
    ) -> Callable:
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> None:
                def callback() -> None:
                    func(*args, **kwargs)

                if not forceSchedule and QtHelper.isMainThread():
                    callback()
                    return

                self._foregroundScheduler.schedule(callback)

            return wrapper

        decoratedFunction = decorator if funcOpt is None \
            else decorator(funcOpt)
        return cast(Callable, decoratedFunction)
