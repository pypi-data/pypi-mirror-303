"""

Contains the types of data supported by Desbordante.

Currently only used as tags for Algorithm.get_option_type

"""

from __future__ import annotations

__all__ = ["ColumnCombination", "Table"]

class ColumnCombination:
    def __str__(self) -> str: ...
    @property
    def column_indices(self) -> list[int]: ...
    @property
    def table_index(self) -> int: ...

class Table:
    pass
