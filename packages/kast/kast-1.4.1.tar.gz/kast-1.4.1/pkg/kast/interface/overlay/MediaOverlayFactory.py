#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from kast.Services import Services
from kast.interface.overlay.IMediaOverlay import IMediaOverlay
from kast.interface.overlay.null.NullMediaOverlay import NullMediaOverlay
from kast.utils.OsInfo import OsInfo, OsName


class MediaOverlayFactory:

    @staticmethod
    def create(
        services: Services,
        feignMode: bool = False
    ) -> IMediaOverlay:
        if feignMode:
            return NullMediaOverlay(services=services)

        if OsInfo.name == OsName.Linux:
            from .mpris.MediaOverlayMpris import MediaOverlayMpris
            return MediaOverlayMpris(services=services)

        if OsInfo.name == OsName.Windows:
            from .winrt.MediaOverlayWinrt import MediaOverlayWinrt
            return MediaOverlayWinrt(services=services)

        return NullMediaOverlay(services=services)
