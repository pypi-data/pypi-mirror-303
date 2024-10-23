from __future__ import annotations
from . import algorithms

__all__ = ["ACException", "ACRanges", "algorithms"]

class ACException:
    @property
    def column_pairs(self) -> list[tuple[int, int]]: ...
    @property
    def row_index(self) -> int: ...

class ACRanges:
    @property
    def column_indices(self) -> tuple[int, int]: ...
    @property
    def ranges(self) -> list[tuple[float, float]]: ...
