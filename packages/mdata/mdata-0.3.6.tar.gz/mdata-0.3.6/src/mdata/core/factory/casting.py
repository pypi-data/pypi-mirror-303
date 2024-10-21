import typing
from collections.abc import Set

from ..base_machine_data import MachineDataV1
from ..shared_defs import Extension
from ..protocols import MD
from ..v2.machine_data_v2 import MachineDataV2

support_levels = {MachineDataV1.supported_extensions: MachineDataV1, MachineDataV2.supported_extensions: MachineDataV2}


def as_base(md: MD) -> MachineDataV1:
    """Explicitly cast Machine Data Instance to `MachineDataV1`. Useful for enabling autocompletion using static
    typechecking."""
    return typing.cast(MachineDataV1, md)

def as_v2(md: MD) -> MachineDataV2:
    """Explicitly cast Machine Data Instance to `MachineDataV2`. Useful for enabling autocompletion using static
    typechecking."""
    return typing.cast(MachineDataV2, md)

def as_supports(md: MD, required: Set[Extension]) -> MachineDataV1 | MachineDataV2:
    min_supporting_type = min((supp for supp in support_levels if supp >= required))
    return typing.cast(min_supporting_type, md)
