#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import inspect

from PyQt5.QtWidgets import QMainWindow

from kast.interface.qt5.UiServices import UiServices
from kast.interface.qt5.view.MainWindowView import Ui_MainWindowView
from kast.interface.qt5.viewModel.AboutViewModel import AboutViewModel
from kast.interface.qt5.viewModel.DeviceSearchViewModel import DeviceSearchViewModel
from kast.interface.qt5.viewModel.MediaControlViewModel import MediaControlViewModel
from kast.interface.qt5.viewModel.PreCastConversionViewModel import PreCastConversionViewModel
from kast.interface.qt5.viewModel.SettingsViewModel import SettingsViewModel
from kast.interface.qt5.viewModel.StatusBarViewModel import StatusBarViewModel
from kast.interface.qt5.viewModel.VideoPreviewViewModel import VideoPreviewViewModel
from kast.interface.qt5.viewModel.VideoSettingsViewModel import VideoSettingsViewModel
from kast.interface.qt5.viewModel.ViewModelBase import ViewBase, ViewModelBase
from kast.interface.qt5.viewModel.taskbar.ITaskbarViewModel import ITaskbarViewModel
from kast.interface.qt5.viewModel.taskbar.TaskbarViewModelFactory import TaskbarViewModelFactory


class View(ViewBase, QMainWindow, Ui_MainWindowView):
    pass


class MainWindowViewModel(ViewModelBase[View]):

    def __init__(self, uiServices: UiServices) -> None:
        super().__init__(uiServices=uiServices, view=View.createView(parent=None))
        self.view.setWindowTitle(self._getWindowTitle())

        self._taskbarViewModel: ITaskbarViewModel = TaskbarViewModelFactory.create(
            parent=self.view,
            uiServices=uiServices,
            feignMode=self.services.appRuntimeFlags.recovery
        )

        self._aboutViewModel = AboutViewModel(parent=self.view, uiServices=self.uiServices)
        self._settingsViewModel = SettingsViewModel(parent=self.view, uiServices=self.uiServices)
        self._deviceSearchViewModel = DeviceSearchViewModel(parent=self.view, uiServices=self.uiServices)
        self._preCastConversionViewModel = PreCastConversionViewModel(parent=self.view, uiServices=uiServices)
        self._videoPreviewViewModel = VideoPreviewViewModel(parent=self.view, uiServices=self.uiServices)
        self._mediaControlViewModel = MediaControlViewModel(parent=self.view, uiServices=self.uiServices)
        self._videoSettingsViewModel = VideoSettingsViewModel(parent=self.view, uiServices=self.uiServices)
        self._statusBarViewModel = StatusBarViewModel(parent=self.view, uiServices=self.uiServices)

        self.view.layoutForPreview.addWidget(self._videoPreviewViewModel.view)
        self._addControlsViewModel(self._mediaControlViewModel)
        self._addControlsViewModel(self._videoSettingsViewModel)
        self._addControlsViewModel(self._statusBarViewModel)

        self._videoPreviewViewModel.signalOnVolumeMutedChange.connect(self._mediaControlViewModel.setLocalMute)
        self._videoPreviewViewModel.signalOnVolumeLevelChange.connect(self._mediaControlViewModel.setLocalVolume)

        self._mediaControlViewModel.signalOnVolumeMutedChange.connect(self._videoPreviewViewModel.triggerMuted)
        self._mediaControlViewModel.signalOnVolumeLevelChange.connect(self._videoPreviewViewModel.setVolume)

        self._videoPreviewViewModel.triggerMuted()

        self.view.actionExit.triggered.connect(self.view.close)
        self.view.actionSettings.triggered.connect(self._settingsViewModel.view.show)
        self.view.actionAbout.triggered.connect(self._aboutViewModel.view.show)

    def _onStartup(self) -> None:
        if self.services.appRuntimeFlags.recovery:
            self.uiServices.dialogService.warning(message=inspect.cleandoc('''
                Application running in recovery mode!
                
                Some features are disabled.
                
                Most notable ones:
                \t- Local video preview
                \t- System media overlay integration
                \t- System taskbar integration
                '''))

    def _addControlsViewModel(self, viewModel: ViewModelBase) -> None:
        self.view.layoutForControls.addWidget(viewModel.view)

    def _getWindowTitle(self) -> str:
        appName = self.services.appInfo.appName
        return appName if not self.services.appRuntimeFlags.recovery \
            else f'{appName} [Recovery Mode]'
