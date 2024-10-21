from __future__ import annotations

import typing
from collections.abc import Mapping
from dataclasses import dataclass, field

from immutabledict import immutabledict

from mdata.core.header import DatapointSpec, Header
from mdata.core.shared_defs import Extension
from mdata.core.util import take_first
from .shared_defs import SegmentProperty, SegmentDefinitionType

if typing.TYPE_CHECKING:
    from mdata.core.v2.raw_v2 import RawDirectionalitySpecs, RawHeaderSpecV2, RawSegmentSpec, RawBaseSegmentSpec


@dataclass(frozen=True, eq=True, repr=True, init=True)
class SegmentDataSpec(DatapointSpec):
    ...


@dataclass(frozen=True, eq=True, repr=True, init=True)
class SegmentSpec:
    name: str
    long_name: str
    properties: frozenset[SegmentProperty]

    @classmethod
    def from_raw(cls, arg: RawSegmentSpec) -> typing.Self:
        from .raw_v2 import RawBaseSegmentSpec, RawMetadataSegmentSpec
        if isinstance(arg, str):
            arg: RawBaseSegmentSpec
            return cls(arg, arg, frozenset())
        elif isinstance(arg, Mapping):
            f, spec = take_first(arg.items())
            spec: RawMetadataSegmentSpec
            long_name = spec.get('long_name', f)
            properties = spec.get('properties', [])
            return cls(f, long_name, frozenset((SegmentProperty(p) for p in properties)))

    def to_raw(self, use_metadata=True) -> RawSegmentSpec:
        from .raw_v2 import RawBaseSegmentSpec, RawMetadataSegmentSpec, SegmentMetadata
        if use_metadata:
            if self.name == self.long_name and len(self.properties) == 0:
                return RawBaseSegmentSpec(self.name)
            else:
                return RawMetadataSegmentSpec(
                    {self.name: SegmentMetadata(long_name=self.long_name,
                                                properties=[p.value for p in self.properties])})
        else:
            return RawBaseSegmentSpec(self.name)


SegmentSpecs = Mapping[str, SegmentSpec]
SegmentDataSpecs = Mapping[str, SegmentDataSpec]


@dataclass(frozen=True, eq=True, repr=True, init=True)
class DirectionalitySpecs:
    input: frozenset[str] = field(default_factory=frozenset)
    output: frozenset[str] = field(default_factory=frozenset)

    @classmethod
    def from_raw(cls, raw: RawDirectionalitySpecs) -> typing.Self:
        return cls(frozenset(raw.get('in', set())), frozenset(raw.get('out', set())))

    def to_raw(self) -> RawDirectionalitySpecs:
        from .raw_v2 import RawDirectionalitySpecs
        return RawDirectionalitySpecs(**{'in': self.input, 'out': self.output})


@dataclass(frozen=True, eq=True, repr=True)
class HeaderV2(Header):
    segment_specs: SegmentSpecs = field(default_factory=immutabledict)
    segment_data_specs: SegmentDataSpecs = field(default_factory=immutabledict)

    def lookup_spec(self, kind, type_name) -> DatapointSpec | SegmentSpec:
        from mdata.core.shared_defs import ObservationKinds
        get_from = None
        if kind == ObservationKinds.E:
            get_from = self.event_specs
        elif kind == ObservationKinds.M:
            get_from = self.measurement_specs
        elif kind == SegmentDefinitionType.Segments:
            get_from = self.segment_specs
        elif kind == SegmentDefinitionType.SegmentData:
            get_from = self.segment_data_specs
        if get_from is None:
            raise KeyError(f'accessing unknown spec kind {kind}')
        try:
            return get_from[type_name]
        except:
            raise KeyError(f'accessing unknown spec type {type_name} in header {self}')

    @classmethod
    def from_raw(cls, raw_header: RawHeaderSpecV2) -> HeaderV2:
        h = super().from_raw(raw_header)

        segment_specs = {ss.name: ss for ss in (SegmentSpec.from_raw(rs) for rs in raw_header.get('segment_specs', []))}
        segment_data_specs = {k: SegmentDataSpec.from_raw(fs) for k, fs in
                              raw_header.get('segment_data_specs', {}).items()}

        return HeaderV2(**h.__dict__, segment_specs=segment_specs, segment_data_specs=segment_data_specs)

    def to_raw(self) -> RawHeaderSpecV2:
        from .raw_v2 import RawHeaderSpecV2
        rh = RawHeaderSpecV2(**super().to_raw())

        use_metadata = Extension.Metadata in self.meta.extensions
        include_segments = Extension.Segments in self.meta.extensions

        if include_segments:
            rh['segment_specs'] = [ss.to_raw(use_metadata=use_metadata) for s, ss in self.segment_specs.items()]
            rh['segment_data_specs'] = {s: spec.to_raw(use_metadata=use_metadata) for s, spec in
                                        self.segment_data_specs.items()}
        return rh


def create_header_from_raw(raw_header: RawHeaderSpecV2) -> HeaderV2:
    return HeaderV2.from_raw(raw_header)


def convert_header_to_raw(header: HeaderV2) -> RawHeaderSpecV2:
    return header.to_raw()
