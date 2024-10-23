#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import time
from logging import Formatter


class UtcFormatter(Formatter):
    converter = time.gmtime
