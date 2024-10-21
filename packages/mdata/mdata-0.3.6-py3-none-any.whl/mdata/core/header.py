from __future__ import annotations

import typing
from collections.abc import Collection, Iterator, Mapping
from dataclasses import dataclass, field
from typing import Any, TYPE_CHECKING, Optional

from immutabledict import immutabledict

from mdata.core.shared_defs import Extension
from .extensions.metadata.feature_typing import FeatureDataType
from .util import take_first

if TYPE_CHECKING:
    from mdata.core.raw import RawHeaderSpec, RawBaseFeatureSpec, RawMetadataFeatureSpec


@dataclass(frozen=True, eq=True, repr=True)
class FeatureSpec:
    name: str
    long_name: str
    data_type: FeatureDataType = field(default=FeatureDataType.Infer)

    @classmethod
    def from_raw(cls, arg: RawBaseFeatureSpec | RawMetadataFeatureSpec) -> FeatureSpec:
        from .raw import RawMetadataFeatureSpec
        if isinstance(arg, str):
            arg: RawBaseFeatureSpec
            return cls(arg, arg)
        elif isinstance(arg, Mapping):
            f, spec = take_first(arg.items())
            spec: RawMetadataFeatureSpec
            long_name = spec.get('long_name', f)
            data_type = spec.get('data_type', FeatureDataType.Infer)
            if data_type is not None:
                data_type = FeatureDataType(data_type)
            return cls(name=f, long_name=long_name, data_type=data_type)

    def to_raw(self, use_metadata=True) -> RawBaseFeatureSpec | RawMetadataFeatureSpec:
        from .raw import RawMetadataFeatureSpec, FeatureMetadata, RawBaseFeatureSpec
        if use_metadata:
            if self.name == self.long_name and self.data_type is FeatureDataType.Infer:
                return RawBaseFeatureSpec(self.name)
            else:
                return RawMetadataFeatureSpec(
                    {self.name: FeatureMetadata(long_name=self.long_name, data_type=self.data_type.value)})
        else:
            return RawBaseFeatureSpec(self.name)


@dataclass(frozen=True, eq=True, repr=True, init=True)
class DatapointSpec(Collection):
    features: tuple[FeatureSpec] = field(default_factory=tuple)

    # def __int__(self, *features: FeatureSpec) -> None:
    #     super().__init__()
    #     object.__setattr__(self, 'features', tuple(*features))

    def __contains__(self, item: object) -> bool:
        if type(item) is str:
            return any(f.name == item for f in self.features)
        elif isinstance(item, FeatureSpec):
            return item in self.features

    def __len__(self) -> int:
        return len(self.features)

    def __iter__(self) -> Iterator[FeatureSpec]:
        return iter(self.features)

    def __getitem__(self, item) -> FeatureSpec:
        if type(item) is int:
            return self.features[item]
        elif type(item) is str:
            return take_first((f for f in self if f.name == item))

    @classmethod
    def of(cls, *features: FeatureSpec):
        return cls(tuple(features))

    @classmethod
    def from_raw(cls, arg: list[RawBaseFeatureSpec | RawMetadataFeatureSpec]) -> typing.Self:
        return cls(tuple(FeatureSpec.from_raw(f) for f in arg))

    def to_raw(self, use_metadata=True) -> list[RawBaseFeatureSpec | RawMetadataFeatureSpec]:
        return [f.to_raw(use_metadata=use_metadata) for f in self.features]


@dataclass(frozen=True, eq=True, repr=True, init=True)
class ObservationSpec(DatapointSpec):
    ...


ObservationSpecs = Mapping[str, ObservationSpec]


class NotMergeableException(Exception):
    pass


@dataclass(frozen=True, eq=True, repr=True)
class Meta:
    extensions: frozenset[Extension] = field(default_factory=frozenset)
    metadata: immutabledict[str, Any] = field(default_factory=immutabledict)

    @classmethod
    def of(cls, extensions: Collection[Extension], metadata: Optional[Mapping[str, Any]] = None):
        return cls(frozenset(extensions), immutabledict(metadata) if metadata else immutabledict())

    def is_mergeable(self, other: Meta):
        return len(self.metadata.keys() & other.metadata.keys()) == 0

    def merge(self, b: Meta) -> Meta:
        if not self.is_mergeable(b):
            raise NotMergeableException
        return Meta.of(self.extensions | b.extensions, dict(self.metadata) | dict(b.metadata))


@dataclass(frozen=True, eq=True, repr=True)
class Header:
    meta: Meta = field(default_factory=Meta)
    event_specs: ObservationSpecs = field(default_factory=immutabledict)
    measurement_specs: ObservationSpecs = field(default_factory=immutabledict)

    def lookup_feature(self, kind, type_name, feature) -> FeatureSpec:
        return self.lookup_spec(kind, type_name).features[feature]

    def lookup_spec(self, kind, type_name) -> ObservationSpec:
        from .shared_defs import ObservationKinds
        get_from = None
        if kind == ObservationKinds.E:
            get_from = self.event_specs
        elif kind == ObservationKinds.M:
            get_from = self.measurement_specs
        if get_from is None:
            raise KeyError(f'accessing unknown spec kind {kind}')
        try:
            return get_from[type_name]
        except:
            raise KeyError(f'accessing unknown spec type {type_name} in header {self}')

    @classmethod
    def from_raw(cls, raw_header: RawHeaderSpec) -> Header:
        meta = Meta.of({Extension(e) for e in raw_header.get('extensions', [])}, raw_header.get('metadata', {}))

        def make_obs_specs(mapping):
            return {k: ObservationSpec.from_raw(fs) for k, fs in mapping.items()}

        event_specs = make_obs_specs(raw_header['event_specs'])
        measurement_specs = make_obs_specs(raw_header['measurement_specs'])

        return Header(meta, event_specs, measurement_specs)

    def to_raw(self) -> RawHeaderSpec:
        from .raw import RawHeaderSpec
        use_metadata = Extension.Metadata in self.meta.extensions

        def specs_to_raw(spec_dict: Mapping[str, ObservationSpec]):
            return {s: spec.to_raw(use_metadata=use_metadata) for s, spec in spec_dict.items()}

        rh = RawHeaderSpec(event_specs=specs_to_raw(self.event_specs),
                           measurement_specs=specs_to_raw(self.measurement_specs))

        if len(self.meta.extensions) > 0:
            rh['extensions'] = [e.value for e in self.meta.extensions]
        if use_metadata:
            rh['metadata'] = dict(self.meta.metadata)

        return rh


def create_header_from_raw(raw_header: RawHeaderSpec) -> Header:
    return Header.from_raw(raw_header)


def convert_header_to_raw(header: Header) -> RawHeaderSpec:
    return header.to_raw()
