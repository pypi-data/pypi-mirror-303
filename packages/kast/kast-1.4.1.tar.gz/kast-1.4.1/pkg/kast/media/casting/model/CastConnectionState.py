#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from enum import Enum

from pychromecast.socket_client import CONNECTION_STATUS_CONNECTED, CONNECTION_STATUS_CONNECTING, \
    CONNECTION_STATUS_DISCONNECTED, CONNECTION_STATUS_FAILED, CONNECTION_STATUS_FAILED_RESOLVE, CONNECTION_STATUS_LOST


class CastConnectionState(Enum):
    Connecting = CONNECTION_STATUS_CONNECTING
    Connected = CONNECTION_STATUS_CONNECTED
    Disconnected = CONNECTION_STATUS_DISCONNECTED
    Failed = CONNECTION_STATUS_FAILED
    FailedResolve = CONNECTION_STATUS_FAILED_RESOLVE
    Lost = CONNECTION_STATUS_LOST

    def isConnected(self) -> bool:
        return self in [
            CastConnectionState.Connected,
            CastConnectionState.Connecting
        ]

    def isConnectedOrRecoverable(self) -> bool:
        return self.isConnected() \
           or self == CastConnectionState.Lost
