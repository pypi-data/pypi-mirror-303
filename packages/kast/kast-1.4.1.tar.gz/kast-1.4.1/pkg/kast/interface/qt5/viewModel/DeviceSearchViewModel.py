#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QHeaderView, QTreeWidgetItem, QWidget

from kast.interface.qt5.UiServices import UiServices
from kast.interface.qt5.service.UiEvent import UiEvent, UiState
from kast.interface.qt5.utils.threading.Schedulable import Schedulable
from kast.interface.qt5.view.DeviceSearchView import Ui_DeviceSearchView
from kast.interface.qt5.viewModel.ViewModelBase import DialogViewBase, ViewModelBase
from kast.media.casting.model.DeviceInfo import DeviceInfo
from kast.utils.Maybe import Maybe
from kast.utils.log.Loggable import Loggable


class DeviceSelectionError(Exception):
    pass


class View(DialogViewBase, QDialog, Ui_DeviceSearchView):
    pass


class DeviceSearchViewModel(ViewModelBase[View], Loggable, Schedulable):

    def __init__(self, parent: QWidget, uiServices: UiServices) -> None:
        ViewModelBase.__init__(self, uiServices=uiServices, view=View.createView(hidden=True, parent=parent))
        Schedulable.__init__(self, threadContext=uiServices.threadContext)
        self.uiServices.uiEventObserver.register(self, self._onUiEvent)

        self.view.signalOnOpen.connect(self._onOpen)
        self.view.signalOnClose.connect(self._onClose)

        treeWidget = self.view.treeWidget
        treeWidget.itemSelectionChanged.connect(self._onSelectionChange)
        treeWidget.doubleClicked.connect(self._onDevicePickApprove)
        treeWidget.header().setSectionResizeMode(QHeaderView.Stretch)

        buttonBox = self.view.buttonBox
        buttonBox.accepted.disconnect()
        buttonBox.rejected.disconnect()
        buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self._onClose)
        buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self._onDevicePickApprove)
        buttonBox.button(QDialogButtonBox.Retry).clicked.connect(self._onRefresh)

    def _onOpen(self) -> None:
        self._enableOkButton(enable=False)
        self._onRefresh()

    def _onClose(self) -> None:
        self.services.castController.stopSearch()
        self.uiServices.uiStateService.dispatch(UiEvent(state=UiState.Idle))
        self.view.hide()

    def _onShutdown(self) -> None:
        self.services.castController.stopSearch()

    def _onUiEvent(self, uiEvent: UiEvent) -> None:
        if uiEvent.state == UiState.DeviceSearch:
            self.view.show()

    def _onDevicePickApprove(self) -> None:
        try:
            self.uiServices.mediaControlService.castDeviceInfo = Maybe(self.view.treeWidget.selectedItems())\
                .filter(lambda items: len(items) > 0)\
                .map(lambda items: items[0])\
                .map(lambda item: item.text(0))\
                .map(self._findDeviceInfo)\
                .orThrow(lambda: DeviceSelectionError("Selected cast device info not found!"))

            self._onClose()

        except DeviceSelectionError as ex:
            self.log.exception(ex)
            self.uiServices.dialogService.error(message="Selecting cast device failed! Please try again.")

    def _onRefresh(self) -> None:
        self.view.treeWidget.clear()
        self.services.castController.searchDevices(callback=self._onDeviceDiscovered)

    def _onDeviceEntryDoubleClick(self, item: QTreeWidgetItem, column: int) -> None:
        if item is None:
            self.log.error("Device entry double click reported, but the entry is null!")
            return

        self._onDevicePickApprove()

    def _onSelectionChange(self) -> None:
        self._enableOkButton(enable=self._isDeviceSelected())

    @Schedulable.foregroundTask
    def _onDeviceDiscovered(self, deviceInfo: DeviceInfo) -> None:
        treeWidget = self.view.treeWidget
        item = QTreeWidgetItem([
            deviceInfo.name,
            deviceInfo.model,
            deviceInfo.manufacturer,
        ])
        treeWidget.addTopLevelItem(item)
        if treeWidget.topLevelItemCount() == 1:
            treeWidget.setCurrentItem(item)
            treeWidget.setFocus()

    def _findDeviceInfo(self, deviceName: str) -> DeviceInfo | None:
        discoveredDevices = self.services.castController.discoveredDeviceInfo
        for deviceInfo in discoveredDevices:
            if deviceName == deviceInfo.name:
                return deviceInfo

        return None

    def _enableOkButton(self, enable: bool) -> None:
        self.view.buttonBox\
            .button(QDialogButtonBox.StandardButton.Ok)\
            .setEnabled(enable)

    def _isDeviceSelected(self) -> bool:
        return len(self.view.treeWidget.selectedItems()) > 0
