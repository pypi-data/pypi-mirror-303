#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from dataclasses import dataclass
from enum import Enum, auto

from PyQt5.QtCore import QSize, QTimer, Qt
from PyQt5.QtGui import QBrush, QColor, QPalette
from PyQt5.QtWidgets import QDialog, QHeaderView, QStyle, QTableWidgetItem, QWidget

from kast.interface.qt5.UiServices import UiServices
from kast.interface.qt5.control.QtImageLabel import QtImageLabel
from kast.interface.qt5.service.UiEvent import UiEvent, UiState
from kast.interface.qt5.view.PreCastConversionView import Ui_PreCastConversionView
from kast.interface.qt5.viewModel.ViewModelBase import DialogViewBase, ViewModelBase
from kast.media.casting.CastMediaFormatService import CastDeviceProfile, CastMediaFormatService, \
    MediaInfo
from kast.media.processing.Resolution import Resolution
from kast.media.processing.Transcoder import Codecs
from kast.utils.log.Loggable import Loggable


class ConversionSpeed(Enum):
    NotRequired = auto()
    VeryFast = auto()
    Fast = auto()
    Slow = auto()


CONVERSION_SPEED_LABELS: dict[ConversionSpeed, str] = {
    ConversionSpeed.NotRequired: 'Not required',
    ConversionSpeed.VeryFast: 'Very fast',
    ConversionSpeed.Fast: 'Fast',
    ConversionSpeed.Slow: 'Slow',
}

CONVERSION_SPEED_EXTRA_INFO: dict[ConversionSpeed, str] = {
    ConversionSpeed.NotRequired: 'Media compatible or converted in cache',
    ConversionSpeed.VeryFast: 'Up to a minute',
    ConversionSpeed.Fast: 'Up to a few minutes',
    ConversionSpeed.Slow: 'Half an hour or more',
}


@dataclass
class ConversionTableEntry:
    current: str
    supported: str
    target: str
    speed: ConversionSpeed
    conversionRequired: bool

    def toList(self) -> list[str]:
        return [
            self.current,
            self.supported,
            self.target,
            CONVERSION_SPEED_LABELS.get(self.speed, ''),
        ]


@dataclass
class EntryStyle:
    foreground: QColor
    background: QColor

    def foregroundBrush(self) -> QBrush:
        return self._makeBrush(color=self.foreground)

    def backgroundBrush(self) -> QBrush:
        return self._makeBrush(color=self.background)

    def _makeBrush(self, color: QColor) -> QBrush:
        return QBrush(color, Qt.SolidPattern)


@dataclass
class TargetMediaFormat:
    containerFormat: str
    codecs: Codecs
    maxResolution: Resolution


class View(DialogViewBase, QDialog, Ui_PreCastConversionView):
    pass


class PreCastConversionViewModel(ViewModelBase[View], Loggable):

    _ENTRY_STYLE_OK: EntryStyle = EntryStyle(
        foreground=QColor(0, 0, 0),
        background=QColor(0, 170, 0),
    )
    _ENTRY_STYLE_WARNING: EntryStyle = EntryStyle(
        foreground=QColor(0, 0, 0),
        background=QColor(255, 255, 127),
    )

    def __init__(self, parent: QWidget, uiServices: UiServices) -> None:
        ViewModelBase.__init__(self, uiServices=uiServices, view=View.createView(hidden=True, parent=parent))
        self.uiServices.uiEventObserver.register(self, self._onUiEvent)

        self.view.signalOnOpen.connect(self._onOpen)
        self.view.signalOnClose.connect(self._onClose)

        self._imageLabel = imageLabel = QtImageLabel(parent=self.view)
        iconInfo = self.view.style().standardIcon(QStyle.SP_MessageBoxInformation)
        imageLabel.setPixmap(iconInfo.pixmap(QSize(500, 500)))
        imageLabel.setMinimumSize(32, 32)
        self.view.layoutInfoBox.insertWidget(0, imageLabel)
        self.view.layoutInfoBox.setStretch(1, 1)

        deviceProfileNames = [profile.model for profile in CastDeviceProfile]
        self.view.comboBoxDeviceModel.addItems(deviceProfileNames)
        self.view.comboBoxDeviceModel.currentIndexChanged.connect(lambda index: self._onUpdate())

        self.view.tableConversion.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.view.tableConversion.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.view.buttonBox.accepted.connect(self._onAccepted)

    def _onOpen(self) -> None:
        self._onUpdate()

    def _onClose(self) -> None:
        self.view.hide()
        self.uiServices.uiStateService.dispatch(UiEvent(state=UiState.Idle))

    def _onAccepted(self) -> None:
        self.uiServices.mediaControlService.startStream()

    def _onUiEvent(self, uiEvent: UiEvent) -> None:
        if uiEvent.state == UiState.CastMediaFormatSelection:
            self.view.show()

    def _onUpdate(self) -> None:
        profileAndMediaInfoOpt = self._getDeviceProfileAndMediaInfo()
        if profileAndMediaInfoOpt is None:
            QTimer.singleShot(0, self.view.reject)
            return

        profile, mediaInfo = profileAndMediaInfoOpt

        containerEntry = self._makeContainerEntry(mediaInfo=mediaInfo, profile=profile)
        resolutionEntry = self._makeResolutionEntry(mediaInfo=mediaInfo, profile=profile)
        videoCodecEntry = self._makeVideoCodecEntry(mediaInfo=mediaInfo, profile=profile)
        audioCodecEntry = self._makeAudioCodecEntry(mediaInfo=mediaInfo, profile=profile)

        self.uiServices.mediaControlService.castContainerFormat = containerEntry.target
        self.uiServices.mediaControlService.castCodecs = Codecs(
            video=videoCodecEntry.target,
            audio=audioCodecEntry.target
        )
        self.uiServices.mediaControlService.castMaxResolution = Resolution.fromStr(resolutionEntry.supported)

        self._updateConversionTable(
            entries=[
                containerEntry,
                resolutionEntry,
                videoCodecEntry,
                audioCodecEntry,
            ],
            isCached=(not self.uiServices.mediaControlService.hasStreamParamsChanged())
        )

    def _updateConversionTable(self, entries: list[ConversionTableEntry], isCached: bool) -> None:
        table = self.view.tableConversion
        table.clearContents()
        for rowIndex in range(table.rowCount()):
            rowEntry = entries[rowIndex]
            itemContentList = rowEntry.toList()
            for columnIndex in range(table.columnCount()):
                item = QTableWidgetItem(itemContentList[columnIndex])

                style = self._ENTRY_STYLE_WARNING if rowEntry.conversionRequired\
                    else self._ENTRY_STYLE_OK

                item.setForeground(style.foregroundBrush())
                item.setBackground(style.backgroundBrush())

                table.setItem(rowIndex, columnIndex, item)

        self._updateTotalConversionSpeed(
            speed=ConversionSpeed(max(entry.speed.value for entry in entries)),
            isCached=isCached
        )

    def _updateTotalConversionSpeed(self, speed: ConversionSpeed, isCached: bool) -> None:
        speed = speed if not isCached else ConversionSpeed.NotRequired
        label = CONVERSION_SPEED_LABELS.get(speed)
        extraInfo = CONVERSION_SPEED_EXTRA_INFO.get(speed)

        lineEdit = self.view.lineEditSpeedTotal
        lineEdit.setText(f"{label} ({extraInfo})")

        style = self._ENTRY_STYLE_WARNING if speed != ConversionSpeed.NotRequired \
            else self._ENTRY_STYLE_OK
        palette = lineEdit.palette()
        palette.setColor(QPalette.Base, style.background)
        palette.setColor(QPalette.Text, style.foreground)
        lineEdit.setPalette(palette)

    def _getDeviceProfileAndMediaInfo(self) -> tuple[CastDeviceProfile, MediaInfo] | None:
        profileName = self.view.comboBoxDeviceModel.currentText()
        profileOpt = self._findDeviceProfileByName(profileName=profileName)
        if profileOpt is None:
            self.log.error(f"Device profile info missing! profile='{profileName}'")
            self.uiServices.dialogService.error(message="Device profile info missing! Please select other one.")
            return None

        metaDataOpt = self.uiServices.mediaControlService.metaData
        if metaDataOpt is None:
            self.log.error("Media file meta data requested before extraction!")
            self.uiServices.dialogService.error(message="Media file meta data missing!")
            return None

        videoStreamId, audioStreamId = (
            self.uiServices.mediaControlService.videoStreamId,
            self.uiServices.mediaControlService.audioStreamId,
        )
        if videoStreamId is None or audioStreamId is None:
            self.log.error(f"Media stream selection info missing! mediaStreamIds={videoStreamId, audioStreamId}")
            self.uiServices.dialogService.error(message="Media stream selection info missing!")
            return None

        mediaInfo = CastMediaFormatService.makeMediaInfo(
            videoStreamId=videoStreamId,
            audioStreamId=audioStreamId,
            metaData=metaDataOpt
        )

        return profileOpt, mediaInfo

    @staticmethod
    def _makeAudioCodecEntry(mediaInfo: MediaInfo, profile: CastDeviceProfile) -> ConversionTableEntry:
        conversionRequired = CastMediaFormatService.shouldChangeAudioCodec(
            mediaInfo=mediaInfo,
            profile=profile
        )
        currentCodec = str(mediaInfo.audioCodec)
        supportedCodecs = [codec for codec in profile.mediaFormatSupport.audioCodecs]
        conversionSpeed = ConversionSpeed.Fast if conversionRequired else ConversionSpeed.NotRequired
        return ConversionTableEntry(
            current=currentCodec,
            supported=','.join(supportedCodecs),
            target=supportedCodecs[0] if conversionRequired else currentCodec,
            speed=conversionSpeed,
            conversionRequired=conversionRequired,
        )

    @staticmethod
    def _makeVideoCodecEntry(mediaInfo: MediaInfo, profile: CastDeviceProfile) -> ConversionTableEntry:
        conversionRequired = CastMediaFormatService.shouldChangeVideoCodec(
            mediaInfo=mediaInfo,
            profile=profile
        )
        currentCodec = str(mediaInfo.videoCodec)
        supportedCodecs = [codec for codec in profile.mediaFormatSupport.videoCodecs]
        conversionSpeed = ConversionSpeed.Slow if conversionRequired else ConversionSpeed.NotRequired
        return ConversionTableEntry(
            current=currentCodec,
            supported=','.join(supportedCodecs),
            target=supportedCodecs[0] if conversionRequired else currentCodec,
            speed=conversionSpeed,
            conversionRequired=conversionRequired,
        )

    @staticmethod
    def _makeResolutionEntry(mediaInfo: MediaInfo, profile: CastDeviceProfile) -> ConversionTableEntry:
        conversionRequired = CastMediaFormatService.shouldChangeResolution(
            mediaInfo=mediaInfo,
            profile=profile
        )
        currentResolution = mediaInfo.resolution
        maxResolution = profile.mediaFormatSupport.maxResolution
        targetResolution = currentResolution.shrinkToFit(boundingSize=maxResolution)
        conversionSpeed = ConversionSpeed.Slow if conversionRequired else ConversionSpeed.NotRequired
        return ConversionTableEntry(
            current=str(currentResolution),
            supported=str(maxResolution),
            target=str(targetResolution),
            speed=conversionSpeed,
            conversionRequired=conversionRequired,
        )

    @staticmethod
    def _makeContainerEntry(mediaInfo: MediaInfo, profile: CastDeviceProfile) -> ConversionTableEntry:
        conversionRequired = CastMediaFormatService.shouldChangeContainer(
            mediaInfo=mediaInfo,
            profile=profile
        )
        currentContainer = mediaInfo.container
        supportedContainerExtensions = [container.extension for container in profile.mediaFormatSupport.containers]
        conversionSpeed = ConversionSpeed.VeryFast if conversionRequired else ConversionSpeed.NotRequired
        return ConversionTableEntry(
            current=currentContainer,
            supported=','.join(supportedContainerExtensions),
            target=supportedContainerExtensions[0] if conversionRequired else currentContainer,
            speed=conversionSpeed,
            conversionRequired=conversionRequired,
        )

    @staticmethod
    def _findDeviceProfileByName(profileName: str) -> CastDeviceProfile | None:
        for profile in CastDeviceProfile:
            if profile.model == profileName:
                return profile

        return None
