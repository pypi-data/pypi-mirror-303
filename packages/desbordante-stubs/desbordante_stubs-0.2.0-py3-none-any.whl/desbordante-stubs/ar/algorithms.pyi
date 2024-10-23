from __future__ import annotations
import desbordante.ar

__all__ = ["Apriori", "Default"]

class Apriori(desbordante.ar.ArAlgorithm):
    """
    Options:
    table: table processed by the algorithm
    has_tid: indicates that the first column contains the transaction IDs
    minconf: minimum confidence value (between 0 and 1)
    input_format: format of the input dataset for AR mining
    [singular|tabular]
    item_column_index: index of the column where an item name is stored
    minsup: minimum support value (between 0 and 1)
    tid_column_index: index of the column where a TID is stored
    """

    def __init__(self) -> None: ...

Default = Apriori
