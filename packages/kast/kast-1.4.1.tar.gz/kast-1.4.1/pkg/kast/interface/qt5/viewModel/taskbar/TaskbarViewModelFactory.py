#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from PyQt5.QtWidgets import QMainWindow

from kast.interface.qt5.UiServices import UiServices
from kast.interface.qt5.viewModel.taskbar.ITaskbarViewModel import ITaskbarViewModel
from kast.interface.qt5.viewModel.taskbar.null.NullTaskbarViewModel import NullTaskbarViewModel
from kast.utils.OsInfo import OsInfo, OsName


class TaskbarViewModelFactory:

    @staticmethod
    def create(
        parent: QMainWindow,
        uiServices: UiServices,
        feignMode: bool = False
    ) -> ITaskbarViewModel:
        if feignMode:
            return NullTaskbarViewModel(
                parent=parent,
                uiServices=uiServices
            )

        if OsInfo.name == OsName.Linux:
            from .unity.UnityTaskbarViewModel import UnityTaskbarViewModel
            return UnityTaskbarViewModel(
                parent=parent,
                uiServices=uiServices
            )

        if OsInfo.name == OsName.Windows:
            from .win32.Win32TaskbarViewModel import Win32TaskbarViewModel
            return Win32TaskbarViewModel(
                parent=parent,
                uiServices=uiServices
            )

        return NullTaskbarViewModel(
            parent=parent,
            uiServices=uiServices
        )
