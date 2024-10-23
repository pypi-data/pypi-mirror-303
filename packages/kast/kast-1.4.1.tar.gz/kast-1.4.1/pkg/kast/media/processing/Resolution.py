#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from __future__ import annotations  # TODO: Remove when support dropped for: Python < ?

from dataclasses import dataclass
from functools import total_ordering


@total_ordering
@dataclass(frozen=True)
class Resolution:
    width: int
    height: int

    def __str__(self) -> str:
        return f"{self.width}{self._sep()}{self.height}"

    def __lt__(self, other: Resolution) -> bool:
        if not isinstance(other, Resolution):
            raise ValueError(f"Cannot compare {Resolution.__name__} with {other.__class__.__name__}!")

        return self.width < other.width or \
            self.height < other.height

    def shrinkToFit(self, boundingSize: Resolution) -> Resolution:
        boundWidthResolution = self._limitWidth(
            resolution=self,
            boundingSize=boundingSize
        )
        return self._limitHeight(
            resolution=boundWidthResolution,
            boundingSize=boundingSize
        )

    @classmethod
    def fromStr(cls, resolutionStr: str) -> Resolution:
        widthStr, heightStr = resolutionStr.split(cls._sep())
        return Resolution(
            width=int(widthStr),
            height=int(heightStr)
        )

    @staticmethod
    def _sep() -> str:
        return 'x'

    @classmethod
    def _limitWidth(cls, resolution: Resolution, boundingSize: Resolution) -> Resolution:
        return resolution if resolution.width < boundingSize.width\
            else Resolution(
                width=boundingSize.width,
                height=cls._adjustDimension(
                    dimToAdjust=resolution.height,
                    dimOther=resolution.width,
                    dimOtherBound=boundingSize.width
                )
        )

    @classmethod
    def _limitHeight(cls, resolution: Resolution, boundingSize: Resolution) -> Resolution:
        return resolution if resolution.height < boundingSize.height\
            else Resolution(
                width=cls._adjustDimension(
                    dimToAdjust=resolution.width,
                    dimOther=resolution.height,
                    dimOtherBound=boundingSize.height
                ),
                height=boundingSize.height
            )

    @staticmethod
    def _adjustDimension(dimToAdjust: int, dimOther: int, dimOtherBound: int) -> int:
        return int(dimToAdjust * (dimOtherBound / dimOther))


FULL_HD = Resolution(1920, 1080)
ULTRA_HD = Resolution(3840, 2160)
