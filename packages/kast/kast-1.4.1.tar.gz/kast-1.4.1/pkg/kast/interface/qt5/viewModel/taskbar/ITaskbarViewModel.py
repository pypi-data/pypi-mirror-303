#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from abc import ABC, abstractmethod


class ITaskbarViewModel(ABC):

    @abstractmethod
    def _displayProgress(self, display: bool, percentage: float = 0.0) -> None: ...
