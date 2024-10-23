from __future__ import annotations
import desbordante
from . import algorithms

__all__ = ["UCC", "UccAlgorithm", "algorithms"]

class UCC:
    def __str__(self) -> str: ...
    @property
    def indices(self) -> list[int]: ...

class UccAlgorithm(desbordante.Algorithm):
    def get_uccs(self) -> list[UCC]: ...
