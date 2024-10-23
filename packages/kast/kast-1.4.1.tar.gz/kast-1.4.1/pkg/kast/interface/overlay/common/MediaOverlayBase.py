#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from abc import ABC

from kast.Services import Services
from kast.interface.overlay.IMediaOverlay import IMediaOverlay


class MediaOverlayBase(IMediaOverlay, ABC):

    def __init__(self, services: Services) -> None:
        services.castEventObserver.register(self, self.onCastEvent)
