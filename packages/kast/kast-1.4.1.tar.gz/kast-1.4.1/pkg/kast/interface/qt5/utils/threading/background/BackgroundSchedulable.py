#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from collections.abc import Callable
from typing import Any

from kast.interface.qt5.utils.threading.AbstractSchedulable import AbstractSchedulable, NonSchedulableException
from kast.interface.qt5.utils.threading.background.BackgroundThreadContext import BackgroundThreadContext


class BackgroundSchedulable(AbstractSchedulable):

    def __init__(self, backgroundThreadContext: BackgroundThreadContext) -> None:
        self.__backgroundThreadContext: BackgroundThreadContext = backgroundThreadContext

    def _onBackgroundException(self, ex: Exception) -> None:
        raise ex

    @classmethod
    def backgroundTask(
        cls,
        funcOpt: Callable | None = None,
        *,
        forceSchedule: bool = False
    ) -> Callable:
        def decoratorProvider(schedulable: BackgroundSchedulable) -> Callable:
            return schedulable.__backgroundThreadContext.backgroundTask(
                forceSchedule=forceSchedule,
                errorHandler=schedulable._onBackgroundException
            )

        return cls._taskDecorator(funcOpt=funcOpt, decoratorProvider=decoratorProvider)

    @staticmethod
    def _verifySchedulable(obj: Any) -> None:
        if not isinstance(obj, BackgroundSchedulable):
            raise NonSchedulableException(f"Object of type '{obj.__class__.__name__}' does not derive from '{BackgroundSchedulable.__name__}'!")
