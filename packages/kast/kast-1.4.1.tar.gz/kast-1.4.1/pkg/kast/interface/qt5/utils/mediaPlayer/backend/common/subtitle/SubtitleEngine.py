#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import time
from collections.abc import Callable, Iterator
from pathlib import Path
from threading import Event, Thread

import pysubs2
from pysubs2 import SSAEvent
from tunit.unit import Milliseconds, Nanoseconds, Seconds

from kast.interface.qt5.utils.mediaPlayer.MediaPlayerState import MediaPlayerState
from kast.interface.qt5.utils.mediaPlayer.frontend.VideoSurface import VideoSurface
from kast.utils.log.Loggable import Loggable

_SubEvents = list[SSAEvent]
PositionSupplier = Callable[[], Milliseconds]


class SubtitleEngine(Loggable):

    _DEFAULT_STATE: MediaPlayerState = MediaPlayerState.Stopped
    _IDLE_DELAY: Milliseconds = Milliseconds(20)
    _COOLDOWN_DELAY: Nanoseconds = Nanoseconds(1)

    def __init__(
        self,
        surface: VideoSurface,
        positionSupplier: PositionSupplier
    ) -> None:
        self._surface: VideoSurface = surface
        self._positionSupplier: PositionSupplier = positionSupplier

        self._thread: Thread | None = None
        self._subtitleFile: Path | None = None

        self._shutdownEvent: Event = Event()
        self._subtitleFileChangeEvent: Event = Event()
        self._state: MediaPlayerState = self._DEFAULT_STATE

    def getSubtitleFile(self) -> Path | None:
        return self._subtitleFile

    def setSubtitleFile(self, subtitles: Path | None) -> None:
        if subtitles != self._subtitleFile:
            self._subtitleFile = subtitles
            self._subtitleFileChangeEvent.set()

    def init(self) -> None:
        if self._thread is None:
            self._thread = Thread(
                target=self._run,
                name=self.__class__.__name__,
                daemon=True
            )
            self._thread.start()

    def shutdown(self) -> None:
        if self._thread is not None:
            self._shutdownEvent.set()
            self._thread.join()
            self._thread = None

    def setState(self, state: MediaPlayerState) -> None:
        self._state = state

    def _shouldStop(self) -> bool:
        return self._shutdownEvent.is_set() or self._subtitleFileChangeEvent.is_set()

    def _shouldRewind(self) -> bool:
        return self._shouldStop() or self._state in [
            MediaPlayerState.Stopped,
            MediaPlayerState.Seeking,
        ]

    @staticmethod
    def _subEventsToText(subEvents: _SubEvents) -> str:
        return '\n'.join([event.plaintext for event in subEvents])

    @staticmethod
    def _getNextSubEvent(subEventIterator: Iterator[SSAEvent]) -> SSAEvent | None:
        try:
            return next(subEventIterator)

        except StopIteration:
            return None

    def _handleNextSubEvent(self, nexSubEvent: SSAEvent | None, newSubEvents: _SubEvents) -> SSAEvent | None:
        if nexSubEvent is None:
            return None

        position = self._positionSupplier().value
        if position < nexSubEvent.start:
            return nexSubEvent

        if position < nexSubEvent.end:
            newSubEvents.append(nexSubEvent)

        return None

    def _fileWalk(self, subEvents: _SubEvents) -> None:
        try:
            subEventIterator = iter(subEvents)
            nextSubEvent = None
            currentSubEvents: _SubEvents = []
            while not self._shouldRewind():
                time.sleep(self._COOLDOWN_DELAY.toRawUnit(unit=Seconds))

                if self._state != MediaPlayerState.Playing:
                    time.sleep(self._IDLE_DELAY.toRawUnit(unit=Seconds))
                    continue

                position = self._positionSupplier()
                newSubEvents = []
                for currentSubEvent in currentSubEvents:
                    if position < Milliseconds(currentSubEvent.end):
                        newSubEvents.append(currentSubEvent)

                if nextSubEvent is None:
                    nextSubEvent = self._getNextSubEvent(subEventIterator)

                nextSubEvent = self._handleNextSubEvent(nexSubEvent=nextSubEvent, newSubEvents=newSubEvents)

                newText = self._subEventsToText(newSubEvents)
                if newText != self._subEventsToText(currentSubEvents):
                    currentSubEvents = newSubEvents
                    self._surface.setSubtitle(newText)

        finally:
            self._surface.setSubtitle('')

    def _fileLoop(self, subEvents: _SubEvents) -> None:
        try:
            while not self._shouldStop():
                time.sleep(self._COOLDOWN_DELAY.toRawUnit(unit=Seconds))

                self._fileWalk(subEvents=subEvents)

        finally:
            self._subtitleFileChangeEvent.clear()

    def _run(self) -> None:
        self.log.info(f"{self.__class__.__name__} started.")
        try:
            while not self._shutdownEvent.is_set():
                try:
                    time.sleep(self._COOLDOWN_DELAY.toRawUnit(unit=Seconds))

                    if self._subtitleFile is None:
                        time.sleep(self._IDLE_DELAY.toRawUnit(unit=Seconds))
                        continue

                    subtitles = pysubs2.load(str(self._subtitleFile), encoding='utf-8')
                    subtitles.remove_miscellaneous_events()
                    subtitles.sort()

                    self._fileLoop(subEvents=subtitles.events)

                except Exception as ex:
                    self.log.exception(ex)
                    self._subtitleFile = None

        finally:
            self._subtitleFile = None
            self._subtitleFileChangeEvent.clear()
            self._shutdownEvent.clear()
            self.log.info(f"{self.__class__.__name__} stopped.")
