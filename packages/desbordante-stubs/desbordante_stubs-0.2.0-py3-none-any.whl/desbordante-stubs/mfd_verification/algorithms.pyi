from __future__ import annotations
import desbordante
import desbordante.mfd_verification

__all__ = ["Default", "MetricVerifier"]

class MetricVerifier(desbordante.Algorithm):
    """
    Options:
    table: table processed by the algorithm
    is_null_equal_null: specify whether two NULLs should be considered equal
    lhs_indices: LHS column indices
    metric_algorithm: MFD algorithm to use
    [brute|approx|calipers]
    dist_from_null_is_infinity: specify whether distance from NULL value is infinity (if not, it is 0)
    parameter: metric FD parameter
    q: q-gram length for cosine metric
    rhs_indices: RHS column indices
    metric: metric to use
    [euclidean|levenshtein|cosine]
    """

    def __init__(self) -> None: ...
    def get_highlights(self) -> list[list[desbordante.mfd_verification.Highlight]]: ...
    def mfd_holds(self) -> bool: ...

Default = MetricVerifier
