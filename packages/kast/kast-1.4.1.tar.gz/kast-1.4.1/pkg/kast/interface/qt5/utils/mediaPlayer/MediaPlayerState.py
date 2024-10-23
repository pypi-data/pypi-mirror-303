#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from enum import Enum, auto


class MediaPlayerState(Enum):
    Buffering = auto()
    Seeking = auto()
    Playing = auto()
    Paused = auto()
    Stopped = auto()
