from __future__ import annotations
import desbordante.gfd_verification

__all__ = ["Default", "EGfdValid", "GfdValid", "NaiveGfdValid"]

class EGfdValid(desbordante.gfd_verification.GfdAlgorithm):
    """
    Options:
    gfd: Path to file with GFD
    graph: Path to dot-file with graph
    """

    def __init__(self) -> None: ...

class GfdValid(desbordante.gfd_verification.GfdAlgorithm):
    """
    Options:
    gfd: Path to file with GFD
    graph: Path to dot-file with graph
    threads: number of threads to use. If 0, then as many threads are used as the hardware can handle concurrently.
    """

    def __init__(self) -> None: ...

class NaiveGfdValid(desbordante.gfd_verification.GfdAlgorithm):
    """
    Options:
    gfd: Path to file with GFD
    graph: Path to dot-file with graph
    """

    def __init__(self) -> None: ...

Default = GfdValid
