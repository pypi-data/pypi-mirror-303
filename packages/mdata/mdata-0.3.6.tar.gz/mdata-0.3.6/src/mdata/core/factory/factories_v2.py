from __future__ import annotations

from collections.abc import Set, Mapping, Sequence, Collection
from dataclasses import dataclass
from typing import Generic, Optional, Iterable, TypedDict, Required, Callable, Any

import pandas as pd

from . import ObservationSeriesDef
from .base import SpecFac, ContFac, cont_fac_for_cls, spec_fac_for_cls, MDFac, md_fac_for_cls, CombContFac, \
    comb_cont_fac_for_cls
from .factories import Factory, match_def_and_df, _prep_series_container_df
from ..header import Meta
from ..protocols import ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC, MD
from ..raw import FeatureMetadata
from ..shared_defs import Extension, SpecType, only_feature_columns
from ..v2.header_v2 import SegmentSpec, SegmentDataSpec
from ..v2.machine_data_v2 import SegmentSeriesSpec, SegmentsContainer, SegmentDataSeriesSpec, \
    SegmentDataContainer, MachineDataV2
from ..v2.protocols_v2 import SSSpec, SDSSpec, SSContainer, SDSContainer, MachineDataV2Protocol, MDV2, SDSView
from ..v2.raw_v2 import SegmentMetadata
from ..v2.shared_defs import SegmentConcepts, SegmentDataConcepts

s_columns_def = {SegmentConcepts.Object: str, SegmentConcepts.Concept: str,
                 SegmentConcepts.Start: str, SegmentConcepts.End: str,
                 SegmentConcepts.Object + '_col': str,
                 SegmentConcepts.Concept + '_col': str,
                 SegmentConcepts.Start + '_col': str, SegmentConcepts.End + '_col': str}

sd_columns_def = {SegmentDataConcepts.Object: str, SegmentDataConcepts.Concept: str,
                  SegmentDataConcepts.Type: str, SegmentDataConcepts.Object + '_col': str,
                  SegmentDataConcepts.Concept + '_col': str,
                  SegmentDataConcepts.Type + '_col': str}

SColumnsDef = TypedDict('SColumnsDef', s_columns_def)
SDColumnsDef = TypedDict('SDColumnsDef', sd_columns_def)

SegmentsDef = TypedDict('SegmentsDef', {'df': Required[pd.DataFrame],
                                        'segment_metadata': Mapping[str, SegmentMetadata],
                                        'preserve_full_df': bool} | s_columns_def)
SegmentDataDef = TypedDict('SegmentDataDef',
                           {'df': Required[pd.DataFrame], 'feature_metadata': Mapping[str, FeatureMetadata],
                            'feature_columns': Sequence[str]} | sd_columns_def)


def define_segment_data_series_defs_by_groupby(df: pd.DataFrame, key: str | list[str],
                                               func: Callable[[Any, pd.DataFrame], SegmentDataDef] = lambda
                                                       g, g_df: SegmentDataDef(df=g_df)) -> list[SegmentDataDef]:
    return [func(g, df.loc[idx]) for g, idx in df.groupby(by=key).groups.items()]


def prepare_segments_df(df: pd.DataFrame, copy=False, **kwargs: SColumnsDef) -> (
        pd.DataFrame, list[SpecType]):
    df = df.copy() if copy else df

    object_def = match_def_and_df(kwargs, df, SegmentConcepts.Object, 0)
    concept_def = match_def_and_df(kwargs, df, SegmentConcepts.Concept, 1)
    index_def = match_def_and_df(kwargs, df, SegmentConcepts.Index, 2)
    start_def = match_def_and_df(kwargs, df, SegmentConcepts.Start, 3, is_dt_type=True)
    end_def = match_def_and_df(kwargs, df, SegmentConcepts.End, 4, is_dt_type=True)
    assert object_def is not None
    assert concept_def is not None
    assert index_def is not None
    assert start_def is not None
    assert end_def is not None

    if not kwargs.get('preserve_full_df'):
        df = df[SegmentConcepts.base_columns()]

    return df, df[SegmentConcepts.Concept].unique().tolist()


def prepare_segment_data_df(df: pd.DataFrame, copy=False, **kwargs: SDColumnsDef) -> (
        pd.DataFrame, SpecType):
    df = df.copy() if copy else df

    type_def = match_def_and_df(kwargs, df, SegmentDataConcepts.Type, 0)
    object_def = match_def_and_df(kwargs, df, SegmentDataConcepts.Object, 1)
    segment_def = match_def_and_df(kwargs, df, SegmentDataConcepts.Concept, 2)
    index_def = match_def_and_df(kwargs, df, SegmentDataConcepts.Index, 3)
    assert type_def is not None
    assert object_def is not None
    assert segment_def is not None
    assert index_def is not None

    if (fc := kwargs.get('feature_columns')) is not None:
        df = df[SegmentDataConcepts.base_columns() + list(fc)]

    return df, type_def


@dataclass
class ExtendedFactory(Factory[ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC, MD], Generic[
    ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC, MD, SSSpec, SSContainer, SDSSpec, SDSView, SDSContainer, MDV2]):
    _ss_spec_cls: type[SSSpec]
    _ss_cont_cls: type[SSContainer]
    _sds_spec_cls: type[SDSSpec]
    _sds_view_cls: type[SDSView]
    _sds_cont_cls: type[SDSContainer]
    _md_v2_cls: type[MachineDataV2Protocol[
        ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC, SSSpec, SSContainer, SDSSpec, SDSView, SDSContainer]]

    def __post_init__(self):
        super().__post_init__()
        self._ss_spec_factory = spec_fac_for_cls(SegmentSpecFactory, SegmentSpec, self._ss_spec_cls)
        self._sds_spec_factory = spec_fac_for_cls(SegmentDataSpecFactory, SegmentDataSpec, self._sds_spec_cls)
        self._ss_cont_factory = comb_cont_fac_for_cls(SegmentContainerFactory, self._ss_spec_cls, self._ss_cont_cls)
        self._sds_cont_factory = cont_fac_for_cls(SegmentDataContainerFactory, self._sds_spec_cls, self._sds_cont_cls)
        self._md_v2_factory = md_fac_for_cls(MachineDataV2Factory, self._md_v2_cls)

    @property
    def supported_extensions(self) -> Set[Extension]:
        return self._md_v2_cls.supported_extensions

    def make_segment_spec(self, typ: SpecType, base_spec: SegmentSpec) -> SSSpec:
        return self._ss_spec_factory.make(typ, base_spec)

    def make_segment_data_spec(self, typ: SpecType, base_spec: SegmentDataSpec) -> SDSSpec:
        return self._sds_spec_factory.make(typ, base_spec)

    def make_segment_spec_from_data(self, typ: SpecType, df: pd.DataFrame,
                                    extra_metadata: SegmentMetadata) -> SSSpec:
        df = df.loc[df[SegmentConcepts.Concept] == typ]
        from mdata.core.extensions.segments.properties import derive_segments_properties

        defined_props = extra_metadata.get('properties', []) if extra_metadata else []
        props = derive_segments_properties(df, claimed=set(defined_props))

        ss = SegmentSpec(typ, long_name=(extra_metadata.get('long_name', typ) if extra_metadata else typ),
                         properties=props)

        return self.make_segment_spec(typ, ss)

    def make_segment_data_spec_from_data(self, type_name: SpecType, df: pd.DataFrame,
                                         extra_metadata: Mapping[str, FeatureMetadata]) -> SDSSpec:
        features = only_feature_columns(df.columns, SegmentDataConcepts.base_columns())
        base_spec = SegmentDataSpec.from_raw(
            [({f: extra_metadata[f]} if (extra_metadata and f in extra_metadata) else f) for f in features])
        return self.make_segment_data_spec(type_name, base_spec)

    def make_segments_container(self, specs: list[SegmentSeriesSpec], df: pd.DataFrame, copy=False) -> SSContainer:
        return self._ss_cont_factory.make(specs, df.copy() if copy else df)

    def make_segments_container_from_data(self, segments_defs: list[SegmentsDef], copy=False) -> SSContainer:
        dfs, segment_specs = [], []
        for segments_def in segments_defs:
            df, segments_list = prepare_segments_df(copy=copy, **segments_def)
            dfs.append(df)
            segment_specs.extend([
                self.make_segment_spec_from_data(concept, df, extra_metadata=segments_def.get('segment_metadata')) for
                concept
                in segments_list])
        concat_df = pd.concat(dfs, axis='rows', ignore_index=True)
        return self.make_segments_container(segment_specs, concat_df, copy=False)

    def make_segment_data_container(self, spec: SegmentDataSeriesSpec, df: pd.DataFrame, copy=True,
                                    convert_dtypes=False) -> SDSContainer:
        df = _prep_series_container_df(spec, df, copy=copy, convert_dtypes=convert_dtypes)
        return self._sds_cont_factory.make(spec, df)

    def make_segment_data_container_from_data(self, segment_data_def: SegmentDataDef, copy=True,
                                              convert_dtypes=False) -> SDSContainer:
        df, label = prepare_segment_data_df(copy=copy, **segment_data_def)
        spec = self.make_segment_data_spec_from_data(label, df, extra_metadata=segment_data_def.get('feature_metadata'))
        return self.make_segment_data_container(spec, df, copy=False, convert_dtypes=convert_dtypes)

    def make_from_data(self, *series_defs: ObservationSeriesDef,
                       meta: Meta = Meta.of(extensions=[Extension.Metadata, Extension.Segments]), sort_by_time=True,
                       copy_dfs=True,
                       convert_dtypes=False, lazy=False, segments_defs: list[SegmentsDef] = None,
                       segment_data_defs: Collection[SegmentDataDef] = ()) -> MachineDataV2Protocol[
        ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC, SSSpec, SSContainer, SDSSpec, SDSView, SDSContainer]:

        md_v1 = super().make_from_data(*series_defs, sort_by_time=sort_by_time, copy_dfs=copy_dfs,
                                       convert_dtypes=convert_dtypes, lazy=True, meta=meta)

        segments = None
        if segments_defs is not None and len(segments_defs) > 0:
            segments = self.make_segments_container_from_data(segments_defs, copy=copy_dfs)

        segment_data = []
        if segment_data_defs is not None and len(segment_data_defs) > 0:
            segment_data = [
                self.make_segment_data_container_from_data(seg_data_def, copy=copy_dfs, convert_dtypes=convert_dtypes)
                for
                seg_data_def in segment_data_defs]

        return self.make(meta=meta, events=md_v1.event_series.values(), measurements=md_v1.measurement_series.values(),
                         segments=segments, segment_data=segment_data,
                         sort_by_time=sort_by_time, lazy=lazy)

    def make(self, meta: Meta = Meta(), events: Iterable[ETSC] = (), measurements: Iterable[MTSC] = (),
             index_frame: pd.DataFrame = None,
             lazy=True,
             segments: Optional[SSContainer] = None, segment_data: Iterable[SDSContainer] = (),
             **kwargs) -> \
            MachineDataV2Protocol[
                ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC, SSSpec, SSContainer, SDSSpec, SDSView, SDSContainer]:
        return self._md_v2_factory.make(meta=meta, events=events, measurements=measurements, index_frame=index_frame,
                                        lazy=lazy, segments=segments, segment_data=segment_data, **kwargs)


class SegmentSpecFactory(SpecFac[SegmentSpec, SSSpec]):
    constructors = {SegmentSeriesSpec: SegmentSeriesSpec.of}


class SegmentDataSpecFactory(SpecFac[SegmentDataSpec, SDSSpec]):
    constructors = {SegmentDataSpec: SegmentDataSeriesSpec.of}


class SegmentContainerFactory(CombContFac[SSSpec, SSContainer]):
    constructors = {SegmentsContainer: SegmentsContainer.of}


class SegmentDataContainerFactory(ContFac[SDSSpec, SDSContainer]):
    constructors = {SegmentDataContainer: SegmentDataContainer.of}


class MachineDataV2Factory(MDFac[MDV2]):
    constructors = {MachineDataV2: MachineDataV2.of}

    def make(self, meta: Meta, events: Iterable[ETSC], measurements: Iterable[MTSC], index_frame: pd.DataFrame = None,
             lazy=True,
             segments: Optional[SSContainer] = None, segment_data: Iterable[SDSContainer] = (),
             **kwargs) -> MDV2:
        return super().make(meta=meta, events=events, measurements=measurements, index_frame=index_frame,
                            lazy_map_creation=lazy, lazy_index_creation=lazy, segments=segments,
                            segment_data=segment_data, **kwargs)
