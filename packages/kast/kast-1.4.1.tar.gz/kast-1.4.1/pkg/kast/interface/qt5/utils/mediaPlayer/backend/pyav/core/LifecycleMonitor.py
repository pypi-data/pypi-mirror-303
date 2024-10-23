#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from threading import Event

from kast.interface.qt5.utils.mediaPlayer.backend.common.core.MediaDetails import MediaDetails
from kast.interface.qt5.utils.mediaPlayer.MediaPlayerState import MediaPlayerState
from kast.interface.qt5.utils.mediaPlayer.backend.pyav.core.PlayerStoppedException import PlayerStoppedException


class LifecycleMonitor:

    def __init__(self, shutdownEvent: Event, mediaDetails: MediaDetails) -> None:
        self._shutdownEvent: Event = shutdownEvent
        self._mediaDetails: MediaDetails = mediaDetails

    def shouldPlay(self) -> bool:
        return self._mediaDetails.state is not MediaPlayerState.Stopped

    def shouldStop(self) -> bool:
        return self._shutdownEvent.is_set() or self._mediaDetails.state in [
            MediaPlayerState.Stopped,
            MediaPlayerState.Seeking,
        ]

    def verifyNotStopped(self) -> None:
        if self.shouldStop():
            raise PlayerStoppedException()
