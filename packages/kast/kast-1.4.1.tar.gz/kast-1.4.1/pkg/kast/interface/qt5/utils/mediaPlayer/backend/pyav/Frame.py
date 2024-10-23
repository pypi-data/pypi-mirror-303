#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from dataclasses import dataclass

from PyQt5.QtMultimedia import QVideoFrame
from numpy.typing import NDArray
from tunit.unit import Milliseconds


@dataclass
class VideoFrame:
    timePos: Milliseconds
    frame: QVideoFrame


@dataclass
class AudioFrame:
    timePos: Milliseconds
    data: NDArray


Frame = VideoFrame | AudioFrame
