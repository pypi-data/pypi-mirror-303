#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright by: P.J. Grochowski

from collections.abc import Callable, Iterator
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

K = TypeVar('K')
V = TypeVar('V')

Node = dict[K, V]


@dataclass
class _NodePairToUpdate(Generic[K, V]):
    current: Node[K, V]
    extension: Node[K, V]


class DeepUpdateableDict(Node[K, V]):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._nodePairToUpdate: list[_NodePairToUpdate] = []

    def deepWalk(self) -> Iterator[tuple[Node[K, V], K, V]]:
        nodesToWalk: list[Node[K, V]] = [self]
        while len(nodesToWalk) > 0:
            node = nodesToWalk.pop()
            for key, value in node.items():
                if isinstance(value, dict):
                    nodesToWalk.append(value)
                    continue

                yield node, key, value

    def deepReplace(self, atKey: K, mapper: Callable[[V], V]) -> None:
        for node, key, value in self.deepWalk():
            if key == atKey:
                node[key] = mapper(value)

    def deepUpdate(self, other: Node[K, V], extendLists: bool = False) -> None:
        self._nodePairToUpdate.clear()
        self._queueForUpdate(current=self, extension=other)

        while len(self._nodePairToUpdate) > 0:
            nodePair = self._nodePairToUpdate.pop()
            for key in nodePair.extension.keys():
                self._updateNodePairKey(key=key, nodePair=nodePair, extendLists=extendLists)

    def _updateNodePairKey(self, key: Any, nodePair: _NodePairToUpdate, extendLists: bool = False) -> None:
        if key not in nodePair.current:
            nodePair.current[key] = nodePair.extension[key]
            return

        currentValue, extensionValue = nodePair.current[key], nodePair.extension[key]

        if self._areOfSameType(currentValue=currentValue, extensionValue=extensionValue, valueType=dict):
            self._queueForUpdate(current=currentValue, extension=extensionValue)
            return

        if extendLists and self._areOfSameType(currentValue=currentValue, extensionValue=extensionValue, valueType=list):
            currentValue.extend(extensionValue)
            return

        nodePair.current[key] = nodePair.extension[key]

    def _areOfSameType(self, currentValue: Any, extensionValue: Any, valueType: type) -> bool:
        return isinstance(currentValue, valueType) and isinstance(extensionValue, valueType)

    def _queueForUpdate(self, current: Node, extension: Node) -> None:
        self._nodePairToUpdate.append(_NodePairToUpdate(current=current, extension=extension))
