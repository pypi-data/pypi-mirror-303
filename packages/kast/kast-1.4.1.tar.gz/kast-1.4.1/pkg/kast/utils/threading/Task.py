#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from dataclasses import dataclass

from tunit.unit import Milliseconds

from kast.utils.functional import Runnable


@dataclass
class Task:
    runnable: Runnable
    scheduledTimestamp: Milliseconds = Milliseconds()
