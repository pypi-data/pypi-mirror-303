from __future__ import annotations
import desbordante
import desbordante.fd_verification

__all__ = ["Default", "FDVerifier"]

class FDVerifier(desbordante.Algorithm):
    """
    Options:
    table: table processed by the algorithm
    is_null_equal_null: specify whether two NULLs should be considered equal
    lhs_indices: LHS column indices
    rhs_indices: RHS column indices
    """

    def __init__(self) -> None: ...
    def fd_holds(self) -> bool: ...
    def get_error(self) -> float: ...
    def get_highlights(self) -> list[desbordante.fd_verification.Highlight]: ...
    def get_num_error_clusters(self) -> int: ...
    def get_num_error_rows(self) -> int: ...

Default = FDVerifier
