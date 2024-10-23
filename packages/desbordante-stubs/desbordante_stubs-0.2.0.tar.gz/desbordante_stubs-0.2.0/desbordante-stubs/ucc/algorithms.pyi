from __future__ import annotations
import desbordante.ucc

__all__ = ["Default", "HyUCC", "PyroUCC"]

class HyUCC(desbordante.ucc.UccAlgorithm):
    """
    Options:
    table: table processed by the algorithm
    is_null_equal_null: specify whether two NULLs should be considered equal
    threads: number of threads to use. If 0, then as many threads are used as the hardware can handle concurrently.
    """

    def __init__(self) -> None: ...

class PyroUCC(desbordante.ucc.UccAlgorithm):
    """
    Options:
    table: table processed by the algorithm
    is_null_equal_null: specify whether two NULLs should be considered equal
    error: error threshold value for Approximate FD algorithms
    max_lhs: max considered LHS size
    seed: RNG seed
    """

    def __init__(self) -> None: ...

Default = HyUCC
