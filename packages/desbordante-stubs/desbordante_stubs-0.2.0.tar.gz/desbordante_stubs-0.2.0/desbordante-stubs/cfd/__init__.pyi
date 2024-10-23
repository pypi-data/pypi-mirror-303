from __future__ import annotations
import desbordante
from . import algorithms

__all__ = ["CFD", "CfdAlgorithm", "Item", "algorithms"]

class CFD:
    def __str__(self) -> str: ...
    @property
    def lhs_items(self) -> list[Item]: ...
    @property
    def rhs_item(self) -> Item: ...

class CfdAlgorithm(desbordante.Algorithm):
    def get_cfds(self) -> list[CFD]: ...

class Item:
    @property
    def attribute(self) -> int: ...
    @property
    def value(self) -> str | None: ...
