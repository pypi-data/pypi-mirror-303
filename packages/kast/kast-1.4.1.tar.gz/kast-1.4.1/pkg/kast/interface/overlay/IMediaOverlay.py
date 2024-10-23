#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from abc import ABC, abstractmethod

from kast.media.casting.model.CastState import CastState


class IMediaOverlay(ABC):

    @abstractmethod
    def start(self) -> None: ...
    @abstractmethod
    def stop(self) -> None: ...
    @abstractmethod
    def onCastEvent(self, event: CastState) -> None: ...
