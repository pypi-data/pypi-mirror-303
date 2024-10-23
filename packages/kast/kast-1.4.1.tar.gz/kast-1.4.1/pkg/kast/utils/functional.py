#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from collections.abc import Callable
from typing import TypeVar

_T = TypeVar('_T')
_R = TypeVar('_R')

ErrorHandler = Callable[[Exception], None]
Mapper = Callable[[_T], _R]
Predicate = Callable[[_T], bool]
Consumer = Callable[[_T], None]
Supplier = Callable[[], _T]
Runnable = Callable[[], None]
