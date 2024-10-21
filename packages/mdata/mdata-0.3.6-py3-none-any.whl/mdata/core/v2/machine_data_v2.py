import typing
from abc import ABC
from copy import copy as copy_func
from dataclasses import dataclass
from typing import Mapping, Set, Generic, Collection, Self, Literal, Any, Iterable, Optional, TypeVar

import numpy as np
import pandas as pd
from immutabledict import immutabledict

from mdata.core import MD
from mdata.core.base_machine_data import SeriesSpec, AbstractSeriesContainer, SeriesView, \
    MachineDataV1, MeasurementTimeseriesContainer, MeasurementTimeseriesView, MeasurementTimeseriesSpec, \
    EventTimeseriesContainer, EventTimeseriesView, EventTimeseriesSpec, AbstractMachineData
from mdata.core.header import Meta, DatapointSpec
from mdata.core.protocols import TSContainer, ETSC, MTSC, MTSSpec, ETSSpec, ETSView, MTSView, MachineDataProtocol
from mdata.core.shared_defs import Extension, SpecType, ObservationConcepts, ExtendedObservationConcepts, \
    MeasurementSpecLabel, EventSpecLabel, SeriesFeatureLabel, ObservationKinds, ObservationKindValue
from mdata.core.shared_protocols import SSpec
from mdata.core.util import StrIndexer, str_indexer_to_pandas
from mdata.core.v2.header_v2 import SegmentDataSpec, SegmentSpec, HeaderV2
from mdata.core.v2.protocols_v2 import SegmentSeriesSpecProtocol, SegmentDataSpecProtocol, \
    SegmentDataSeriesViewProtocol, SDSSpec, SDSView, SegmentDataSeriesContainerProtocol, SegmentSeriesContainerProtocol, \
    MachineDataV2Protocol, SDSContainer, SSContainer, SSSpec
from mdata.core.v2.shared_defs import SegmentSpecType, SegmentConcepts, SegmentProperty, SegmentDataSpecType, \
    ExtendedSegmentConcepts, SpecIdentifier, SegmentDefinitionTypes, SegmentDataConcepts

BMD = TypeVar('BMD', bound=MachineDataProtocol[
    EventTimeseriesSpec, EventTimeseriesView, EventTimeseriesContainer, MeasurementTimeseriesSpec, MeasurementTimeseriesView, MeasurementTimeseriesContainer])


@dataclass(frozen=True, unsafe_hash=True, eq=True, repr=False)
class SegmentDataSeriesSpec(SeriesSpec[SegmentDataSpecType, SegmentDataSpec], SegmentDataSpecProtocol):

    @classmethod
    def of(cls, type_name: SpecType, base_spec: SegmentDataSpec) -> Self:
        return super().of(type_name, base_spec)

    @property
    def identifier(self) -> SegmentDataSpecType:
        return super().identifier

    @property
    def base(self) -> SegmentDataSpec:
        return self._base


@dataclass(frozen=True, unsafe_hash=True, eq=True, repr=False)
class SegmentSeriesSpec(SegmentSeriesSpecProtocol):
    _label: SegmentSpecType
    _base: SegmentSpec

    @classmethod
    def of(cls, label: SegmentSpecType, base: SegmentSpec) -> Self:
        return cls(label, base)

    @property
    def type_name(self) -> SegmentSpecType:
        return self._label

    @property
    def base(self) -> SegmentSpec:
        return self._base

    @property
    def properties(self) -> frozenset[SegmentProperty]:
        return self.base.properties

    @property
    def long_name(self) -> str:
        return self.base.long_name

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(spec_id={self.identifier}, properties={self.properties})'

    def __copy__(self) -> Self:
        return self.__class__.of(self.type_name, copy_func(self.base))


class SegmentDataSeriesView(SeriesView[SDSSpec], SegmentDataSeriesViewProtocol[SDSSpec], Generic[SDSSpec]):

    @property
    def series_spec(self) -> SDSSpec:
        return self._series_spec

    @classmethod
    def of(cls, series_spec: SDSSpec, df: pd.DataFrame, objects: Collection[str] = (), **kwargs: Any) -> Self:
        return super().of(series_spec, df, objects, **kwargs)

    def feature_column_view(self, *, add_spec_id_prefix: bool = False, use_long_names: bool = False,
                            **kwargs: Any) -> pd.DataFrame:
        return super().feature_column_view(add_spec_id_prefix=add_spec_id_prefix, use_long_names=use_long_names,
                                           **kwargs)


class SegmentDataContainer(AbstractSeriesContainer[SDSSpec, SDSView],
                           SegmentDataSeriesContainerProtocol[SDSSpec, SDSView], Generic[
                               SDSSpec, SDSView]):
    _s_spec_cls = SegmentDataSeriesSpec
    _s_view_cls = SegmentDataSeriesView
    _concepts_enum = SegmentDataConcepts

    @property
    def segment_data_instance_count(self) -> int:
        return self.datapoint_count

    def _repopulate_internal_index(self) -> None:
        self.__internal_index = pd.Series(self.df.index, index=self.df[SegmentDataConcepts.Object])
        self._object_set: frozenset[str] = frozenset(self.df.loc[:, SegmentDataConcepts.Object].unique())

    def merge(self, other: Self,
              axis: Literal['horizontal', 'vertical'] = 'vertical', copy: bool = True) -> Self:
        assert axis in {'horizontal', 'vertical'}
        if axis == 'horizontal':
            assert self.series_spec.is_mergeable(other.series_spec)
            ov = self.series_spec.feature_intersection(other.series_spec)
            if ov:
                assert self.df.loc[:, ov].equals(
                    other.df.loc[:, ov])  # np.array_equal(self.df.loc[:, ov].values, other.df.loc[:, ov].values)
            _, new_fs = self.series_spec.feature_symmetric_difference(other.series_spec)
            if new_fs:
                assert self.df.loc[:,
                       [SegmentConcepts.Concept, SegmentConcepts.Index, SegmentConcepts.Object]].equals(
                    other.df.loc[:, [SegmentConcepts.Concept, SegmentConcepts.Index, SegmentConcepts.Object]])
                df = pd.concat([self.df, other.df.loc[:, new_fs]], axis='columns', copy=copy)
                return self.__class__(self.series_spec.merge(other.series_spec), df)
            return self
        elif axis == 'vertical':
            assert self.series_spec == other.series_spec
            df = pd.concat([self.df, other.df], axis='index', ignore_index=True, copy=copy)
            df.sort_values([SegmentConcepts.Concept, SegmentConcepts.Index], ignore_index=True, inplace=True)
            return self.__class__(self.series_spec, df)


class SegmentsContainer(SegmentSeriesContainerProtocol[SegmentSeriesSpec]):

    def __init__(self, segment_specs: Mapping[SegmentSpecType, SegmentSeriesSpec], df: pd.DataFrame) -> None:
        self.df = df.set_index(
            keys=[SegmentConcepts.Object, SegmentConcepts.Concept, SegmentConcepts.Index]).sort_index()
        self._segment_specs = segment_specs
        self._objects = None

    @classmethod
    def empty(cls) -> Self:
        return SegmentsContainer.of({}, pd.DataFrame(
            columns=[SegmentConcepts.Object, SegmentConcepts.Concept, SegmentConcepts.Index]).astype(
            {SegmentConcepts.Object: 'str', SegmentConcepts.Concept: 'str', SegmentConcepts.Index: 'int'}))

    @classmethod
    def of(cls, segment_specs: Iterable[SegmentSeriesSpec] | Mapping[SegmentSpecType, SegmentSeriesSpec],
           df: pd.DataFrame) -> Self:
        if isinstance(segment_specs, list):  # this is unclean
            segment_specs = typing.cast(Iterable[SegmentSeriesSpec], segment_specs)
            segment_specs = {s.type_name: s for s in segment_specs}
        return cls(segment_specs, df)

    @property
    def segment_instance_count(self) -> int:
        return len(self.df)

    @property
    def df(self) -> pd.DataFrame:
        return self._df

    @df.setter
    def df(self, value: pd.DataFrame) -> None:
        self._df = value

    @property
    def segment_specs(self) -> Mapping[SegmentSpecType, SegmentSeriesSpec]:
        return self._segment_specs

    @property
    def objects(self) -> Set[str]:
        if self._objects is None:
            self._objects = frozenset(self.df._get_label_or_level_values(ObservationConcepts.Object))
        return self._objects

    def get_intervals(self, segment_label: SegmentSpecType, objs: StrIndexer) -> pd.DataFrame:
        objs = str_indexer_to_pandas(objs)
        sliced = self.df.loc[pd.IndexSlice[objs, segment_label, :], [SegmentConcepts.Start, SegmentConcepts.End]]

        outer_indices = [SegmentConcepts.Concept]
        if isinstance(objs, str):
            outer_indices = [SegmentConcepts.Object] + outer_indices
        return sliced.droplevel(level=outer_indices, axis=0)

    def view(self, segment_label: SegmentSpecType, objs: StrIndexer = slice(None)) -> pd.DataFrame:
        return self.get_intervals(segment_label, objs=objs)

    def gen_interval_index(self, segment_label: SegmentSpecType, objs: StrIndexer) -> pd.MultiIndex:
        interval_df = self.get_intervals(segment_label, objs)
        return self._create_multi_index(interval_df, groupby_object=not isinstance(objs, str))

    @classmethod
    def _create_multi_index(cls, interval_df: pd.DataFrame, groupby_object=True) -> pd.MultiIndex:
        def make_interval_index(ivs: pd.DataFrame) -> pd.IntervalIndex:
            ivs = ivs.sort_values(SegmentConcepts.Index)
            return pd.IntervalIndex.from_arrays(ivs.loc[:, SegmentConcepts.Start],
                                                ivs.loc[:, SegmentConcepts.End], closed='left')

        if groupby_object:
            interval_index = interval_df.groupby(ObservationConcepts.Object, group_keys=False).apply(
                make_interval_index, raw=True)
        else:
            interval_index = make_interval_index(interval_df)

        return pd.MultiIndex.from_arrays([interval_df.index, interval_index], names=[SegmentConcepts.Index,
                                                                                     ExtendedSegmentConcepts.SegmentInterval])

    def segment_df(self, observations: pd.DataFrame, by: SegmentSpecType, obj: str,
                   return_segment_intervals=False) -> pd.DataFrame | tuple[pd.DataFrame, pd.MultiIndex]:
        # TODO per-object segmentation
        if SegmentProperty.Disjoint in self.segment_specs[by].properties:
            interval_index = self.gen_interval_index(by, obj)
            cut = pd.cut(observations[ObservationConcepts.Time],
                         interval_index.get_level_values(ExtendedSegmentConcepts.SegmentInterval))
            cut = cut.cat.rename_categories(interval_index.get_level_values(SegmentConcepts.Index))
            result = observations.set_index(cut, append=True, verify_integrity=False).swaplevel()
            result.index.rename([SegmentConcepts.Index, ExtendedObservationConcepts.Index], inplace=True)
            return (result, interval_index) if return_segment_intervals else result
        else:
            # many alternatives were considered but pandas simply does not provide a vectorized isin function for intervals
            # interval_index = self.gen_interval_index(by, obj)
            # ivs = interval_index.get_level_values(ExtendedSegmentConcepts.SegmentInterval)
            #
            # for i in ivs:
            #     vfunc = np.vectorize(lambda t: t in i)
            #     print(vfunc(observations[ObservationConcepts.Time]))
            intervals = self.get_intervals(by, obj)
            concat = pd.concat([observations.loc[
                                    (getattr(s, SegmentConcepts.Start) <= observations[ObservationConcepts.Time]) & (
                                            observations[ObservationConcepts.Time] < getattr(s,
                                                                                             SegmentConcepts.End))]
                                for s in intervals.itertuples()], axis='rows', keys=intervals.index,
                               verify_integrity=False)
            concat.index.rename([SegmentConcepts.Index, ExtendedObservationConcepts.Index], inplace=True)
            return (concat, self._create_multi_index(interval_df=intervals,
                                                     groupby_object=False)) if return_segment_intervals else concat

    def segment(self, tsc: TSContainer, by: SegmentSpecType, objs: StrIndexer = None) -> TSContainer:
        raise NotImplemented
        intervals = self.get_intervals(by, objs)
        intervals.apply()
        sliced = self.df.loc[pd.IndexSlice[:, by, :], [SegmentConcepts.Start, SegmentConcepts.End]]
        sliced = sliced.droplevel(level=SegmentConcepts.Concept, axis=0)
        sliced.apply(lambda s: pd.IntervalIndex.from_arrays(sliced.iloc[:, 0], sliced.iloc[:, 1]))
        raise NotImplementedError


class AbstractMachineDataV2(MachineDataV2Protocol[
                                EventTimeseriesSpec, EventTimeseriesView, EventTimeseriesContainer, MeasurementTimeseriesSpec, MeasurementTimeseriesView, MeasurementTimeseriesContainer,
                                SSSpec, SSContainer, SDSSpec, SDSView, SDSContainer],
                            Generic[SSSpec, SSContainer, SDSSpec, SDSView, SDSContainer], ABC):
    _md_v1_cls: type[MachineDataV1] = None
    _ssc_cls: type[SSContainer] = None
    _sdsc_cls: type[SDSContainer] = None

    def __init__(self, meta: Meta, events: Iterable[ETSC], measurements: Iterable[MTSC],
                 index_frame: Optional[pd.DataFrame] = None,
                 segments: Optional[SSContainer] = None,
                 segment_data: Iterable[SDSContainer] = ()) -> None:

        # MachineDataProtocol[EventTimeseriesSpec, EventTimeseriesView, EventTimeseriesContainer, MeasurementTimeseriesSpec, MeasurementTimeseriesView, MeasurementTimeseriesContainer]
        self.bmd: MachineDataV1 = self._md_v1_cls.of(meta, events, measurements, index_frame=index_frame)

        self._segments: SSContainer = segments if segments is not None else self._ssc_cls.empty()
        self._segment_data: Mapping[SegmentDataSpecType, SDSContainer] = immutabledict(
            {sdc.series_spec.type_name: sdc for sdc in (segment_data if segment_data is not None else ())})

        assert isinstance(self.segments, self._ssc_cls)
        for sdsc in self.segment_data.values():
            assert isinstance(sdsc, self._sdsc_cls)

        # derived fields/maps
        self._objects: Optional[Set[str]] = None
        self._segment_specs: Optional[Mapping[SegmentSpecType, SSSpec]] = None
        self._segment_data_specs: Optional[Mapping[SegmentDataSpecType, SDSSpec]] = None

    @classmethod
    def of(cls, meta: Meta = Meta(), events: Iterable[ETSC] = (), measurements: Iterable[MTSC] = (), *,
           segments: Optional[SSContainer] = None,
           segment_data: Iterable[SDSContainer] = (),
           **kwargs: Any) -> Self:
        return cls(meta, events, measurements, segments=segments, segment_data=segment_data)

    def _repopulate_maps(self):
        self._segment_data_specs = immutabledict(
            {sdc.series_spec.type_name: sdc.series_spec for sdc in self.segment_data.values()})
        self._segment_specs: Mapping[SegmentDataSpecType, SSSpec] = immutabledict(
            self.segments.segment_specs) if self.segments is not None else immutabledict()
        self._objects = frozenset(self.bmd.objects | set().union(*(sdc.objects for sdc in self.segment_data.values())) | self.segments.objects)

    @property
    def segments(self) -> SSContainer:
        return self._segments

    @property
    def segment_data(self) -> Mapping[SegmentDataSpecType, SDSContainer]:
        return self._segment_data

    @property
    def segment_specs(self) -> Mapping[SegmentSpecType, SSSpec]:
        if self._segment_specs is None:
            self._repopulate_maps()
        return self._segment_specs

    @property
    def segment_data_specs(self) -> Mapping[SegmentSpecType, SDSSpec]:
        if self._segment_data_specs is None:
            self._repopulate_maps()
        return self._segment_data_specs

    @property
    def objects(self) -> Set[str]:
        if self._objects is None:
            self._repopulate_maps()
        return self._objects

    def project(self, *, measurement_feature_selection: Optional[Mapping[
        MeasurementSpecLabel, bool | Collection[SeriesFeatureLabel]]] = None, event_feature_selection: Optional[
        Mapping[EventSpecLabel, bool | Collection[SeriesFeatureLabel]]] = None, project_underlying_dfs=False,
                copy_underlying_dfs=False, segment_data_selection: Optional[Mapping[
                SegmentSpecType, bool | Collection[SeriesFeatureLabel]]] = None, **kwargs) -> Self:
        raise NotImplemented

    def summary(self) -> str:
        summary = self.bmd.summary()
        extra = (f'#Segment Specs: {len(self.segment_specs)}' + '\n'
                 + f'#Segment Data Specs: {len(self.segment_data_specs)}')
        return summary + '\n' + extra

    def __str__(self):
        bmd_string = str(self.bmd)[:-1]
        return (
                'Extended' + bmd_string + f'Segment: {[f"{ss} ({len(self.segments.view(ss))})" for ss in self.segment_specs]}' + '\n'
                + f'Segment Data Specs: {[f"{sds} ({self.segment_data[sds].datapoint_count})" for sds in self.segment_data_specs]}' + '\n' + '}')

    def __repr__(self):
        return str(self)

    @property
    def header(self) -> HeaderV2:
        from .util import unpack_specs
        return HeaderV2(meta=self.meta, event_specs=unpack_specs(self.event_specs), measurement_specs=unpack_specs(self.measurement_specs),
                        segment_specs=unpack_specs(self.segment_specs), segment_data_specs=unpack_specs(self.segment_data_specs))

    def get_spec(self, identifier: SpecIdentifier) -> ETSSpec | MTSSpec | SSSpec | SDSSpec:
        kind, type_name = identifier
        if kind in ObservationKinds:
            kind: ObservationKindValue = kind
            return self.bmd.get_spec((kind, type_name))
        else:
            match kind:
                case SegmentDefinitionTypes.Segments:
                    return self.segment_specs[type_name]
                case SegmentDefinitionTypes.SegmentData:
                    return self.segment_data_specs[type_name]
                case _:
                    raise KeyError

    def fit_to_data(self, ignore_index=False):
        self.bmd.fit_to_data(ignore_index=ignore_index)
        for sdsc in self.segment_data.values():
            sdsc.fit_to_data()

    def is_mergeable(self, other: MD) -> bool:
        if isinstance(other, AbstractMachineData):
            return self.bmd.is_mergeable(other)
        elif isinstance(other, AbstractMachineDataV2):
            for s, ss in self.segment_specs.items():
                if o_ss := other.segment_specs.get(s):
                    if not ss.is_mergable(o_ss):
                        return False
            for sd, sds in self.segment_specs.items():
                if o_sds := other.segment_specs.get(sd):
                    if not sds.is_mergable(o_sds):
                        return False
            return self.bmd.is_mergeable(other.bmd)

    def merge(self, other: Self, axis: Literal['horizontal', 'vertical'] = 'horizontal', copy: bool = True,
              suppress_index_creation=False) -> Self:
        assert axis in {'horizontal', 'vertical'}
        assert self.is_mergeable(other)
        return NotImplemented

    def __copy__(self) -> typing.Self:
        self.bmd.__copy__()
        return self.__class__.of(copy_func(self.meta), (copy_func(tsc) for tsc in self.event_series.values()),
                                 (copy_func(tsc) for tsc in self.measurement_series.values()),
                                 index_frame=self.observation_index.copy(), segments=copy_func(self.segments),
                                 segment_data=(copy_func(sdsc) for sdsc in self.segment_data.values()))

    def __getitem__(self, item: SpecIdentifier) -> ETSC | MTSC | SSContainer | SDSContainer:
        t, label = item
        if t in ObservationKinds:
            t: ObservationKindValue = t
            return self.bmd.__getitem__((t, label))
        else:
            match t:
                case SegmentDefinitionTypes.Segments:
                    return self.segments
                case SegmentDefinitionTypes.SegmentData:
                    return self.segment_data[label]
                case _:
                    raise KeyError

    def __contains__(self, __x: object) -> bool:
        if not isinstance(__x, tuple):
            return False
        try:
            self[__x]
        except KeyError:
            return False
        return True

    ### delegations

    @property
    def meta(self) -> Meta:
        return self.bmd.meta

    @property
    def event_series(self) -> Mapping[EventSpecLabel, EventTimeseriesContainer]:
        return self.bmd.event_series

    @property
    def measurement_series(self) -> Mapping[MeasurementSpecLabel, MTSC]:
        return self.bmd.measurement_series

    @property
    def observation_index(self) -> pd.DataFrame:
        return self.bmd.observation_index

    @property
    def series_containers(self) -> Set[ETSC | MTSC]:
        return self.bmd.series_containers

    @property
    def observation_count(self) -> int:
        return self.bmd.observation_count

    @property
    def event_specs(self) -> Mapping[EventSpecLabel, ETSSpec]:
        return self.bmd.event_specs

    @property
    def measurement_specs(self) -> Mapping[MeasurementSpecLabel, MTSSpec]:
        return self.bmd.measurement_specs

    def get_events(self, label: EventSpecLabel) -> ETSC:
        return self.bmd.get_events(label)

    def get_measurements(self, label: MeasurementSpecLabel) -> MTSC:
        return self.bmd.get_measurements(label)

    def view_event_series(self, label: EventSpecLabel, **kwargs) -> ETSView:
        return self.bmd.view_event_series(label, **kwargs)

    def view_measurement_series(self, label: MeasurementSpecLabel, **kwargs) -> MTSView:
        return self.bmd.view_measurement_series(label, **kwargs)

    def recalculate_index(self, override_categorical_types=True, sort_by_time=True, **kwargs):
        self.bmd.recalculate_index(override_categorical_types=override_categorical_types, sort_by_time=sort_by_time,
                                   **kwargs)

    def create_joined_observations_df(self, event_labels: Iterable[EventSpecLabel] | bool | None = None,
                                      measurement_labels: Iterable[MeasurementSpecLabel] | bool | None = None,
                                      prefix_columns_to_avoid_collisions=True, copy=False) -> pd.DataFrame:
        return self.bmd.create_joined_observations_df(event_labels, measurement_labels,
                                                      prefix_columns_to_avoid_collisions, copy)

    def create_observation_index_view(self,
                                      kinds: Optional[ObservationKindValue | Iterable[ObservationKindValue]] = None,
                                      objs: Optional[str | Iterable[str]] = None,
                                      types: Optional[SpecType | Iterable[SpecType]] = None) -> pd.DataFrame:
        return self.bmd.create_observation_index_view(kinds, objs, types)

    @classmethod
    def lifted_merge(cls, machine_datas: Iterable[MD], axis: Literal['horizontal', 'vertical'] = 'horizontal',
                     copy: bool = True, suppress_index_creation=False) -> MD:
        return cls._md_v1_cls.lifted_merge(machine_datas, axis, copy, suppress_index_creation)


class MachineDataV2(AbstractMachineDataV2[
                        SegmentSpec, SegmentsContainer, SegmentDataSpec, SegmentDataSeriesView, SegmentDataContainer]):
    supported_extensions = frozenset({Extension.Metadata, Extension.Segments})
    _md_v1_cls = MachineDataV1
    _ssc_cls = SegmentsContainer
    _sdsc_cls = SegmentDataContainer

    @classmethod
    def of(cls, meta: Meta = Meta(), events: Iterable[EventTimeseriesContainer] = (), measurements: Iterable[MeasurementTimeseriesContainer] = (), *,
           segments: Optional[SegmentsContainer] = None, segment_data: Iterable[SegmentDataContainer] = (), **kwargs: Any) -> Self:
        return super().of(meta, events, measurements, segments=segments, segment_data=segment_data, **kwargs)
