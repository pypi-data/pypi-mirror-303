from __future__ import annotations
import desbordante
import desbordante.dd

__all__ = ["Default", "Split"]

class Split(desbordante.Algorithm):
    """
    Options:
    table: table processed by the algorithm
    difference_table: CSV table containing difference limits for each column
    num_rows: Use only first N rows of the table
    num_columns: Use only first N columns of the table
    """

    def __init__(self) -> None: ...
    def get_dds(self) -> list[desbordante.dd.DD]: ...

Default = Split
