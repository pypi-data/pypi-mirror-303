from __future__ import annotations
import desbordante
import desbordante.od

__all__ = ["Default", "Fastod", "Order"]

class Fastod(desbordante.Algorithm):
    """
    Options:
    table: table processed by the algorithm
    time_limit: max running time of the algorithm. Pass 0 to remove limit
    """

    def __init__(self) -> None: ...
    def get_asc_ods(self) -> list[desbordante.od.AscCanonicalOD]: ...
    def get_desc_ods(self) -> list[desbordante.od.DescCanonicalOD]: ...
    def get_simple_ods(self) -> list[desbordante.od.SimpleCanonicalOD]: ...

class Order(desbordante.Algorithm):
    """
    Options:
    table: table processed by the algorithm
    """

    def __init__(self) -> None: ...
    def get_list_ods(self) -> list[desbordante.od.ListOD]: ...

Default = Order
