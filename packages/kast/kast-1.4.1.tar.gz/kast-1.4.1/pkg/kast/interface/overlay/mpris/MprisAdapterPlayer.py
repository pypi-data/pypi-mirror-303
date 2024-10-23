#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from mpris_api.adapter.IMprisAdapterPlayer import IMprisAdapterPlayer
from mpris_api.common.DbusObject import DbusObject
from mpris_api.model.MprisLoopStatus import MprisLoopStatus
from mpris_api.model.MprisMetaData import MprisMetaData
from mpris_api.model.MprisPlaybackStatus import MprisPlaybackStatus
from mpris_api.model.MprisTrack import MprisTrack
from tunit.unit import Microseconds, Milliseconds

from kast.Services import Services
from kast.core.AppInfo import AppInfo
from kast.media.casting.CastController import CastController
from kast.media.casting.model.CastConnectionState import CastConnectionState
from kast.media.casting.model.CastState import CastState
from kast.utils.Maybe import Maybe


class MprisAdapterPlayer(IMprisAdapterPlayer):

    def __init__(self, services: Services) -> None:
        self._services: Services = services

    @property
    def _appInfo(self) -> AppInfo:
        return self._services.appInfo

    @property
    def _castState(self) -> CastState:
        return self._services.castController.castState

    @property
    def _castController(self) -> CastController:
        return self._services.castController

    def canControl(self) -> bool:
        return True

    def canPlay(self) -> bool:
        return True

    def canPause(self) -> bool:
        return True

    def canGoNext(self) -> bool:
        return False

    def canGoPrevious(self) -> bool:
        return False

    def canSeek(self) -> bool:
        return True

    def getMinimumRate(self) -> float:
        return self.DEFAULT_RATE

    def getMaximumRate(self) -> float:
        return self.DEFAULT_RATE

    def getRate(self) -> float:
        return self.DEFAULT_RATE

    def setRate(self, value: float) -> None:
        pass

    def getVolume(self) -> float:
        return self._castState\
            .mediaState\
            .volumeLevel

    def setVolume(self, value: float) -> None:
        self._castController.setVolume(value=value)

    def getMetadata(self) -> MprisMetaData:
        return MprisMetaData(
            trackId=self._getTrack(),
            length=Microseconds(self._castState.mediaState.duration),
            artUrl=self._getArtUrl(),
            url=self._getMediaUrl(),
            title=self._getTitle(),
            artists=[self._castState.deviceInfo.name],
        )

    def getPlaybackStatus(self) -> MprisPlaybackStatus:
        if self._castState.mediaState.playerState.isPlaying():
            return MprisPlaybackStatus.PLAYING
        if self._castState.mediaState.playerState.isPaused():
            return MprisPlaybackStatus.PAUSED
        return MprisPlaybackStatus.STOPPED

    def getPosition(self) -> Microseconds:
        return Microseconds(self._castState.mediaState.currentPosition)

    def getLoopStatus(self) -> MprisLoopStatus:
        return MprisLoopStatus.NONE

    def setLoopStatus(self, value: MprisLoopStatus) -> None:
        pass

    def isShuffle(self) -> bool:
        return False

    def setShuffle(self, value: bool) -> None:
        pass

    def stop(self) -> None:
        self._castController.stop()

    def play(self) -> None:
        self._castController.play()

    def pause(self) -> None:
        self._castController.pause()

    def next(self) -> None:
        pass  # TODO: Should we support that?

    def previous(self) -> None:
        pass  # TODO: Should we support that?

    def seek(self, position: Microseconds, trackId: str | None = None) -> None:
        self._castController.seek(timePos=Milliseconds(position))

    def openUri(self, uri: str) -> None:
        pass  # TODO: Should we support that?

    def _getTrack(self) -> DbusObject:
        title = self._getTitle()
        return DbusObject(value=f'/track/{title}') if title\
            else MprisTrack.DEFAULT

    def _getArtUrl(self) -> str:
        return (
            self._castState.mediaState.imageUrl
            or self._castState.mediaState.iconUrl
            or str(self._appInfo.appIconPath)
        )

    def _getMediaUrl(self) -> str | None:
        return Maybe(self._castState.mediaState.contentUrl)\
            .filter(lambda url: bool(url))\
            .value

    def _getTitle(self) -> str:
        title = self._castState.mediaState.title \
            if self._castState.mediaState.title is not None \
            else self._appInfo.appName

        if self._castState.connection == CastConnectionState.Lost:
            title = f'[Connection Lost] {title}'

        return title
