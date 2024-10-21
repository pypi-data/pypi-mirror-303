import typing
from collections.abc import Collection
from dataclasses import dataclass
from typing import TypedDict, TypeAlias, Optional

import pandas as pd

from mdata.core import MD
from mdata.core.raw import RawHeaderSpec, RawDatapointSpecs, convert_to_raw_observations, \
    gen_feature_column_names, split_squashed_df_into_ts_series_containers
from mdata.core.shared_protocols import SContainer
from mdata.core.v2.header_v2 import SegmentDataSpec, SegmentSpec
from mdata.core.v2.protocols_v2 import SSContainer, SDSContainer
from mdata.core.v2.shared_defs import SegmentPropertyValue, SegmentConcepts, SegmentDefinitionType, SegmentDataConcepts

RawBaseSegmentSpec: TypeAlias = str


class SegmentMetadata(TypedDict, total=False):
    long_name: str
    description: str
    properties: list[SegmentPropertyValue]


RawMetadataSegmentSpec: TypeAlias = dict[str, SegmentMetadata]
RawSegmentSpec: TypeAlias = RawBaseSegmentSpec | RawMetadataSegmentSpec
RawSegmentSpecs: TypeAlias = list[RawSegmentSpec]
RawSegmentDataSpecs: TypeAlias = RawDatapointSpecs


class RawDirectionalitySpecs(TypedDict('RawDirectionalitySpecs', {'in': set[str], 'out': set[str]}, total=True)):
    @classmethod
    def empty(cls):
        return cls(**{'in': set(), 'out': set()})


class RawHeaderSpecV2(RawHeaderSpec, total=False):
    segment_specs: RawSegmentSpecs
    segment_data_specs: RawSegmentDataSpecs
    directionality: RawDirectionalitySpecs


@dataclass(repr=True)
class DataPartition:
    observations: Optional[pd.DataFrame] = None
    segments: Optional[pd.DataFrame] = None
    segment_data: Optional[pd.DataFrame] = None


@dataclass(frozen=True, repr=True, eq=True)
class RawMD:
    header: RawHeaderSpecV2
    data: DataPartition


def convert_to_raw_segments(md: MD) -> pd.DataFrame:
    from mdata.core.factory.casting import as_v2
    md = as_v2(md)
    df = md.segments.df.reset_index()
    return df


def convert_to_raw_segment_data(md: MD) -> pd.DataFrame:
    from mdata.core.factory.casting import as_v2
    md = as_v2(md)
    df = squash_segment_data_series_containers(md.segment_data.values())
    return df


def convert_to_raw_header_v2(md: MD) -> RawHeaderSpecV2:
    from mdata.core.factory.casting import as_v2
    md = as_v2(md)
    return md.header.to_raw()


def convert_to_raw_data(md: MD) -> DataPartition:
    from mdata.core.factory.casting import as_v2
    md = as_v2(md)

    obs_df, seg_df, segdata_df = None, None, None
    if md.observation_count > 0:
        obs_df = convert_to_raw_observations(md)
    if md.segments.segment_instance_count > 0:
        seg_df = convert_to_raw_segments(md)
    if sum(map(lambda sds_cont: sds_cont.segment_data_instance_count, md.segment_data.values())) > 0:
        segdata_df = convert_to_raw_segment_data(md)
    return DataPartition(observations=obs_df, segments=seg_df, segment_data=segdata_df)


def convert_to_raw(md: MD) -> RawMD:
    return RawMD(header=convert_to_raw_header_v2(md), data=convert_to_raw_data(md))


def squash_segment_data_series_containers(series: Collection[SDSContainer]) -> pd.DataFrame:
    max_features = max(map(lambda sc: len(sc.series_spec), series), default=0)
    # dfs = [pd.DataFrame(tsc.df[base_machine_data_columns + list(tsc.timeseries_type.features)], copy=False) for tsc in
    #       md.iter_all_timeseries()]
    # for df, tsc in zip(dfs, md.iter_all_timeseries()):
    #    df.columns = base_machine_data_columns + gen_feature_column_names(len(tsc.timeseries_type.features))
    # res = md.index_frame.join((df.drop(base_machine_data_columns, axis=1) for df in dfs), how='inner')

    full_placeholder_col_names = gen_feature_column_names(max_features)

    dfs = []
    for s_container in series:
        df = pd.DataFrame(s_container.df)
        cs = gen_feature_column_names(s_container.series_spec.feature_count)
        df.columns = SegmentDataConcepts.base_columns() + cs
        dfs.append(df)

    res = pd.concat(dfs, ignore_index=True, copy=True, verify_integrity=False)
    # res.columns = SegmentConcepts.segmentdata_columns + full_placeholder_col_names
    res.astype({c: 'object' for c in full_placeholder_col_names}, copy=False)

    # res.sort_values(COLUMN_NAME_DICT[MDConcepts.Time], ascending=True, inplace=True)
    return res


def split_squashed_df_into_segment_data_series_containers(df: pd.DataFrame, header, factory, sort_by_index=False) -> (
        pd.DataFrame, list[SContainer]):
    from mdata.core.df_utils import derive_categoricals
    from mdata.core.factory import ExtendedFactory
    from mdata.core.v2.machine_data_v2 import SegmentDataSeriesSpec

    factory = typing.cast(ExtendedFactory, factory)

    categories = derive_categoricals(df,
                                     [SegmentDataConcepts.Type, SegmentDataConcepts.Object,
                                      SegmentDataConcepts.Concept])

    overall = pd.DataFrame(df, columns=SegmentDataConcepts.base_columns(), copy=True)

    if sort_by_index:
        overall.sort_values(SegmentConcepts.Index, inplace=True, ignore_index=True)

    overall = overall.astype(categories, copy=False)

    series_containers = []
    for group, idx in overall.groupby([SegmentDataConcepts.Type],
                                      observed=True).groups.items():
        typ = group
        spec: SegmentDataSpec = header.lookup_spec(SegmentDefinitionType.SegmentData, typ)
        sds_spec: SegmentDataSeriesSpec = factory.make_segment_data_spec(typ, spec)

        actual_feature_labels = sds_spec.features
        feature_count = len(actual_feature_labels)
        placeholder_feature_labels = gen_feature_column_names(feature_count)
        df_g = pd.concat(
            [overall.loc[idx, SegmentDataConcepts.base_columns()], df.loc[idx, placeholder_feature_labels]],
            copy=False, axis=1).set_index(idx)
        # relevant_cols = list(base_machine_data_columns) + placeholder_feature_labels
        # df = pd.DataFrame(raw_data.loc[idx, relevant_cols], copy=True)
        # not a good idea in case of duplicates
        # df.set_index('time', inplace=True, verify_integrity=True, drop=False)
        renaming_dict = {old: new for old, new in zip(placeholder_feature_labels, actual_feature_labels)}
        df_g.rename(columns=renaming_dict, inplace=True)

        series_containers.append(factory.make_segment_data_container(sds_spec, df_g, copy=True, convert_dtypes=True))

    placeholder_cols = list(set(overall.columns).difference(SegmentDataConcepts.base_columns()))
    overall.drop(columns=placeholder_cols, inplace=True)

    return overall, series_containers


def gen_segments_container(seg_df, header, factory) -> SSContainer:
    from mdata.core.v2.machine_data_v2 import SegmentSeriesSpec
    segment_names = seg_df[SegmentConcepts.Concept].unique()
    seg_specs = []
    for name in segment_names:
        base_spec: SegmentSpec = header.lookup_spec(SegmentDefinitionType.Segments, name)
        seg_spec: SegmentSeriesSpec = factory.make_segment_spec(name, base_spec)
        seg_specs.append(seg_spec)
    return factory.make_segments_container(seg_specs, seg_df)


def create_machine_data_from_raw(raw_md: RawMD, sort_by_time=False, sort_by_index=False) -> MD:
    from mdata.core.v2 import header_v2
    header = header_v2.create_header_from_raw(raw_md.header)

    from mdata.core.factory import ExtendedFactory, extended_factory
    factory: ExtendedFactory = extended_factory

    overall, series_containers = split_squashed_df_into_ts_series_containers(raw_md.data.observations, header, factory,
                                                                             sort_by_time)

    ss_container = None
    if (seg_df := raw_md.data.segments) is not None:
        ss_container = gen_segments_container(seg_df, header, factory)

    sds_containers = ()
    if (sds_df := raw_md.data.segment_data) is not None:
        _, sds_containers = split_squashed_df_into_segment_data_series_containers(sds_df, header, factory,
                                                                                  sort_by_index=sort_by_index)

    from mdata.core import ObservationKind
    return factory.make(meta=header.meta,
                        events=(tsc for tsc in series_containers if tsc.observation_kind == ObservationKind.E),
                        measurements=(tsc for tsc in series_containers if tsc.observation_kind == ObservationKind.M),
                        index_frame=overall, segments=ss_container, segment_data=sds_containers)
