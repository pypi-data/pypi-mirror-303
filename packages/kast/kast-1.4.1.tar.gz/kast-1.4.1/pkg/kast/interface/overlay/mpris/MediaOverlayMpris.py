#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from mpris_api.MprisService import MprisService

from kast.Services import Services
from kast.interface.overlay.common.MediaOverlayBase import MediaOverlayBase
from kast.interface.overlay.mpris.MprisAdapterPlayer import MprisAdapterPlayer
from kast.interface.overlay.mpris.MprisAdapterRoot import MprisAdapterRoot
from kast.media.casting.model.CastState import CastState
from kast.utils.log.Loggable import Loggable


class MediaOverlayMpris(MediaOverlayBase, Loggable):

    def __init__(self, services: Services) -> None:
        super().__init__(services=services)

        self._mprisService: MprisService = MprisService(
            name=services.appInfo.appName,
            adapterRoot=MprisAdapterRoot(services=services),
            adapterPlayer=MprisAdapterPlayer(services=services),
        )

    def start(self) -> None:
        self._mprisService.start()

    def stop(self) -> None:
        self._mprisService.stop()

    def onCastEvent(self, event: CastState) -> None:
        self._mprisService.updateNotifier.emitPropertyChangeAll()
