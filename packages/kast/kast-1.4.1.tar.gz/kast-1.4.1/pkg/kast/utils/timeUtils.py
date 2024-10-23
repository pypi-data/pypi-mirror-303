#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import time

from tunit.unit import Milliseconds, Seconds


def getTimestampMsNow() -> Milliseconds:
    return Milliseconds.fromRawUnit(unit=Seconds, value=time.time())
