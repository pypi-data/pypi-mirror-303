#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from collections.abc import Callable
from typing import Any

from kast.interface.qt5.utils.threading.AbstractSchedulable import AbstractSchedulable, NonSchedulableException
from kast.interface.qt5.utils.threading.foreground.ForegroundThreadContext import ForegroundThreadContext


class ForegroundSchedulable(AbstractSchedulable):

    def __init__(self, foregroundThreadContext: ForegroundThreadContext) -> None:
        self.__foregroundThreadContext: ForegroundThreadContext = foregroundThreadContext

    @classmethod
    def foregroundTask(
        cls,
        funcOpt: Callable | None = None,
        *,
        forceSchedule: bool = False
    ) -> Callable:
        def decoratorProvider(schedulable: ForegroundSchedulable) -> Callable:
            return schedulable.__foregroundThreadContext.foregroundTask(forceSchedule=forceSchedule)

        return cls._taskDecorator(funcOpt=funcOpt, decoratorProvider=decoratorProvider)

    @staticmethod
    def _verifySchedulable(obj: Any) -> None:
        if not isinstance(obj, ForegroundSchedulable):
            raise NonSchedulableException(f"Object of type '{obj.__class__.__name__}' does not derive from '{ForegroundSchedulable.__name__}'!")
