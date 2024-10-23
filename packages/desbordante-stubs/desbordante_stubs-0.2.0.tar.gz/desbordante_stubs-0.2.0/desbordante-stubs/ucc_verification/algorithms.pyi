from __future__ import annotations
import desbordante

__all__ = ["Default", "UccVerifier"]

class UccVerifier(desbordante.Algorithm):
    """
    Options:
    table: table processed by the algorithm
    ucc_indices: column indices for UCC verification
    is_null_equal_null: specify whether two NULLs should be considered equal
    """

    def __init__(self) -> None: ...
    def get_clusters_violating_ucc(self) -> list[list[int]]: ...
    def get_error(self) -> float: ...
    def get_num_clusters_violating_ucc(self) -> int: ...
    def get_num_rows_violating_ucc(self) -> int: ...
    def ucc_holds(self) -> bool: ...

Default = UccVerifier
