#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from kast.interface.qt5.utils.QtAbcMeta import QtAbcMeta


class QtAbc(metaclass=QtAbcMeta):
    """
    Allows QObject based classes to inherit ABC based abstract classes. Usage:

    class NewClass(QtAbc, QObject, AbcBasedAbstractClass):  # Must be the first inherited class!
        ...
    """
