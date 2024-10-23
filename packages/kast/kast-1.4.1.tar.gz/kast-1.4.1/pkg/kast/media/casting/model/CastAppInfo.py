#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from dataclasses import dataclass

RECEIVER_ID: str = 'CC1AD845'
RECEIVER_NAME: str = 'Default Media Receiver'


@dataclass(frozen=True)
class CastAppInfo:
    id: str = ''
    name: str = ''

    def isDefaultReceiver(self) -> bool:
        return (
            self.id == RECEIVER_ID or
            self.name == RECEIVER_NAME
        )
