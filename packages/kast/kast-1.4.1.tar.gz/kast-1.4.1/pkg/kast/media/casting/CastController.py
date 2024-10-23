#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import pychromecast
from pychromecast.controllers.media import MediaStatus
from tunit.unit import Milliseconds, Seconds

from kast.core.AppInfo import AppInfo
from kast.media.casting.CastDeviceStateListener import CastDeviceStateListener
from kast.media.casting.CastEventObserver import CastEventObserver
from kast.media.casting.CastException import CastException
from kast.media.casting.model.CastMediaState import VolumeLevel
from kast.media.casting.model.CastState import CastState
from kast.media.casting.model.DeviceInfo import DeviceInfo
from kast.utils.Maybe import Maybe
from kast.utils.functional import Consumer
from kast.utils.log.Loggable import Loggable


class CastController(Loggable):
    TIMEOUT_FAST = Seconds(10)
    TIMEOUT_SLOW = Seconds(10)
    SEEK_DELTA = Milliseconds(Seconds(10))

    def __init__(
            self,
            appInfo: AppInfo,
            castEventObserver: CastEventObserver
    ) -> None:
        self._appInfo: AppInfo = appInfo
        self._castEventObserver = castEventObserver

        self._deviceDiscoverer: pychromecast.CastBrowser | None = None
        self._discoveredDeviceInfo: list[DeviceInfo] = []

        self._castDeviceStateListener: CastDeviceStateListener = CastDeviceStateListener()
        self._device: pychromecast.Chromecast | None = None
        self._castState: CastState = CastState()

    @property
    def _mediaController(self) -> pychromecast.controllers.media.MediaController | None:
        return Maybe(self._device).map(lambda device: device.media_controller).value  # type: ignore

    @property
    def castState(self) -> CastState:
        return self._castState

    @property
    def isConnected(self) -> bool:
        return Maybe(self._device) \
            .map(lambda _: self._castState.connection.isConnected()) \
            .orElse(False)

    @property
    def discoveredDeviceInfo(self) -> list[DeviceInfo]:
        return self._discoveredDeviceInfo

    def stopSearch(self) -> None:
        Maybe(self._deviceDiscoverer).ifPresent(lambda discoverer: discoverer.stop_discovery())  # type: ignore
        self._deviceDiscoverer = None

    def searchDevices(
        self,
        callback: Consumer[DeviceInfo] = lambda d: None,
        timeout: Seconds | None = TIMEOUT_FAST
    ) -> None:
        self._discoveredDeviceInfo = []
        self.stopSearch()
        self._deviceDiscoverer = pychromecast.get_chromecasts(
            blocking=False,
            timeout=float(timeout) if timeout is not None else None,
            callback=lambda device: self._onDeviceDiscovered(
                device=device,
                callback=callback
            )
        )

    def connect(self, name: str) -> None:
        self.disconnect()

        chromecasts, castBrowser = pychromecast.get_chromecasts(timeout=float(self.TIMEOUT_FAST))
        castBrowser.stop_discovery()
        for chromecast in chromecasts:
            if name == chromecast.name:
                self._setupDevice(chromecast)
                return
        raise CastException(f"Could not find device by name '{name}'!")

    def disconnect(self) -> None:
        device = self._device
        if device is None:
            return

        self._castDeviceStateListener.unregister()

        if self._castState.appInfo.isDefaultReceiver():
            self._quitApp(device=device)

        self._onCastStateChange(castState=CastState())

        device.disconnect(timeout=float(self.TIMEOUT_SLOW))

    def stream(
            self,
            movieUrl: str,
            movieMime: str = 'video/mp4',
            subtitlesUrl: str | None = None,
            subtitlesMime: str = 'text/vtt',
            thumbnailUrl: str | None = None,
            play: bool = True,
            title: str | None = None
    ) -> None:
        title = title if title is not None else self._appInfo.appName

        device = self._device
        if not device:
            return

        mediaController = device.media_controller
        if not mediaController:
            return

        device.quit_app()

        mediaController.play_media(
            url=movieUrl,
            content_type=movieMime,
            subtitles=subtitlesUrl,
            subtitles_mime=subtitlesMime,
            autoplay=play,
            title=title,
            thumb=thumbnailUrl
        )
        mediaController.block_until_active(timeout=float(self.TIMEOUT_FAST))

    def quit(self) -> None:
        if self._castState.appInfo.isDefaultReceiver():
            Maybe(self._device).ifPresent(lambda device: self._quitApp(device=device))

    def setMute(self, value: bool) -> None:
        Maybe(self._device).ifPresent(lambda device: device.set_volume_muted(value))  # type: ignore

    def setVolume(self, value: VolumeLevel) -> None:
        Maybe(self._device).ifPresent(lambda device: device.set_volume(value))  # type: ignore

    def play(self) -> None:
        Maybe(self._mediaController).ifPresent(lambda mediaController: mediaController.play())  # type: ignore

    def pause(self) -> None:
        Maybe(self._mediaController).ifPresent(lambda mediaController: mediaController.pause())  # type: ignore

    def stop(self) -> None:
        Maybe(self._mediaController).ifPresent(lambda mediaController: mediaController.stop())  # type: ignore

    def seek(self, timePos: Milliseconds) -> None:
        Maybe(self._mediaController).ifPresent(
            lambda mediaController: mediaController.seek(timePos.toRawUnit(unit=Seconds)))  # type: ignore

    def seekForward(self) -> None:
        self.seek(self._castState.mediaState.currentPosition + self.SEEK_DELTA)

    def seekBackward(self) -> None:
        self.seek(self._castState.mediaState.currentPosition - self.SEEK_DELTA)

    def _onDeviceDiscovered(
            self,
            device: pychromecast.Chromecast,
            callback: Consumer[DeviceInfo]
    ) -> None:
        if device.cast_info.cast_type != pychromecast.CAST_TYPE_CHROMECAST:
            self.log.debug(
                f"Ignoring unsupported device! name='{device.name}', castType='{device.cast_info.cast_type}'")
            return

        deviceInfo = DeviceInfo(
            name=device.name,
            model=device.model_name,
            manufacturer=device.cast_info.manufacturer
        )
        self._discoveredDeviceInfo.append(deviceInfo)
        callback(deviceInfo)

    def _setupDevice(self, device: pychromecast.Chromecast) -> None:
        if device.cast_type != pychromecast.CAST_TYPE_CHROMECAST:
            raise CastException(f"Device '{device.name}' does not support video casting!")

        self._castDeviceStateListener.register(
            device=device,
            updateCallback=self._onCastStateChange
        )

        device.wait(timeout=float(self.TIMEOUT_FAST))

        self._device = device

    def _quitApp(self, device: pychromecast.Chromecast) -> None:
        try:
            device.quit_app()
        except pychromecast.error.ControllerNotRegistered:
            self.log.exception("Closing remote app failed!")

    def _onCastStateChange(self, castState: CastState) -> None:
        self._castState = castState
        self._castEventObserver.notify(event=castState)
