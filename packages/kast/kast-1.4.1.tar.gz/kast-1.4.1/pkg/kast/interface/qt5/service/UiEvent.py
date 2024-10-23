#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import threading
from dataclasses import dataclass
from enum import Enum


class UiState(Enum):
    Idle = 'Idle'
    DeviceSearch = 'Searching for cast devices'
    VideoProbe = 'Extracting video meta data'
    CastMediaFormatSelection = 'Media format selection'
    ConvertingSubtitles = 'Converting subtitles'
    ConvertingMedia = 'Transcoding/Remuxing'
    Connecting = 'Connecting'
    Streaming = 'Streaming'


@dataclass
class Progress:
    complete: bool = True
    percentage: int | None = None
    cancelEvent: threading.Event | None = None


@dataclass
class UiEvent:
    state: UiState = UiState.Idle
    progress: Progress = Progress()
