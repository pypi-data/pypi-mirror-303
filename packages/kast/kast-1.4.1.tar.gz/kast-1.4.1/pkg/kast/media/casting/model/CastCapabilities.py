#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from dataclasses import dataclass


@dataclass(frozen=True)
class CastCapabilities:
    canPause: bool = False
    canSeek: bool = False
    canSetMute: bool = False
    canSetVolume: bool = False
    canSkipForward: bool = False
    canSkipBackward: bool = False
    canQueueNext: bool = False
    canQueuePrevious: bool = False
