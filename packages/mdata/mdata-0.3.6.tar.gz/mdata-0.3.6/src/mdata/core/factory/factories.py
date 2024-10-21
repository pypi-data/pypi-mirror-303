from __future__ import annotations

import typing
from collections.abc import Sequence, Set
from dataclasses import dataclass
from typing import TypedDict, Required, Callable, Iterable, Generic, Mapping, Any

import pandas as pd

from mdata.core import df_utils
from mdata.core.base_machine_data import EventTimeseriesContainer, MachineDataV1, MeasurementTimeseriesContainer, \
    EventTimeseriesSpec, \
    MeasurementTimeseriesSpec, SeriesSpec
from mdata.core.extensions.metadata import feature_typing
from mdata.core.factory.base import ContFac, SpecFac, spec_fac_for_cls, cont_fac_for_cls, MDFac, md_fac_for_cls
from mdata.core.header import ObservationSpec, Meta
from mdata.core.protocols import TSSpec, ETSC, MTSC, MD, \
    MachineDataProtocol, TSContainer, ETSView, ETSSpec, MTSView, MTSSpec
from mdata.core.raw import create_machine_data_from_raw, RawHeaderSpec, FeatureMetadata
from mdata.core.shared_defs import ObservationKind, ObservationSpecIdentifier, ObservationKinds, \
    ObservationKindValue, ObservationConcepts, only_feature_columns, Extension

md_columns_def = {ObservationConcepts.Object: str, ObservationConcepts.Time: str,
                  ObservationConcepts.Type: str, ObservationConcepts.Time + '_col': str,
                  ObservationConcepts.Object + '_col': str,
                  ObservationConcepts.Kind + '_col': str, ObservationConcepts.Type + '_col': str}
MDColumnsDef = TypedDict('MDColumnsDef', md_columns_def)
ObservationSeriesDef = TypedDict('ObservationSeriesDef',
                                 {'df': Required[pd.DataFrame],
                                  'feature_metadata': Mapping[str, FeatureMetadata],
                                  'feature_columns': Sequence[str]} | md_columns_def,
                                 total=False)


def define_observation_series_defs_by_groupby(df: pd.DataFrame, key: str | list[str],
                                              func: Callable[[Any, pd.DataFrame], ObservationSeriesDef] = lambda
                                                g, g_df: ObservationSeriesDef(df=g_df)) -> list[ObservationSeriesDef]:
    return [func(g, df.loc[idx]) for g, idx in df.groupby(by=key).groups.items()]


def machine_data_from_complete_df(header: RawHeaderSpec, df: pd.DataFrame) -> MachineDataV1:
    return create_machine_data_from_raw(header, df)


def prepare_observations_df(df: pd.DataFrame, copy=False, sort_by_time=False, **kwargs: MDColumnsDef) -> tuple[
    pd.DataFrame, ObservationSpecIdentifier]:
    df = df.copy() if copy else df

    kind_def = match_def_and_df(kwargs, df, ObservationConcepts.Kind, 0)
    type_def = match_def_and_df(kwargs, df, ObservationConcepts.Type, 1)
    object_def = match_def_and_df(kwargs, df, ObservationConcepts.Object, 2)
    time_def = match_def_and_df(kwargs, df, ObservationConcepts.Time, 3,
                                fallback=lambda: df_utils.create_artificial_daterange(df), is_dt_type=True)
    assert kind_def is not None
    assert type_def is not None
    assert object_def is not None
    assert time_def is not None

    if (fc := kwargs.get('feature_columns')) is not None:
        df = df[ObservationConcepts.base_columns() + list(fc)]

    # assert isinstance(kind_def, ObservationTypeValue)
    kind_def = typing.cast(ObservationKindValue, kind_def)

    if sort_by_time:
        df.sort_values(ObservationConcepts.Time, inplace=True)

    return df, (kind_def, type_def)


def match_def_and_df(kwargs, df, concept, col_idx, fallback=None, is_dt_type=False) -> str:
    concept_def = None
    if concept + '_col' in kwargs:
        assert concept not in kwargs
        col = kwargs.get(concept + '_col')
        concept_def = df[col]
        if is_dt_type:
            concept_def = pd.to_datetime(concept_def, format='ISO8601')
    elif concept in kwargs:
        assert concept + '_col' not in kwargs
        concept_def = kwargs.get(concept)
        if concept == is_dt_type and concept_def == 'artificial':
            concept_def = fallback()
    if concept_def is not None:
        if concept not in df.columns:
            df.insert(col_idx, concept, concept_def)
        else:
            df.loc[:, concept] = concept_def
    elif len(df) > 0:
        concept_def = str(df.iloc[0][concept])
        # assert len(df.loc[:, concept].unique()) == 1, f'there may only be a singular {concept} value in the dataframe'
    return concept_def


@dataclass
class Factory(Generic[ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC, MD]):
    ets_spec_cls: type[ETSSpec]
    ets_view_cls: type[ETSView]
    ets_cont_cls: type[ETSC]
    mts_spec_cls: type[MTSSpec]
    mts_view_cls: type[MTSView]
    mts_cont_cls: type[MTSC]
    md_cls: type[MachineDataProtocol[ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC]]

    def __post_init__(self):
        self.ets_spec_factory = spec_fac_for_cls(TimeseriesSpecFactory, ObservationSpec, self.ets_spec_cls,
                                                 observation_kind=ObservationKind.E)
        self.mts_spec_factory = spec_fac_for_cls(TimeseriesSpecFactory, ObservationSpec, self.mts_spec_cls,
                                                 observation_kind=ObservationKind.M)

        self.ets_cont_factory = cont_fac_for_cls(TimeseriesContainerFactory, self.ets_spec_cls, self.ets_cont_cls)
        self.mts_cont_factory = cont_fac_for_cls(TimeseriesContainerFactory, self.mts_spec_cls, self.mts_cont_cls)

        self.md_factory: MDFac[
            MachineDataProtocol[ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC]] = md_fac_for_cls(MachineDataFactory,
                                                                                                  self.md_cls)

    @property
    def supported_extensions(self) -> Set[Extension]:
        return self.md_cls.supported_extensions

    def make_ts_spec(self, spec_id: ObservationSpecIdentifier, base_spec: ObservationSpec) -> ETSSpec | MTSSpec:
        observation_kind, observation_type = spec_id
        match observation_kind:
            case ObservationKinds.E:
                return self.ets_spec_factory.make(observation_type, base_spec)
            case ObservationKinds.M:
                return self.mts_spec_factory.make(observation_type, base_spec)

    def make_ts_spec_from_data(self, spec_id: ObservationSpecIdentifier, df: pd.DataFrame,
                               extra_metadata: Mapping[str, FeatureMetadata]) -> ETSSpec | MTSSpec:
        features = only_feature_columns(df.columns)
        base_spec = ObservationSpec.from_raw(
            [({f: extra_metadata[f]} if (extra_metadata and f in extra_metadata) else f) for f in features])
        return self.make_ts_spec(spec_id, base_spec)

    def make_ts_container(self, ts_spec: ETSSpec | MTSSpec, df: pd.DataFrame, copy=True,
                          convert_dtypes=False) -> ETSC | MTSC:
        df = _prep_series_container_df(ts_spec, df, copy=copy, convert_dtypes=convert_dtypes)
        match ts_spec.observation_kind:
            case ObservationKind.E:
                return self.ets_cont_factory.make(ts_spec, df)
            case ObservationKind.M:
                return self.mts_cont_factory.make(ts_spec, df)

    def make_ts_container_from_data(self, series_def: ObservationSeriesDef, copy=False, convert_dtypes=False,
                                    sort_by_time=False) -> ETSC | MTSC:
        df, spec_id = prepare_observations_df(copy=copy, sort_by_time=sort_by_time, **series_def)
        ts_spec = self.make_ts_spec_from_data(spec_id, df, extra_metadata=series_def.get('feature_metadata'))
        return self.make_ts_container(ts_spec, df, copy=False, convert_dtypes=convert_dtypes)

    def make_from_data(self, *series_defs: ObservationSeriesDef, meta: Meta = Meta(), sort_by_time=True, copy_dfs=True,
                       convert_dtypes=False, lazy=False) -> MachineDataProtocol[
        ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC]:
        events, measurements = [], []
        for sd in series_defs:
            sd: ObservationSeriesDef = sd
            tsc = self.make_ts_container_from_data(sd, copy=copy_dfs, convert_dtypes=convert_dtypes,
                                                   sort_by_time=sort_by_time)
            match tsc.observation_kind:
                case ObservationKind.E:
                    events.append(tsc)
                case ObservationKind.M:
                    measurements.append(tsc)
                case x:
                    print('unhandled observation kind ' + x)

        return self.make(meta=meta, events=events, measurements=measurements, lazy=lazy)

    def make(self, meta: Meta = Meta(), events: Iterable[ETSC] = (), measurements: Iterable[MTSC] = (), lazy=False,
             index_frame: pd.DataFrame = None,
             **kwargs) -> MachineDataProtocol[ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC]:
        return self.md_factory.make(meta=meta, events=events, measurements=measurements, lazy=lazy,
                                    index_frame=index_frame, **kwargs)


def _prep_series_container_df(spec: SeriesSpec, df, copy=True,
                              convert_dtypes=False) -> pd.DataFrame:
    if convert_dtypes:
        df = feature_typing.convert_df(df,
                                       {f.name: f.data_type for f in spec.base},
                                       inplace=True, copy=copy)
    elif copy:
        df = df.copy()
    return df


class TimeseriesSpecFactory(SpecFac[ObservationSpec, TSSpec]):
    constructors = {ObservationKind.E: {EventTimeseriesSpec: EventTimeseriesSpec.of},
                    ObservationKind.M: {MeasurementTimeseriesSpec:
                                            MeasurementTimeseriesSpec.of}}

    def __init__(self, ts_spec_cls: type[TSSpec] = None, observation_kind: ObservationKind = ObservationKind.E) -> None:
        ts_spec_cls = typing.get_args(self.__class__)[1] if ts_spec_cls is None else ts_spec_cls
        if not isinstance(observation_kind, ObservationKind):
            observation_kind = ObservationKind(observation_kind)
        self.constr = self.constructors[observation_kind][ts_spec_cls]
        self.__call__ = self.make


class TimeseriesContainerFactory(ContFac[TSSpec, TSContainer]):
    constructors = {EventTimeseriesContainer: EventTimeseriesContainer.of,
                    MeasurementTimeseriesContainer: MeasurementTimeseriesContainer.of}


class MachineDataFactory(MDFac[MD]):
    constructors = {MachineDataV1: MachineDataV1.of}

    def make(self, meta: Meta, events: Iterable[ETSC], measurements: Iterable[MTSC], index_frame: pd.DataFrame = None,
             lazy=True,
             **kwargs) -> MD:
        return super().make(meta=meta, events=events, measurements=measurements, index_frame=index_frame,
                            lazy_map_creation=lazy, lazy_index_creation=lazy, **kwargs)
