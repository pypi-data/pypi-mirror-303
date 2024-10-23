#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from kast.interface.qt5.service.UiEvent import UiEvent, UiState
from kast.interface.qt5.service.UiEventObserver import UiEventObserver
from kast.interface.qt5.utils.threading.Schedulable import Schedulable
from kast.interface.qt5.utils.threading.foreground.ForegroundSchedulable import ForegroundSchedulable
from kast.interface.qt5.utils.threading.foreground.ForegroundThreadContext import ForegroundThreadContext
from kast.media.casting.CastEventObserver import CastEventObserver
from kast.media.casting.model.CastState import CastState
from kast.utils.log.Loggable import Loggable


class UiStateService(Loggable, ForegroundSchedulable):

    def __init__(
        self,
        foregroundThreadContext: ForegroundThreadContext,
        uiEventObserver: UiEventObserver,
        castEventObserver: CastEventObserver
    ) -> None:
        ForegroundSchedulable.__init__(self, foregroundThreadContext=foregroundThreadContext)

        self._uiEventObserver = uiEventObserver

        self._uiEvent = UiEvent()
        self._castState = CastState()

        castEventObserver.register(listener=self, callback=self._onCastEvent)

    @property
    def uiEvent(self) -> UiEvent:
        return self._uiEvent

    @property
    def castState(self) -> CastState:
        return self._castState

    @Schedulable.foregroundTask
    def dispatch(self, uiEvent: UiEvent) -> None:
        self._uiEvent = uiEvent
        self._dispatch()

    @Schedulable.foregroundTask
    def _onCastEvent(self, event: CastState) -> None:
        self._castState = event
        self._updateUiState()
        self._dispatch()

    def _updateUiState(self) -> None:
        if (self._uiEvent.state == UiState.Streaming) and (not self._castState.connection.isConnectedOrRecoverable()):
            self._uiEvent = UiEvent(UiState.Idle)
            return

        if (self._uiEvent.state == UiState.Idle) and self._castState.connection.isConnectedOrRecoverable():
            self._uiEvent = UiEvent(UiState.Streaming)
            return

    def _dispatch(self) -> None:
        self.log.info(
            f"UiState={self.uiEvent.state.name}, "
            f"DeviceState={self.castState.connection.value.lower().capitalize()}, "
            f"MediaState={self.castState.mediaState.playerState.value.lower().capitalize()}"
        )

        self._uiEventObserver.notify(self._uiEvent)
