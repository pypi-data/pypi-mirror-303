from __future__ import annotations
from . import algorithms

__all__ = ["Highlight", "algorithms"]

class Highlight:
    @property
    def cluster(self) -> list[int]: ...
    @property
    def most_frequent_rhs_value_proportion(self) -> float: ...
    @property
    def num_distinct_rhs_values(self) -> int: ...
