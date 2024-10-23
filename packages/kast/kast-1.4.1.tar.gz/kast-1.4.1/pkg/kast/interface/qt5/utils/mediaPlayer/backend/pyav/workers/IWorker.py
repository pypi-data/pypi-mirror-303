#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from abc import ABC, abstractmethod


class IWorker(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def run(self) -> None:
        pass

    @abstractmethod
    def cleanup(self) -> None:
        pass
