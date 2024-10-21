"""
Main module containing Machine Data representation object definitions and implementations.
Exposes `factory` and `extensions` sub modules.
"""

from .shared_defs import ObservationKind, ObservationKinds, ObservationConcepts
from .protocols import MD
from .base_machine_data import MachineDataV1
from .v2 import MachineDataV2, MDV2
from .factory import as_base, as_v2
from . import base_machine_data as bmd
from . import factory
from . import extensions as ext
from . import v2
