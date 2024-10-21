from __future__ import annotations

from collections.abc import Collection
from typing import TypedDict, Any, TypeAlias, Required

import pandas as pd

from .df_utils import derive_categoricals
from .factory.casting import as_base
from .header import create_header_from_raw, ObservationSpec, convert_header_to_raw
from .protocols import MD
from .shared_defs import ObservationConcepts, ObservationKind
from .shared_protocols import SContainer


def gen_feature_column_names(n):
    return [f'a_{i}' for i in range(1, n + 1)]
def gen_typed_feature_column_names(n):
    res = []
    for i in range(1, n + 1):
        res.extend((f'a_{i}', f'a_dt_{i}'))
    return res

class FeatureMetadata(TypedDict, total=False):
    data_type: str
    long_name: str


RawBaseFeatureSpec: TypeAlias = str
RawMetadataFeatureSpec: TypeAlias = dict[str, FeatureMetadata]
RawDatapointSpecs: TypeAlias = dict[str, list[RawBaseFeatureSpec | RawMetadataFeatureSpec]]
RawObservationSpecs: TypeAlias = RawDatapointSpecs


class RawHeaderSpec(TypedDict, total=False):
    extensions: list[str]
    event_specs: Required[RawObservationSpecs]
    measurement_specs: Required[RawObservationSpecs]
    metadata: dict[str, Any]


def convert_to_raw_header(md: MD) -> RawHeaderSpec:
    return convert_header_to_raw(md.header)


def squash_series_containers(index_frame: pd.DataFrame, series: Collection[SContainer]) -> pd.DataFrame:
    max_features = max(map(lambda sc: len(sc.series_spec), series), default=0)
    # dfs = [pd.DataFrame(tsc.df[base_machine_data_columns + list(tsc.timeseries_type.features)], copy=False) for tsc in
    #       md.iter_all_timeseries()]
    # for df, tsc in zip(dfs, md.iter_all_timeseries()):
    #    df.columns = base_machine_data_columns + gen_feature_column_names(len(tsc.timeseries_type.features))
    # res = md.index_frame.join((df.drop(base_machine_data_columns, axis=1) for df in dfs), how='inner')

    res = pd.DataFrame(index_frame, copy=True)  # .reindex(columns=))
    full_placeholder_col_names = gen_feature_column_names(max_features)
    res[full_placeholder_col_names] = pd.NA
    res.astype({c: 'object' for c in full_placeholder_col_names}, copy=False)

    # res.columns = base_raw_machine_data_columns + gen_feature_column_names(max_features)
    for s_container in series:
        df = s_container.feature_column_view(include_time_col=False)
        cs = gen_feature_column_names(s_container.series_spec.feature_count)
        res.loc[df.index, cs] = df.astype(
            'object').values  # df.loc[:, list(ts_container.timeseries_spec.features)].values

    res.columns = ObservationConcepts.base_columns() + full_placeholder_col_names
    # res = pd.concat(dfs, ignore_index=True, copy=False, verify_integrity=False, join='inner') # TODO check copying

    # res.sort_values(COLUMN_NAME_DICT[MDConcepts.Time], ascending=True, inplace=True)
    return res


def convert_to_raw_observations(md: MD) -> pd.DataFrame:
    md = as_base(md)
    res = squash_series_containers(md.observation_index, md.series_containers)

    # res.sort_values(COLUMN_NAME_DICT[MDConcepts.Time], ascending=True, inplace=True)
    return res


def convert_to_raw_data_legacy(md: MD) -> pd.DataFrame:
    max_features = max(map(lambda tsc: len(tsc.series_spec), md.series_containers))
    rows = []
    for ts_container in md.series_containers:
        tt = ts_container.series_spec
        df = ts_container.df
        for tup in df.itertuples(index=True):
            rows.append(
                [getattr(tup, ObservationConcepts.Time), getattr(tup, ObservationConcepts.Object), tt.kind,
                 tt.type_name] + [getattr(tup, f)
                                  for f in
                                  tt.features if
                                  f in df.columns])
    res = pd.DataFrame(rows, columns=(ObservationConcepts.base_columns() + gen_feature_column_names(max_features)))
    res.sort_values(ObservationConcepts.Time, inplace=True)
    return res


def split_squashed_df_into_ts_series_containers(df: pd.DataFrame, header, factory, sort_by_time=False) -> (pd.DataFrame, list[SContainer]):
    categories = derive_categoricals(df,
                                     [ObservationConcepts.Kind, ObservationConcepts.Type, ObservationConcepts.Object])

    overall = pd.DataFrame(df, columns=ObservationConcepts.base_columns(), copy=True)

    if sort_by_time:
        overall.sort_values(ObservationConcepts.Time, inplace=True, ignore_index=True)

    overall = overall.astype(categories, copy=False)

    series_containers = []
    for group, idx in overall.groupby([ObservationConcepts.Kind, ObservationConcepts.Type],
                                      observed=True).groups.items():
        kind, type_name = group
        spec: ObservationSpec = header.lookup_spec(kind, type_name)
        ts_spec = factory.make_ts_spec((kind, type_name), spec)

        actual_feature_labels = ts_spec.features
        feature_count = len(actual_feature_labels)
        placeholder_feature_labels = gen_feature_column_names(feature_count)
        df_g = pd.concat(
            [overall.loc[idx, ObservationConcepts.base_columns()], df.loc[idx, placeholder_feature_labels]],
            copy=False, axis=1).set_index(idx)
        # relevant_cols = list(base_machine_data_columns) + placeholder_feature_labels
        # df = pd.DataFrame(raw_data.loc[idx, relevant_cols], copy=True)
        # not a good idea in case of duplicates
        # df.set_index('time', inplace=True, verify_integrity=True, drop=False)
        renaming_dict = {old: new for old, new in zip(placeholder_feature_labels, actual_feature_labels)}
        df_g.rename(columns=renaming_dict, inplace=True)

        series_containers.append(factory.make_ts_container(ts_spec, df_g, copy=True, convert_dtypes=True))

    placeholder_cols = list(set(overall.columns).difference(ObservationConcepts.base_columns()))
    overall.drop(columns=placeholder_cols, inplace=True)

    return overall, series_containers

def create_machine_data_from_raw(raw_header: RawHeaderSpec, raw_data: pd.DataFrame, sort_by_time=False) -> MD:
    header = create_header_from_raw(raw_header)

    from .factory import get_factory
    factory = get_factory(header.meta.extensions)

    overall, series_containers = split_squashed_df_into_ts_series_containers(raw_data, header, factory, sort_by_time)

    return factory.make(header.meta,
                        events=(tsc for tsc in series_containers if tsc.observation_kind == ObservationKind.E),
                        measurements=(tsc for tsc in series_containers if tsc.observation_kind == ObservationKind.M),
                        index_frame=overall)
