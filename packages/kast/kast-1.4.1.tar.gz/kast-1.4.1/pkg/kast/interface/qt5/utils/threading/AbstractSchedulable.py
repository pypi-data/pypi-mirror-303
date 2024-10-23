#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from abc import ABC, abstractmethod
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar, cast


class NonSchedulableException(Exception):
    pass


class ISchedulable(ABC):
    @staticmethod
    @abstractmethod
    def _verifySchedulable(obj: Any) -> None: ...


T = TypeVar('T', bound=ISchedulable)

DecoratorProvider = Callable[[T], Callable]


class AbstractSchedulable(ISchedulable, ABC):

    @classmethod
    def _taskDecorator(
        cls,
        funcOpt: Callable | None,
        *,
        decoratorProvider: DecoratorProvider
    ) -> Callable:
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(obj: Any, *args: Any, **kwargs: Any) -> None:
                cls._verifySchedulable(obj)

                @decoratorProvider(obj)
                def callback() -> None:
                    func(obj, *args, **kwargs)

                callback()

            return wrapper

        decoratedFunction = decorator if funcOpt is None \
            else decorator(funcOpt)
        return cast(Callable, decoratedFunction)
