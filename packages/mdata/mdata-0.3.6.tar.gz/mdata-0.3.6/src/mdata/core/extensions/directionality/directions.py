from __future__ import annotations

from typing import Literal
from enum import Enum
from mdata.core.util import StringEnumeration

CSV_KEY = 'D'
DirectionsShortNames = Literal['I', 'O']
DirectionsLongNames = Literal['in', 'out']


class Directions(StringEnumeration):
    Ingoing: DirectionsShortNames = 'I'
    Outgoing: DirectionsShortNames = 'O'
    csv_tuple_qualifiers = [(CSV_KEY, Ingoing), (CSV_KEY, Outgoing)]
    long_names: dict[DirectionsShortNames, DirectionsLongNames] = {Ingoing: 'in', Outgoing: 'out'}


class Direction(Enum):
    Ingoing = 'I'
    Outgoing = 'O'
