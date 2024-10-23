#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from enum import Enum

from pychromecast.controllers.media import MEDIA_PLAYER_STATE_BUFFERING, MEDIA_PLAYER_STATE_IDLE, \
    MEDIA_PLAYER_STATE_PAUSED, \
    MEDIA_PLAYER_STATE_PLAYING, MEDIA_PLAYER_STATE_UNKNOWN


class CastPlayerState(Enum):
    Playing = MEDIA_PLAYER_STATE_PLAYING
    Buffering = MEDIA_PLAYER_STATE_BUFFERING
    Paused = MEDIA_PLAYER_STATE_PAUSED
    Idle = MEDIA_PLAYER_STATE_IDLE
    Unknown = MEDIA_PLAYER_STATE_UNKNOWN

    def isPlaying(self) -> bool:
        return self in [
            CastPlayerState.Playing,
            CastPlayerState.Buffering,
        ]

    def isPaused(self) -> bool:
        return self == CastPlayerState.Paused

    def isStopped(self) -> bool:
        return not self.isPlaying()\
            and not self.isPaused()
