#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from dataclasses import dataclass


@dataclass
class FpsReport:
    mediaFps: int | None = None
    backendFps: int | None = None
    frontendFps: int | None = None
