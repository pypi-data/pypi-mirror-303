#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from pathlib import Path

from PyQt5.QtWidgets import QComboBox, QFileDialog, QStyle, QWidget

from kast.core.settings.SettingsKeys import SettingsKeys
from kast.interface.qt5.UiServices import UiServices
from kast.interface.qt5.service.UiEvent import Progress, UiEvent, UiState
from kast.interface.qt5.view.VideoSettingsView import Ui_VideoSettingsView
from kast.interface.qt5.viewModel.ViewModelBase import ViewBase, ViewModelBase
from kast.media.processing.SubtitlesSourceList import SubtitlesSourceList
from kast.media.processing.Transcoder import TranscodeParams
from kast.utils.Maybe import Maybe
from kast.utils.log.Loggable import Loggable


class View(ViewBase, QWidget, Ui_VideoSettingsView):
    pass


class VideoSettingsViewModel(Loggable, ViewModelBase[View]):

    _LABEL_NO_SUBTITLES: str = 'No Subtitles'

    def __init__(self, parent: QWidget, uiServices: UiServices) -> None:
        super().__init__(uiServices=uiServices, view=View.createView(parent=parent))
        self.uiServices.uiEventObserver.register(self, self._onUiEvent)

        self.view.buttonDeviceRefresh.setIcon(self.view.style().standardIcon(QStyle.SP_BrowserReload))
        self.view.buttonVideoOpen.setIcon(self.view.style().standardIcon(QStyle.SP_DirOpenIcon))
        self.view.buttonSubtitlesAdd.setIcon(self.view.style().standardIcon(QStyle.SP_DirOpenIcon))

        self.view.buttonDeviceRefresh.clicked.connect(self._onSearchDevice)
        self.view.buttonVideoOpen.clicked.connect(self._signalVideoOpen)
        self.view.buttonSubtitlesAdd.clicked.connect(self._signalSubtitlesAdd)
        self.view.buttonStream.clicked.connect(self._signalStream)

        self.uiServices.mediaControlService.signalOnMetaDataChange.connect(self._onMetaDataChange)
        self.uiServices.mediaControlService.signalOnCastDeviceChange.connect(self._onCastDeviceChange)

        self._subtitlesSourceList = SubtitlesSourceList()
        self._lastTranscodeParams: TranscodeParams | None = None

        self._fillSubtitlesComboBox()

    def _onUiEvent(self, uiEvent: UiEvent) -> None:
        viewEnabled = uiEvent.state == UiState.Idle
        self.view.setEnabled(viewEnabled)

        self.view.setVisible(uiEvent.state != UiState.Streaming)

    def _onSearchDevice(self) -> None:
        self.uiServices.uiStateService.dispatch(UiEvent(state=UiState.DeviceSearch, progress=Progress(complete=False)))

    def _onMetaDataChange(self) -> None:
        self._fillAudioComboBox()
        self._fillSubtitlesComboBox()

    def _onCastDeviceChange(self) -> None:
        deviceName = Maybe(self.uiServices.mediaControlService.castDeviceInfo)\
            .map(lambda deviceInfo: deviceInfo.name)\
            .orElse('')
        self.view.lineEditDevice.setText(deviceName)

    def _signalVideoOpen(self) -> None:
        filePath = QFileDialog.getOpenFileName(
            self.view,
            "Open Video",
            self._getPreviousMediaBrowsePath(),
            "Videos (*.mp4 *.mkv *.webm *.avi)"
        )[0]
        if not filePath:
            return

        self.view.lineEditVideo.setText(filePath)

        self.uiServices.mediaControlService.videoFilePath = Path(filePath)

    def _signalSubtitlesAdd(self) -> None:
        filePathStr = QFileDialog.getOpenFileName(
            self.view,
            "Open Subtitles",
            str(self._getPreviousMediaBrowsePath()),
            "Subtitles (*.srt *.sub *.ass *.ssa *.txt *.vtt)"
        )[0]
        if not filePathStr:
            return

        filePath = Path(filePathStr)

        self.uiServices.mediaControlService.addSubtitles(filePath)

        self._fillSubtitlesComboBox()
        self.view.comboBoxSubtitles.setCurrentIndex(self.view.comboBoxSubtitles.count() - 1)

    def _signalStream(self) -> None:
        mediaControlService = self.uiServices.mediaControlService
        mediaControlService.videoStreamId = 0  # Might be switchable in the future.
        mediaControlService.audioStreamId = self._getSelectedAudioStreamId()
        mediaControlService.subtitleId = self._getSelectedSubtitlesId()

        if mediaControlService.videoFilePath is None or mediaControlService.castDeviceInfo is None:
            self.uiServices.dialogService.warning(message="Video file and cast device must be selected before streaming!")
            return

        self.uiServices.uiStateService.dispatch(UiEvent(state=UiState.CastMediaFormatSelection, progress=Progress(complete=False)))

    def _getPreviousMediaBrowsePath(self) -> str:
        mediaPathStr = self.services.settingsFacade.get(key=SettingsKeys.BrowseMediaPath)
        return str(mediaPathStr) if mediaPathStr is not None else ''

    def _getSelectedAudioStreamId(self) -> int:
        return self.view.comboBoxAudio.currentIndex()  # TODO: Should we care if it fails (-1)?

    def _getSelectedSubtitlesId(self) -> int | None:
        selectedSubtitles = self.view.comboBoxSubtitles.currentIndex()
        return (selectedSubtitles - 1) if selectedSubtitles > 0 else None

    def _fillAudioComboBox(self) -> None:
        self._fillComboBox(
            self.view.comboBoxAudio,
            self.uiServices.mediaControlService.audioStreamList
        )

    def _fillSubtitlesComboBox(self) -> None:
        self._fillComboBox(
            self.view.comboBoxSubtitles,
            [self._LABEL_NO_SUBTITLES] + self.uiServices.mediaControlService.subtitleList
        )

    @staticmethod
    def _fillComboBox(comboBox: QComboBox, items: list[str] | None = None) -> None:
        comboBox.clear()
        if items is not None:
            comboBox.addItems(items)
