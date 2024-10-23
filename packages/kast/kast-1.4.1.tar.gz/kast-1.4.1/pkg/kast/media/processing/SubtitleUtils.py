#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

import fractions
import re
from pathlib import Path
from typing import cast

import av
from pysubs2 import SSAEvent, SSAFile

from kast.media.processing.common import StreamId


class SubtitleException(Exception):
    pass


class SubtitleUtils:

    _TAG_PATTERN: re.Pattern = re.compile('<.*?>')

    @classmethod
    def extract(cls, inputFile: Path, streamId: StreamId, outputFile: Path) -> None:
        cls._extract(inputFile=inputFile, streamId=streamId).save(str(outputFile), encoding='utf-8')

    @staticmethod
    def convert(inputFile: Path, outputFile: Path) -> None:
        SSAFile.load(str(inputFile), encoding='utf-8').save(str(outputFile), encoding='utf-8')

    @classmethod
    def _extract(cls, inputFile: Path, streamId: StreamId) -> SSAFile:
        ssaFile = SSAFile()

        def posToMs(pos: int, timeBase: float | fractions.Fraction) -> int:
            return int(pos * timeBase * 1000)

        def sanitizeText(s: str) -> str:
            return cls._TAG_PATTERN.sub('', s)

        with av.open(str(inputFile)) as fInput:
            inStream = fInput.streams.subtitles[streamId]

            if not inStream.codec_context.codec.text_sub:  # type: ignore
                raise SubtitleException('Extraction supported only for the text based subtitle streams!')

            for packet in fInput.demux(inStream):
                if packet.dts is None:
                    continue

                text = sanitizeText(bytes(packet).decode(encoding='utf-8', errors='ignore'))  # type: ignore
                if not text.strip():
                    continue

                event = SSAEvent()
                event.start = posToMs(cast(int, packet.pts), packet.time_base)
                event.duration = posToMs(cast(int, packet.duration), packet.time_base)
                event.text = text

                ssaFile.append(event)

        return ssaFile
