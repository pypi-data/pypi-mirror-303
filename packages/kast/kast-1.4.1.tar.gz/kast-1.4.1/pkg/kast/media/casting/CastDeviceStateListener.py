#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import pychromecast
from pychromecast.controllers.media import MEDIA_PLAYER_ERROR_CODES, MediaStatus, MediaStatusListener
from pychromecast.controllers.receiver import CastStatus, CastStatusListener, LaunchErrorListener, LaunchFailure
from pychromecast.socket_client import ConnectionStatus, ConnectionStatusListener

from kast.media.casting.CastStateUpdater import CastStateUpdater
from kast.media.casting.model.CastState import CastState
from kast.media.casting.model.DeviceInfo import DeviceInfo
from kast.utils.functional import Consumer
from kast.utils.log.Loggable import Loggable

CastStateChangeCallback = Consumer[CastState]


class _DeviceListener(
    MediaStatusListener,
    CastStatusListener,
    ConnectionStatusListener,
    LaunchErrorListener,
    Loggable
):
    def __init__(
        self,
        device: pychromecast.Chromecast,
        updateCallback: CastStateChangeCallback
    ) -> None:
        self._updateCallback: CastStateChangeCallback = updateCallback
        self._castState: CastState = CastState(deviceInfo=DeviceInfo(
            name=device.name,
            model=device.cast_info.model_name,
            manufacturer=device.cast_info.manufacturer
        ))

        device.register_launch_error_listener(self)
        device.register_status_listener(self)
        device.media_controller.register_status_listener(self)
        device.socket_client.register_connection_listener(self)

    def new_media_status(self, status: MediaStatus) -> None:
        self._castState = CastStateUpdater.updateOnMediaEvent(
            currentState=self._castState,
            event=status
        )
        self._updateCallback(self._castState)

    def new_cast_status(self, status: CastStatus) -> None:
        self._castState = CastStateUpdater.updateOnCastEvent(
            currentState=self._castState,
            event=status
        )
        self._updateCallback(self._castState)

    def new_connection_status(self, status: ConnectionStatus) -> None:
        self._castState = CastStateUpdater.updateOnConnectionEvent(
            currentState=self._castState,
            event=status
        )
        self._updateCallback(self._castState)

    def load_media_failed(self, item: int, error_code: int) -> None:
        errorName = MEDIA_PLAYER_ERROR_CODES.get(error_code, 'UNKNOWN')
        self.log.error(f"Media load failure! error='{errorName}({error_code})'")  # TODO: Handle!

    def new_launch_error(self, status: LaunchFailure) -> None:
        self.log.error(f"Launch failure! Details: '{status}'")  # TODO: Handle!


class CastDeviceStateListener:  # TODO: Provide multiple subscribers support!

    def __init__(self) -> None:
        self._deviceListener: _DeviceListener | None = None
        self._updateCallback: CastStateChangeCallback | None = None

    def register(
        self,
        device: pychromecast.Chromecast,
        updateCallback: CastStateChangeCallback
    ) -> None:
        self._updateCallback = updateCallback
        self._deviceListener = _DeviceListener(
            device=device,
            updateCallback=self._onUpdate
        )

    def unregister(self) -> None:
        self._deviceListener = None
        self._updateCallback = None

    def _onUpdate(self, event: CastState) -> None:
        if self._updateCallback is not None:
            self._updateCallback(event)
