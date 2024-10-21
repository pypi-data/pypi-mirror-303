from collections.abc import Mapping
from typing import overload

from mdata.core.shared_protocols import SeriesSpecProtocol, BaseSpec
from mdata.core.v2.header_v2 import SegmentSpec
from mdata.core.v2.protocols_v2 import SegmentSeriesSpecProtocol


@overload
def unpack_specs(dic: Mapping[str, SeriesSpecProtocol[BaseSpec]]) -> Mapping[str, BaseSpec]: ...


@overload
def unpack_specs(dic: Mapping[str, SegmentSeriesSpecProtocol]) -> Mapping[str, SegmentSpec]: ...


def unpack_specs(dic: Mapping[str, SeriesSpecProtocol[BaseSpec] | SegmentSeriesSpecProtocol]) -> Mapping[
    str, BaseSpec | SegmentSpec]:
    return {s: spec.base for s, spec in dic.items()}
