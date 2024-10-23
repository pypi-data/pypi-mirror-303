#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QWidget

from kast.interface.qt5.UiServices import UiServices
from kast.interface.qt5.view.SettingsView import Ui_SettingsView
from kast.interface.qt5.viewModel.LocalPlayerBackendSettingsViewModel import LocalPlayerBackendSettingsViewModel
from kast.interface.qt5.viewModel.ViewModelBase import ViewBase, ViewModelBase


class View(ViewBase, QDialog, Ui_SettingsView):
    pass


class SettingsViewModel(ViewModelBase[View]):

    def __init__(self, parent: QWidget, uiServices: UiServices) -> None:
        super().__init__(uiServices=uiServices, view=View.createView(hidden=True, parent=parent))

        self._previewBackendSection = LocalPlayerBackendSettingsViewModel(parent=self.view, uiServices=uiServices)

        self.view.tabWidget.addTab(self._previewBackendSection.view, "Local Player Backend")

        self.view.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self._onAccepted)
        self.view.accepted.connect(self._onAccepted)

    def _onAccepted(self) -> None:
        self._previewBackendSection.apply()
