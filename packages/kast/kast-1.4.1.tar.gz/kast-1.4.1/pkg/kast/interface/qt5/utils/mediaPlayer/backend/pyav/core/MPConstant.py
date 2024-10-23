#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from tunit.unit import Microseconds, Milliseconds


class MPConstant:
    SLEEP_WHILE_WAITING = Milliseconds(500)
    SLEEP_TO_COOL_DOWN = Microseconds(200)
    SLEEP_WHEN_IDLE = Milliseconds(1000)
