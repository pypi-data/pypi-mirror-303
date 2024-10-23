#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from typing import TypeVar, cast

_T = TypeVar('_T')


def castNotNull(value: _T | None) -> _T:
    return cast(_T, value)
