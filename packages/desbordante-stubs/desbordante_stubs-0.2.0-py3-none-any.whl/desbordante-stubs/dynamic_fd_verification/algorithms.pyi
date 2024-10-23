from __future__ import annotations
import desbordante
import desbordante.fd_verification

__all__ = ["Default", "DynamicFDVerifier"]

class DynamicFDVerifier(desbordante.Algorithm):
    """
    Options:
    table: table processed by the algorithm
    insert: Rows to be inserted into the table using the insert operation
    delete: Rows to be deleted from the table using the delete operation
    update: Rows to be replaced in the table using the update operation
    lhs_indices: LHS column indices
    rhs_indices: RHS column indices
    """

    def __init__(self) -> None: ...
    def fd_holds(self) -> bool: ...
    def get_error(self) -> float: ...
    def get_highlights(self) -> list[desbordante.fd_verification.Highlight]: ...
    def get_num_error_clusters(self) -> int: ...

Default = DynamicFDVerifier
