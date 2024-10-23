#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from abc import ABCMeta

from PyQt5 import sip


class QtAbcMeta(ABCMeta, sip.wrappertype):
    """
    Allows QObject based classes to inherit ABC based abstract classes. Usage:

    class NewClass(QObject, AbcBasedAbstractClass, metaclass=QtAbcMeta):
        ...
    """
