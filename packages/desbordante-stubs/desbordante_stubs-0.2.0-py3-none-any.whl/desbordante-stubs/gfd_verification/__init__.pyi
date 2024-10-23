from __future__ import annotations
import desbordante
from . import algorithms

__all__ = ["Gfd", "GfdAlgorithm", "algorithms"]

class Gfd:
    def __str__(self) -> str: ...

class GfdAlgorithm(desbordante.Algorithm):
    def get_gfds(self) -> list[Gfd]: ...
