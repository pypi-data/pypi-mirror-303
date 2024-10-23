#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from PyQt5.QtWidgets import QRadioButton, QWidget

from kast.core.settings.SettingsKeys import SettingsKeys
from kast.interface.qt5.UiServices import UiServices
from kast.interface.qt5.utils.mediaPlayer.MediaPlayerFactory import MediaPlayerBackend, MediaPlayerFactory
from kast.interface.qt5.view.LocalPlayerBackendSettingsView import Ui_LocalPlayerBackendSettingsView
from kast.interface.qt5.viewModel.ViewModelBase import ViewBase, ViewModelBase


def _stripDescription(text: str) -> str:
    return '\n'.join([line.strip() for line in text.strip().split('\n')]).strip()


class View(ViewBase, QWidget, Ui_LocalPlayerBackendSettingsView):
    pass


class LocalPlayerBackendSettingsViewModel(ViewModelBase[View]):

    _BACKEND_DESCRIPTIONS: dict[MediaPlayerBackend, str] = {
        MediaPlayerBackend.Null: _stripDescription('''
            Mock implementation of a media player:
            -> Available on all platforms.
            -> Disables local player.
        '''),
        MediaPlayerBackend.PyAV: _stripDescription('''
            Media player engine built with PyAV:
            -> Available on Linux and Windows.
            -> Planned to be the default choice on all platforms.
            -> Uses media codecs from (builtin) FFmpeg.
            -> Still experimental.
        '''),
        MediaPlayerBackend.Qt: _stripDescription('''
            Qt implementation of a media player:
            -> Available on all platforms.
            -> Requires media codecs to be installed on your system.
            -> On Linux based on gstreamer.
            -> On Windows based either on DirectShow or Windows Media Foundation.
            -> Planned to be phased out.
        '''),
        MediaPlayerBackend.WinRt: _stripDescription('''
            Media player engine built with WinRT:
            -> Available only on Windows.
            -> Requires some proprietary codecs (e.g. HEVC) to be installed on your system.
            -> Based on Windows Media Foundation.
            -> Experimental.
        '''),
    }

    def __init__(self, parent: QWidget, uiServices: UiServices) -> None:
        super().__init__(uiServices=uiServices, view=View.createView(parent=parent))

        self._selectedBackend: MediaPlayerBackend = MediaPlayerBackend(self.services.settingsFacade.get(SettingsKeys.MediaPreviewBackendEngine))

        self._setDescription()
        for backend in MediaPlayerFactory.getSupportedBackends():
            radioButton = QRadioButton(backend.name, self.view.groupBox)
            radioButton.toggled.connect(lambda checked, backendCapture=backend: self._onBackendSelected(checked, backendCapture))
            self.view.layoutRadioButtons.addWidget(radioButton)
            if backend == self._selectedBackend:
                radioButton.setChecked(True)

    def apply(self) -> None:
        self.services.settingsFacade.set(SettingsKeys.MediaPreviewBackendEngine, self._selectedBackend.value)

    def _onBackendSelected(self, checked: bool, backend: MediaPlayerBackend) -> None:
        if checked:
            self._selectedBackend = backend
            self._setDescription()

    def _setDescription(self) -> None:
        self.view.textEditDescription.setPlainText(self._BACKEND_DESCRIPTIONS[self._selectedBackend])
