#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import dataclasses
from collections.abc import Callable
from typing import TypeVar

from pychromecast.controllers.media import MediaStatus
from pychromecast.controllers.receiver import CastStatus
from pychromecast.socket_client import ConnectionStatus
from tunit.unit import Milliseconds, Seconds

from kast.media.casting.model.CastCapabilities import CastCapabilities
from kast.media.casting.model.CastConnectionState import CastConnectionState
from kast.media.casting.model.CastMediaState import CastMediaState, CastPlayerState
from kast.media.casting.model.CastState import CastState
from kast.utils.timeUtils import getTimestampMsNow

_T = TypeVar('_T')
_V = TypeVar('_V')


class CastStateUpdater:

    @classmethod
    def updateOnConnectionEvent(cls, currentState: CastState, event: ConnectionStatus) -> CastState:
        newState = dataclasses.replace(
            currentState,
            connection=CastConnectionState(cls._nonNullUpdate(event.status, currentState.connection.value))
        )

        if not newState.connection.isConnectedOrRecoverable():
            return CastState(deviceInfo=newState.deviceInfo)

        return newState

    @classmethod
    def updateOnCastEvent(cls, currentState: CastState, event: CastStatus) -> CastState:
        newAppInfo = dataclasses.replace(
            currentState.appInfo,
            id=event.app_id,
            name=event.display_name,
        )
        newMediaState = dataclasses.replace(
            currentState.mediaState,
            volumeMuted=event.volume_muted,
            volumeLevel=event.volume_level,
            displayName=event.display_name,
            iconUrl=event.icon_url,
        )
        return dataclasses.replace(
            currentState,
            appInfo=newAppInfo,
            mediaState=newMediaState,
        )

    @classmethod
    def updateOnMediaEvent(cls, currentState: CastState, event: MediaStatus) -> CastState:
        isDefaultReceiver = currentState.appInfo.isDefaultReceiver()
        currentCapabilities = currentState.capabilities
        newCapabilities = dataclasses.replace(
            currentState.capabilities,
            canPause=isDefaultReceiver and cls._nonNullUpdate(event.supports_pause, currentCapabilities.canPause),
            canSeek=isDefaultReceiver and cls._nonNullUpdate(event.supports_seek, currentCapabilities.canSeek),
            canSetMute=isDefaultReceiver and cls._nonNullUpdate(event.supports_stream_mute, currentCapabilities.canSetMute),
            canSetVolume=isDefaultReceiver and cls._nonNullUpdate(event.supports_stream_volume, currentCapabilities.canSetVolume),
            canSkipForward=isDefaultReceiver and cls._nonNullUpdate(event.supports_skip_forward, currentCapabilities.canSkipForward),
            canSkipBackward=isDefaultReceiver and cls._nonNullUpdate(event.supports_skip_backward, currentCapabilities.canSkipBackward),
            canQueueNext=isDefaultReceiver and cls._nonNullUpdate(event.supports_queue_next, currentCapabilities.canQueueNext),
            canQueuePrevious=isDefaultReceiver and cls._nonNullUpdate(event.supports_queue_prev, currentCapabilities.canQueuePrevious),
        )
        currentMediaState = currentState.mediaState
        newMediaState = dataclasses.replace(
            currentState.mediaState,
            volumeMuted=event.volume_muted,
            volumeLevel=event.volume_level,
            title=event.title,
            imageUrl=event.images[0].url if event.images else '',
            contentUrl=event.content_id,
            playerState=cls._updateIfNotNull(currentMediaState.playerState, event.player_state, CastPlayerState)\
                if isDefaultReceiver else CastPlayerState.Idle,
            duration=cls._updateIfNotNull(currentMediaState.duration, event.duration, cls._secToMs),
            lastUpdatePosition=cls._updateIfNotNull(currentMediaState.lastUpdatePosition, event.adjusted_current_time, cls._secToMs),
            lastUpdateTimestamp=getTimestampMsNow(),
        )

        if newMediaState.playerState.isStopped():
            newCapabilities = CastCapabilities()
            newMediaState = CastMediaState()

        return dataclasses.replace(
            currentState,
            capabilities=newCapabilities,
            mediaState=newMediaState,
        )

    @staticmethod
    def _secToMs(value: int | float) -> Milliseconds:
        return Milliseconds.fromRawUnit(unit=Seconds, value=value)

    @staticmethod
    def _nonNullUpdate(value: _T | None, defaultValue: _T) -> _T:
        return defaultValue if value is None else value

    @staticmethod
    def _updateIfNotNull(currentValue: _T, newValue: _V | None, updateCallback: Callable[[_V], _T]) -> _T:
        return currentValue if newValue is None else updateCallback(newValue)
