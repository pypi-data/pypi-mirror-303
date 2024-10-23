#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from kast.Services import Services
from kast.interface.overlay.common.MediaOverlayBase import MediaOverlayBase
from kast.media.casting.model.CastState import CastState
from kast.utils.log.Loggable import Loggable


class NullMediaOverlay(Loggable, MediaOverlayBase):

    def __init__(self, services: Services) -> None:
        super().__init__(services=services)

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass

    def onCastEvent(self, event: CastState) -> None:
        pass
