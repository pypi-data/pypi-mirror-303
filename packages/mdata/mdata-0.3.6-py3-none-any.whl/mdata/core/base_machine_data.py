from __future__ import annotations

import itertools
import logging
import typing
from abc import ABC
from collections.abc import Iterable, Collection, Mapping, Set, Iterator
from copy import copy as copy_func
from dataclasses import dataclass
from typing import Generic, Literal, Self, Optional, Any

import numpy as np
import pandas as pd
from immutabledict import immutabledict

from mdata.core.shared_defs import Extension, SeriesSpecMergeException, ConceptsEnum
from .df_utils import derive_categoricals
from .extensions.metadata.feature_typing import FeatureDataType
from .header import Header, ObservationSpec, Meta, FeatureSpec
from .protocols import EventSpecific, MeasurementSpecific, TimeseriesSpecProtocol, TimeseriesViewProtocol, \
    TimeseriesContainerProtocol, MachineDataProtocol, TSView, ETSC, MTSC, \
    ETSView, ETSSpec, MTSView, MTSSpec, TSContainer, MD, TSSpec
from .shared_defs import SeriesFeatureLabel, SeriesFeatureLabels, ObservationKindValue, \
    ObservationKind, SpecType, ObservationSpecIdentifier, EventSpecLabel, MeasurementSpecLabel, \
    ObservationKinds, ObservationConcepts, only_feature_columns
from .shared_protocols import SeriesSpecProtocol, SSpec, SeriesViewProtocol, SView, SeriesContainerProtocol, BaseSpec, \
    Identifier
from .util import mangle_arg_to_set, mangle_arg_with_bool_fallback, mangle_arg_to_tuple, \
    assert_in, StrIndexer, str_indexer_to_pandas


@dataclass(frozen=True, unsafe_hash=True, eq=True)
class SeriesSpec(SeriesSpecProtocol[Identifier, BaseSpec]):
    _type: SpecType
    _base: BaseSpec
    _features: SeriesFeatureLabels

    @classmethod
    def of(cls, label: SpecType, base_spec: BaseSpec) -> Self:
        return cls(label, base_spec, tuple((f.name for f in base_spec)))

    @property
    def type_name(self) -> SpecType:
        return self._type

    @property
    def identifier(self) -> Identifier:
        return self.type_name

    @property
    def base(self) -> BaseSpec:
        return self._base

    @property
    def features(self) -> SeriesFeatureLabels:
        return self._features

    @property
    def feature_count(self) -> int:
        return len(self._features)

    @property
    def long_names(self) -> SeriesFeatureLabels:
        return tuple((f.long_name for f in self.base))

    def __iter__(self) -> Iterator[str]:
        return iter(self.features)

    def __len__(self) -> int:
        return len(self.features)

    def __str__(self) -> str:
        extended_feature_labels = tuple(
            (str(f) if f == ln else f'{f} ({ln})') for f, ln in zip(self.features, self.long_names))
        return f'{self.__class__.__name__}(spec_id={self.identifier}, features={extended_feature_labels})'

    def __repr__(self):
        return str(self)

    def is_mergeable(self, other: Self) -> bool:
        return (self.__class__ == other.__class__) and self.identifier == other.identifier

    def feature_intersection(self, other: Self) -> list[str]:
        return [f for f in self.features if f in set(other.features)]

    def feature_symmetric_difference(self, other: Self) -> tuple[list[str], list[str]]:
        return [f for f in self.features if f not in set(other.features)], [f for f in other.features if
                                                                            f not in set(self.features)]

    def project(self, feature_selection: bool | str | Collection[str]) -> Self:
        feature_selection = mangle_arg_with_bool_fallback(mangle_arg_to_tuple, feature_selection, if_true=self.features)
        assert all(f in self.features for f in feature_selection)
        return self.__class__.of(self.type_name, self._base.__class__.of(*(self.base[f] for f in feature_selection)))

    def merge(self, other: Self) -> Self:
        assert self.is_mergeable(other)
        specs: list[FeatureSpec] = [copy_func(f) for f in self.base.features]
        for fspec in other.base:
            if fspec not in self.base:
                specs.append(copy_func(fspec))
            elif self.base[fspec.name] != fspec:
                print('redefined', self.base, self.base[fspec.name], fspec.name)
                raise SeriesSpecMergeException(
                    f'Feature {fspec.name} is incompatibly defined in {self} and {other}. ({self.base[fspec.name]} != {fspec})')
        return self.__class__.of(self.type_name, self._base.__class__.of(*specs))

    def __copy__(self) -> Self:
        return self.__class__.of(self.type_name, copy_func(self.base))


@dataclass(frozen=True, unsafe_hash=True, eq=True, repr=True)
class TimeseriesSpec(SeriesSpec, TimeseriesSpecProtocol):
    observation_kind: typing.ClassVar[ObservationKind]
    _base: ObservationSpec

    @property
    def kind(self) -> ObservationKindValue:
        return self.observation_kind.value

    @property
    def identifier(self) -> ObservationSpecIdentifier:
        return self.kind, self.type_name

    @property
    def base(self) -> ObservationSpec:
        return self._base


# @dataclass(frozen=True, repr=False)
class EventTimeseriesSpec(TimeseriesSpec, EventSpecific):
    observation_kind = ObservationKind.E


# @dataclass(frozen=True, repr=False)
class MeasurementTimeseriesSpec(TimeseriesSpec, MeasurementSpecific):
    observation_kind = ObservationKind.M


class SeriesView(SeriesViewProtocol[SSpec], Generic[SSpec]):

    def __init__(self, series_spec: SSpec, df: pd.DataFrame, objects: Collection[str] = ()) -> None:
        super().__init__()
        self._series_spec: SSpec = series_spec
        self._df = df
        self._objects = frozenset(objects) if objects is not None else frozenset()

    @property
    def series_spec(self) -> SSpec:
        return self._series_spec

    @property
    def df(self) -> pd.DataFrame:
        return self._df

    def feature_column_view(self, *, add_spec_id_prefix: bool = False, use_long_names: bool = False,
                            **kwargs: Any) -> pd.DataFrame:
        return _feature_column_view(self.series_spec, self.df, include_time_col=False,
                                    include_object_col=False, add_spec_id_prefix=add_spec_id_prefix,
                                    use_long_names=use_long_names)

    @classmethod
    def of(cls, series_spec: SSpec, df: pd.DataFrame, objects: Collection[str] = (), **kwargs) -> Self:
        return cls(series_spec, df, objects)

    @property
    def objects(self) -> Set[str]:
        return self._objects

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(spec={self.series_spec}, #datapoints={len(self.df)}, objects={str(self.objects)})'

    def __repr__(self) -> str:
        return str(self)


class TimeseriesView(SeriesView[TSSpec], TimeseriesViewProtocol[TSSpec], Generic[TSSpec]):

    @property
    def observation_kind(self) -> ObservationKind:
        return self.series_spec.observation_kind

    @property
    def observation_count(self) -> int:
        return len(self.df)

    def feature_column_view(self, *, add_spec_id_prefix: bool = False,
                            use_long_names: bool = False, include_time_col: bool = True,
                            include_object_col: bool = False,
                            **kwargs) -> pd.DataFrame:
        return _feature_column_view(self.series_spec, self.df, include_time_col=include_time_col,
                                    include_object_col=include_object_col, add_spec_id_prefix=add_spec_id_prefix,
                                    use_long_names=use_long_names)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(spec={self.series_spec}, #observations={len(self.df)}, objects={str(self.objects)})'


class EventTimeseriesView(TimeseriesView[EventTimeseriesSpec]):

    def __init__(self, series_spec: EventTimeseriesSpec, df: pd.DataFrame, objects: Collection[str] = ()) -> None:
        super().__init__(series_spec, df, objects)


class MeasurementTimeseriesView(TimeseriesView[MeasurementTimeseriesSpec]):

    def __init__(self, series_spec: MeasurementTimeseriesSpec, df: pd.DataFrame,
                 objects: Collection[str] = ()) -> None:
        super().__init__(series_spec, df, objects)


def _feature_column_view(spec: TimeseriesSpec, df, include_time_col=True, include_object_col=False,
                         add_spec_id_prefix=False,
                         use_long_names=False):
    cols = list(spec.features)
    if include_object_col:
        cols = [ObservationConcepts.Object] + cols
    if include_time_col:
        cols = [ObservationConcepts.Time] + cols

    view = df.loc[:, cols]

    renaming = {}

    def maybe_prefix(c: str) -> str:
        if add_spec_id_prefix:
            if isinstance(spec.identifier, tuple):
                prefix = '_'.join(spec.identifier)
            else:
                prefix = spec.identifier
            return prefix + '_' + c
        else:
            return c

    if use_long_names | add_spec_id_prefix:
        if use_long_names:
            renaming = {f: maybe_prefix(ln) for f, ln in
                        zip(spec.features, spec.long_names)}
        else:
            renaming = {f: maybe_prefix(f) for f in spec.features}

    return view.rename(renaming, inplace=False, axis='columns') if renaming else view


class AbstractSeriesContainer(SeriesContainerProtocol[SSpec, SView], Generic[SSpec, SView], ABC):
    _s_spec_cls: type[SSpec] = None
    _s_view_cls: type[SView] = None
    _concepts_enum: ConceptsEnum = None

    def __init__(self, series_spec: SSpec, df: pd.DataFrame) -> None:
        super().__init__()
        assert isinstance(series_spec, self._s_spec_cls)
        self._series_spec = series_spec
        self._df = df

        self.__internal_index = None
        self._object_set: frozenset[str] = frozenset()
        self._repopulate_internal_index()

    @property
    def series_spec(self) -> SSpec:
        return self._series_spec

    @series_spec.setter
    def series_spec(self, value: SSpec) -> None:
        self._series_spec = value

    @property
    def df(self) -> pd.DataFrame:
        return self._df

    @df.setter
    def df(self, value: pd.DataFrame) -> None:
        self._df = value

    @classmethod
    def of(cls, series_spec: SSpec, df: pd.DataFrame, **kwargs: Any) -> Self:
        return cls(series_spec, df)

    @property
    def objects(self) -> Set[str]:
        return self._object_set

    @property
    def series_count(self) -> int:
        return len(self.objects)

    @property
    def datapoint_count(self) -> int:
        return len(self.df)

    @property
    def _internal_index(self) -> pd.DataFrame:
        if self.__internal_index is None:
            self._repopulate_internal_index()
        return self.__internal_index

    def __contains__(self, item) -> bool:
        return item in self._object_set

    def __getitem__(self, item: str) -> SView:
        return self.view(item)

    def __len__(self) -> int:
        return len(self.objects)

    def __iter__(self) -> Iterator[SView]:
        return iter(self.view(obj) for obj in self.objects)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(spec={str(self.series_spec)}, #obs={self.datapoint_count}, #objects={len(self.objects)})'

    def __repr__(self) -> str:
        return str(self)

    def __copy__(self) -> Self:
        return self.__class__.of(copy_func(self.series_spec), self.df.copy())

    def feature_column_view(self, *, add_spec_id_prefix=False, use_long_names=False, **kwargs) -> pd.DataFrame:
        return _feature_column_view(self.series_spec, self.df, include_time_col=False,
                                    include_object_col=False, add_spec_id_prefix=add_spec_id_prefix,
                                    use_long_names=use_long_names)

    def view(self, objs: StrIndexer, *args: Any, **kwargs: Any) -> SView:
        objs = str_indexer_to_pandas(objs)
        return self._mk_series_view(self.series_spec, objs)

    def _repopulate_internal_index(self) -> None:
        self.__internal_index = pd.Series(self.df.index, index=self.df[ObservationConcepts.Object])
        self._object_set: frozenset[str] = frozenset(self._internal_index.index.unique())

    def _check_series_features(self) -> bool:
        return set(self.series_spec.features) <= set(self.df.columns)

    def _mk_series_view(self, series_spec, objs) -> SView:
        df = self.df.loc[self._internal_index.loc[objs]]
        if isinstance(df, pd.Series):
            ...
        return self._s_view_cls(series_spec, df, objects=self.objects)

    def _update_series_spec(self, series_spec: SSpec = None, override_declared_types:bool = False) -> None:
        self.series_spec = self._derive_series_spec(override_declared_types) if series_spec is None else series_spec
        assert self._check_series_features()

    def _derive_series_spec(self, override_declared_types: bool = False) -> SSpec:
        current_features = only_feature_columns(self.df.columns, exclusion_list=self._concepts_enum.base_columns())
        from .extensions import metadata

        specs: list[FeatureSpec] = []
        for f in current_features:
            long_name = f
            fdt = FeatureDataType.Infer
            if f in self.series_spec.base:
                fspec: FeatureSpec = self.series_spec.base[f]
                long_name = fspec.long_name
                fdt = fspec.data_type
            if override_declared_types or fdt == FeatureDataType.Infer:
                fdt = metadata.feature_typing.get_type(self.df.loc[:, f])

            specs.append(FeatureSpec(f, long_name, fdt))

        return self._s_spec_cls.of(self.series_spec.type_name, self.series_spec.base.__class__.of(*specs))

    def update_index(self) -> None:
        self._repopulate_internal_index()

    def fit_to_data(self) -> None:
        self._update_series_spec()
        self.update_index()


class AbstractTimeseriesContainer(AbstractSeriesContainer[TSSpec, TSView], TimeseriesContainerProtocol[TSSpec, TSView],
                                  Generic[TSSpec, TSView], ABC):

    @property
    def series_spec(self) -> TSSpec:
        return self._series_spec

    @series_spec.setter
    def series_spec(self, value: TSSpec) -> None:
        self._series_spec = value

    @property
    def observation_kind(self) -> ObservationKind:
        return self.series_spec.observation_kind

    @property
    def observation_count(self) -> int:
        return len(self.df)

    def view(self, objs: StrIndexer, *args: Any, **kwargs: Any) -> TSView:
        return super().view(objs, *args, **kwargs)

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
                assert self.df.loc[:, [ObservationConcepts.Time, ObservationConcepts.Object]].equals(
                    other.df.loc[:, [ObservationConcepts.Time, ObservationConcepts.Object]])
                df = pd.concat([self.df, other.df.loc[:, new_fs]], axis='columns', copy=copy)
                return self.__class__(self.series_spec.merge(other.series_spec), df)
            return self
        elif axis == 'vertical':
            assert self.series_spec == other.series_spec
            df = pd.concat([self.df, other.df], axis='index', ignore_index=True, copy=copy)
            df.sort_values(ObservationConcepts.Time, ignore_index=True, inplace=True)
            return self.__class__(self.series_spec, df)

    def feature_column_view(self, *, add_spec_id_prefix=False,
                            use_long_names=False, include_time_col=True, include_object_col=False,
                            **kwargs: Any) -> pd.DataFrame:
        return _feature_column_view(self.series_spec, self.df, include_time_col=include_time_col,
                                    include_object_col=include_object_col, add_spec_id_prefix=add_spec_id_prefix,
                                    use_long_names=use_long_names)


class EventTimeseriesContainer(AbstractTimeseriesContainer[EventTimeseriesSpec, EventTimeseriesView]):
    _s_spec_cls = EventTimeseriesSpec
    _s_view_cls = EventTimeseriesView
    _concepts_enum = ObservationConcepts


class MeasurementTimeseriesContainer(AbstractTimeseriesContainer[MeasurementTimeseriesSpec, MeasurementTimeseriesView]):
    _s_spec_cls = MeasurementTimeseriesSpec
    _s_view_cls = MeasurementTimeseriesView
    _concepts_enum = ObservationConcepts

class AbstractMachineData(MachineDataProtocol[ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC],
                          Generic[ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC], ABC):
    supported_extensions = frozenset()
    _etsc_cls: type[ETSC] = None
    _mtsc_cls: type[MTSC] = None

    def __init__(self, meta: Meta, events: Iterable[ETSC],
                 measurements: Iterable[MTSC],
                 index_frame: Optional[pd.DataFrame] = None) -> None:

        self._meta: Meta = meta
        self._event_series: Mapping[EventSpecLabel, ETSC] = immutabledict(
            {etc.series_spec.type_name: etc for etc in events})
        self._measurement_series: Mapping[MeasurementSpecLabel, MTSC] = immutabledict(
            {mtc.series_spec.type_name: mtc for mtc in
             measurements})

        for etsc in self.event_series.values():
            assert isinstance(etsc, self._etsc_cls)
        for mtsc in self.measurement_series.values():
            assert isinstance(mtsc, self._mtsc_cls)

        # derived fields/maps
        self._event_specs = None
        self._measurement_specs = None
        self._observation_index: Optional[pd.DataFrame] = index_frame
        self._objects: Optional[Set[str]] = None
        self._series_containers: Set[ETSC | MTSC] = frozenset(
            itertools.chain(self.event_series.values(), self.measurement_series.values()))

    @property
    def meta(self) -> Meta:
        return self._meta

    @property
    def event_series(self) -> Mapping[EventSpecLabel, ETSC]:
        return self._event_series

    @property
    def measurement_series(self) -> Mapping[MeasurementSpecLabel, MTSC]:
        return self._measurement_series

    @classmethod
    def of(cls, meta: Meta = Meta(), events: Iterable[ETSC] = (),
           measurements: Iterable[MTSC] = (), *, lazy_index_creation=False, lazy_map_creation=True,
           **kwargs) -> Self:
        md = cls(meta, events, measurements, **kwargs)
        if not lazy_index_creation and md._observation_index is None:
            md.recalculate_index()
        if not lazy_map_creation:
            md._repopulate_maps()
        return md

    @property
    def header(self) -> Header:
        return Header(self.meta, {e: tspec.base for e, tspec in self.event_specs.items()},
                      {m: tspec.base for m, tspec in self.measurement_specs.items()})

    @property
    def observation_index(self) -> pd.DataFrame:
        if self._observation_index is None:
            self.recalculate_index()
        return self._observation_index

    @observation_index.setter
    def observation_index(self, value: pd.DataFrame):
        self._observation_index = value

    @property
    def objects(self) -> Set[str]:
        if self._objects is None:
            self._repopulate_maps()
        return self._objects

    @property
    def observation_count(self) -> int:
        return len(self.observation_index)

    @property
    def series_containers(self) -> Set[ETSC | MTSC]:
        if self._series_containers is None:
            self._repopulate_maps()
        return self._series_containers

    @property
    def event_specs(self) -> Mapping[EventSpecLabel, ETSSpec]:
        if self._event_specs is None:
            self._repopulate_maps()
        return self._event_specs

    @property
    def measurement_specs(self) -> Mapping[MeasurementSpecLabel, MTSSpec]:
        if self._measurement_specs is None:
            self._repopulate_maps()
        return self._measurement_specs

    def __getitem__(self, item: ObservationSpecIdentifier) -> ETSC | MTSC:
        t, label = item
        match t:
            case ObservationKinds.E:
                return self.event_series[label]
            case ObservationKinds.M:
                return self.measurement_series[label]
            case _:
                raise KeyError

    def __contains__(self, item: object) -> bool:
        if not isinstance(item, tuple):
            return False
        try:
            self[item]
        except KeyError:
            return False
        return True

    def __copy__(self) -> Self:
        return self.__class__.of(copy_func(self.meta), (copy_func(tsc) for tsc in self.event_series.values()),
                                 (copy_func(tsc) for tsc in self.measurement_series.values()),
                                 index_frame=self.observation_index.copy())

    def get_spec(self, identifier: ObservationSpecIdentifier) -> ETSSpec | MTSSpec:
        t, label = identifier
        match t:
            case ObservationKinds.E:
                return self.event_specs[label]
            case ObservationKinds.M:
                return self.measurement_specs[label]
            case _:
                raise KeyError

    def get_events(self, label: EventSpecLabel) -> ETSC:
        return self.event_series[label]

    def get_measurements(self, label: MeasurementSpecLabel) -> MTSC:
        return self.measurement_series[label]

    def view_event_series(self, label: EventSpecLabel, *, objs: StrIndexer = slice(None), **kwargs) -> ETSView:
        """
        Creates a sliced/indexed view of events with spec `label` by objects `objs`.
        See `MachineDataProtocol.view_event_series`.

        :param label: event spec label
        :param objs: selection of objects to be included in the view
        :return: a typed view on the events
        :rtype: implementation of `TimeseriesViewProtocol`
        """
        return self.event_series[label].view(objs=objs, **kwargs)

    def view_measurement_series(self, label: MeasurementSpecLabel, *, objs: StrIndexer = slice(None),
                                **kwargs) -> MTSView:
        """
        Creates a sliced/indexed view of measurements with spec `label` by objects `objs`.
        See `MachineDataProtocol.view_measurement_series`.

        :param label: measurement spec label
        :param objs: selection of objects to be included in the view
        :return: a view on the measurements
        :rtype: implementation of `TimeseriesViewProtocol`
        """
        return self.measurement_series[label].view(objs=objs, **kwargs)

    def recalculate_index(self, override_categorical_types=True, sort_by_time=True, **kwargs):
        self._observation_index = build_shared_index(self.series_containers,
                                                     override_categorical_types=override_categorical_types,
                                                     sort_by_time=sort_by_time, **kwargs)

    def _repopulate_maps(self):
        self._series_containers = frozenset(
            itertools.chain(self.event_series.values(), self.measurement_series.values()))
        self._event_specs = immutabledict({es.series_spec.type_name: es.series_spec for es in
                                           self.event_series.values()})
        self._measurement_specs = immutabledict({ms.series_spec.type_name: ms.series_spec for ms in
                                                 self.measurement_series.values()})
        self._objects = frozenset(self.observation_index.loc[:, ObservationConcepts.Object])

    def fit_to_data(self, ignore_index=False):
        for tsc in self.series_containers:
            # retain only the rows that are referenced in the overall index
            if not ignore_index:
                tsc.df = tsc.df.filter(items=self.observation_index.index, axis=0)
            tsc.fit_to_data()

        if ignore_index:
            self.recalculate_index()
        else:
            old_index = self.observation_index.index
            mask = pd.Series(False, index=old_index)
            for tsc in self.series_containers:
                mask |= old_index.isin(tsc.df.index)
            self._observation_index = self.observation_index[mask]

    def create_joined_observations_df(self, event_labels: Iterable[EventSpecLabel] | bool | None = None,
                                      measurement_labels: Iterable[MeasurementSpecLabel] | bool | None = None,
                                      prefix_columns_to_avoid_collisions=True, copy=False):
        event_keys = self.event_specs.keys()
        esl = mangle_arg_with_bool_fallback(mangle_arg_to_tuple, event_labels,
                                            if_true=event_keys,
                                            rm_duplicates=True, preserve_order=True)
        assert_in(esl, event_keys)
        measurement_keys = self.measurement_specs.keys()
        msl = mangle_arg_with_bool_fallback(mangle_arg_to_tuple, measurement_labels,
                                            if_true=measurement_keys,
                                            rm_duplicates=True, preserve_order=True)
        assert_in(msl, measurement_keys)
        it: Iterable[ETSC | MTSC] = itertools.chain((self.event_series[e] for e in esl),
                                                    (self.measurement_series[m] for m in msl))
        return pd.concat([self.observation_index] + [
            tsc.feature_column_view(add_spec_id_prefix=prefix_columns_to_avoid_collisions, include_time_col=False,
                                    include_object_col=False) for
            tsc in it], axis='columns', copy=copy)

    def create_observation_index_view(self,
                                      kinds: Optional[ObservationKindValue | Iterable[ObservationKindValue]] = None,
                                      objs: Optional[str | Iterable[str]] = None,
                                      types: Optional[SpecType | Iterable[SpecType]] = None) -> pd.DataFrame:

        mask = pd.Series(True, index=self.observation_index.index)
        if isinstance(objs, str):
            mask &= (self.observation_index[ObservationConcepts.Object] == objs)
        elif objs is not None:
            mask &= (self.observation_index[ObservationConcepts.Object].isin(mangle_arg_to_set(objs)))
        if isinstance(types, SpecType):
            mask &= (self.observation_index[ObservationConcepts.Type] == types)
        elif types is not None:
            mask &= (self.observation_index[ObservationConcepts.Type].isin(mangle_arg_to_set(types)))
        if isinstance(kinds, ObservationKindValue):
            mask &= (self.observation_index[ObservationConcepts.Kind] == kinds)
        elif kinds is not None:
            mask &= (self.observation_index[ObservationConcepts.Kind].isin(mangle_arg_to_set(kinds)))

        return self.observation_index.loc[mask]

    def project(self, *,
                event_feature_selection: Mapping[
                    EventSpecLabel, bool | Collection[SeriesFeatureLabel]] = immutabledict(),
                measurement_feature_selection: Mapping[
                    MeasurementSpecLabel, bool | Collection[SeriesFeatureLabel]] = immutabledict(),
                project_underlying_dfs=False, copy_underlying_dfs=False, **kwargs) -> Self:
        def proj(tsc: TimeseriesContainerProtocol, fs):
            tspec = tsc.series_spec
            fs = mangle_arg_with_bool_fallback(mangle_arg_to_tuple, fs, if_true=tspec.features, preserve_order=True)
            spec_proj = tspec.project(fs)
            df_proj = tsc.df.loc[:,
                      ObservationConcepts.base_columns() + list(spec_proj.features)] if project_underlying_dfs else tsc.df
            return spec_proj, (df_proj.copy() if copy_underlying_dfs else df_proj)

        es = [self._etsc_cls(*proj(self.event_series[e], fs)) for e, fs in event_feature_selection.items()]
        ms = [self._mtsc_cls(*proj(self.measurement_series[m], fs)) for m, fs in
              measurement_feature_selection.items()]

        index_view = self.create_observation_index_view(
            types=itertools.chain(event_feature_selection.keys(), measurement_feature_selection.keys()))
        if copy_underlying_dfs:
            index_view = index_view.copy()
        return self.__class__.of(meta=self.meta, events=es, measurements=ms, index_frame=index_view,
                                 lazy_index_creation=True,
                                 lazy_map_creation=True)

    def is_mergeable(self, other: MD) -> bool:
        if self.__class__ != other.__class__:
            return False
        other: Self = other
        for e, et in self.event_specs.items():
            if o_et := other.event_specs.get(e):
                if not et.is_mergeable(o_et):
                    return False
        for m, mt in self.measurement_specs.items():
            if o_mt := other.measurement_specs.get(m):
                if not mt.is_mergeable(o_mt):
                    return False
        return True

    def merge(self, other: Self,
              axis: Literal['horizontal', 'vertical'] = 'horizontal', copy: bool = True,
              suppress_index_creation=False) -> Self:
        assert axis in {'horizontal', 'vertical'}
        assert self.is_mergeable(other)
        es, e_index_change = self._etsc_cls.lifted_merge(self.event_series, other.event_series, axis=axis, copy=copy)
        ms, m_index_change = self._mtsc_cls.lifted_merge(self.measurement_series, other.measurement_series, axis=axis,
                                                         copy=copy)
        meta = self.meta.merge(other.meta)
        if e_index_change | m_index_change:
            kwargs = dict(lazy_index_creation=suppress_index_creation)
        else:
            inherited_index = self.observation_index.copy() if copy else self.observation_index
            kwargs = dict(lazy_index_creation=True, index_frame=inherited_index)
        return self.__class__.of(meta=meta, events=es.values(), measurements=ms.values(), lazy_map_creation=True,
                                 **kwargs)

    def summary(self) -> str:
        first = min(self.observation_index[ObservationConcepts.Time])
        last = max(self.observation_index[ObservationConcepts.Time])
        return f'#Observations: {self.observation_count} between {first} and {last}.' + '\n' + f'#Objects: {len(self.objects)}' + '\n' + f'#Event Specs: {len(self.event_specs)}' + '\n' + f'#Measurement Specs: {len(self.measurement_specs)}'

    def __str__(self) -> str:
        def spec_strings(specs_dict):
            return '\n'.join([f'\t{label}: {", ".join(tspec.features)}' for label, tspec in specs_dict.items()])

        e_specs = spec_strings(self.event_specs)
        m_specs = spec_strings(self.measurement_specs)
        objs = ' ' + ', '.join(map(str, self.objects))
        return 'MachineData {' + '\n' + 'Event Specs:' + (
            '\n' + e_specs if e_specs != "" else "[]") + '\n' + 'Measurement Specs:' + (
            '\n' + m_specs if m_specs != "" else "[]") + '\n' + 'Objects:' + objs + '\n' + f'Observations: {self.observation_count}' + '\n' + '}'

    def __repr__(self) -> str:
        return str(self)


class MachineDataV1(AbstractMachineData[
                        EventTimeseriesSpec, EventTimeseriesView, EventTimeseriesContainer, MeasurementTimeseriesSpec, MeasurementTimeseriesView, MeasurementTimeseriesContainer]):
    supported_extensions = frozenset({Extension.Metadata})
    _etsc_cls = EventTimeseriesContainer
    _mtsc_cls = MeasurementTimeseriesContainer

    @classmethod
    def of(cls, meta: Meta = Meta(), events: Iterable[EventTimeseriesContainer] = (),
           measurements: Iterable[MeasurementTimeseriesContainer] = (), *,
           lazy_index_creation=True,
           lazy_map_creation=True, **kwargs) -> Self:
        return super().of(meta, events, measurements, lazy_index_creation=lazy_index_creation,
                          lazy_map_creation=lazy_map_creation, **kwargs)

    # def merge(self, other: BaseMachineData, axis: Literal['horizontal', 'vertical'] = 'horizontal',
    #          copy: bool = True, suppress_index_creation=False) -> BaseMachineData:
    #    return super().merge(other, axis, copy=copy, suppress_index_creation=suppress_index_creation)


def build_shared_index(series: Iterable[TSContainer], index_cols=None,
                       override_categorical_types=True,
                       sort_by_time=False) -> pd.DataFrame:
    if index_cols is None:
        index_cols = ObservationConcepts.base_columns()
    series = list(series)
    if len(series) == 0:
        return pd.DataFrame([], columns=index_cols)

    lengths = [len(tsc.df) for tsc in series]
    orig_idx_ranges = np.empty(len(lengths) + 1, dtype=int)
    np.cumsum(lengths, out=orig_idx_ranges[1:])
    orig_idx_ranges[0] = 0

    frame = pd.concat((tsc.df.loc[:, index_cols] for tsc in series), ignore_index=True, join='inner',
                      copy=True)

    if sort_by_time:
        sorted_idx = np.argsort(frame[ObservationConcepts.Time].values)
        frame = frame.iloc[sorted_idx]
        frame.reset_index(drop=True, inplace=True)
        rev = np.empty_like(sorted_idx)
        rev[sorted_idx] = np.arange(len(sorted_idx))
        for tsc, start, end in zip(series, orig_idx_ranges[:-1], orig_idx_ranges[1:]):
            tsc.df.index = pd.Index(rev[start:end])
            tsc.update_index()
    else:
        if not frame[ObservationConcepts.Time].is_monotonic_increasing:
            logging.log(logging.WARN, 'machine data index is unsorted')

        for tsc, start, end in zip(series, orig_idx_ranges[:-1], orig_idx_ranges[1:]):
            tsc.df.index = pd.RangeIndex(start, end)
            tsc.update_index()

    cats = derive_categoricals(frame, [ObservationConcepts.Object, ObservationConcepts.Kind, ObservationConcepts.Type])
    frame = frame.astype(cats, copy=False)
    if override_categorical_types:
        for tsc in series:
            tsc.df = tsc.df.astype(cats, copy=False)

    assert frame is not None
    return frame
