#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from pathlib import Path


def fileExtension(filePath: Path) -> str:
    return filePath.suffix.split('.', maxsplit=1)[-1]
