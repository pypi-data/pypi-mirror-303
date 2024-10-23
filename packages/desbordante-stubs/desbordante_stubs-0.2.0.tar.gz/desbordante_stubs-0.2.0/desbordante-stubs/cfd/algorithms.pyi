from __future__ import annotations
import desbordante.cfd

__all__ = ["Default", "FDFirst"]

class FDFirst(desbordante.cfd.CfdAlgorithm):
    """
    Options:
    table: table processed by the algorithm
    columns_number: Number of columns in the part of the dataset if you want to use algo not on the full dataset, but on its part
    cfd_minsup: minimum support value (integer number between 1 and number of tuples in dataset)
    cfd_minconf: cfd minimum confidence value (between 0 and 1)
    tuples_number: Number of tuples in the part of the dataset if you want to use algo not on the full dataset, but on its part
    cfd_max_lhs: cfd max considered LHS size
    cfd_substrategy: CFD lattice traversal strategy to use
    [dfs|bfs]
    """

    def __init__(self) -> None: ...

Default = FDFirst
