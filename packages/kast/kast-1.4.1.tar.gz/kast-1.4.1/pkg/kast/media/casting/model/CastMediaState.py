#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from dataclasses import dataclass, field

from tunit.unit import Milliseconds

from kast.media.casting.model.CastPlayerState import CastPlayerState
from kast.utils.timeUtils import getTimestampMsNow

VolumeLevel = float


@dataclass(frozen=True)
class CastMediaState:
    volumeMuted: bool = False
    volumeLevel: VolumeLevel = 1.0

    title: str = ''
    displayName: str = ''
    iconUrl: str = ''
    imageUrl: str = ''
    contentUrl: str = ''

    playerState: CastPlayerState = CastPlayerState.Unknown
    duration: Milliseconds = Milliseconds()
    lastUpdatePosition: Milliseconds = Milliseconds()
    lastUpdateTimestamp: Milliseconds = field(default_factory=lambda: getTimestampMsNow())

    @property
    def currentPosition(self) -> Milliseconds:
        offset = Milliseconds() if self.playerState != CastPlayerState.Playing\
            else getTimestampMsNow() - self.lastUpdateTimestamp
        return self.lastUpdatePosition + offset
