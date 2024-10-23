#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import platform
from enum import Enum


class OsName(Enum):
    Unknown = 'Unknown'
    Linux = 'Linux'
    Windows = 'Windows'
    Darwin = 'Darwin'


def _findOsName() -> OsName:
    try:
        return OsName(platform.system())
    except ValueError:
        return OsName.Unknown


class OsInfo:
    name: OsName = _findOsName()
