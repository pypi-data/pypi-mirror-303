#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from dataclasses import dataclass


@dataclass(frozen=True)
class DeviceInfo:
    name: str = ''
    model: str = ''
    manufacturer: str = ''
