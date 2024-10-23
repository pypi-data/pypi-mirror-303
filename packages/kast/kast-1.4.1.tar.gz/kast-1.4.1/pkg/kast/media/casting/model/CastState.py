#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from dataclasses import dataclass, field

from kast.media.casting.model.CastAppInfo import CastAppInfo
from kast.media.casting.model.CastCapabilities import CastCapabilities
from kast.media.casting.model.CastConnectionState import CastConnectionState
from kast.media.casting.model.CastMediaState import CastMediaState
from kast.media.casting.model.DeviceInfo import DeviceInfo


@dataclass(frozen=True)
class CastState:
    connection: CastConnectionState = CastConnectionState.Disconnected
    deviceInfo: DeviceInfo = field(default_factory=lambda: DeviceInfo())
    appInfo: CastAppInfo = field(default_factory=lambda: CastAppInfo())
    capabilities: CastCapabilities = field(default_factory=lambda: CastCapabilities())
    mediaState: CastMediaState = field(default_factory=lambda: CastMediaState())
