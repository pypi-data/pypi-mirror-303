#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from __future__ import annotations  # TODO: Remove when support dropped for: Python < ?

import logging
from typing import Any


class _LoggerProvider:
    def __get__(
        self,
        instance: Any,
        owner: type[Any]
    ) -> logging.Logger:
        logFormat = f"{owner.__name__}:({hex(id(self))})"
        return logging.getLogger(logFormat)


class Loggable:
    log: _LoggerProvider | logging.Logger = _LoggerProvider()
