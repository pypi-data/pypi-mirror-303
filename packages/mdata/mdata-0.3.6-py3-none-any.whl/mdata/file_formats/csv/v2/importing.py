from typing import Literal, Union

import pandas as pd

from mdata.core import MDV2
from mdata.file_formats.io_utils import DataSource, use_for_pandas_io
from mdata.file_formats.shared import MDFiles, HeaderFormatLiterals


def read_raw_segments(source: DataSource) -> pd.DataFrame:
    """
    Load and read Machine Data segments dataframe from `source`.
    Supports virtual files, as `DataSource` can be a file path, memoryview, or byte/str buffer.
    """

    with use_for_pandas_io(source) as f:
        df = pd.read_csv(f, parse_dates=False, sep=';')

    from mdata.core.extensions.metadata.feature_typing import FeatureDataType, convert_df
    from mdata.core.v2.shared_defs import SegmentConcepts
    convert_df(df, {SegmentConcepts.Object: FeatureDataType.Categorical, SegmentConcepts.Index: FeatureDataType.Integer,
                    SegmentConcepts.Start: FeatureDataType.Datetime,
                    SegmentConcepts.End: FeatureDataType.Datetime}, inplace=True, copy=False)
    return df


def read_raw_segment_data(source: DataSource) -> pd.DataFrame:
    """
    Load and read Machine Data segmentdata dataframe from `source`.
    Supports virtual files, as `DataSource` can be a file path, memoryview, or byte/str buffer.
    """

    with use_for_pandas_io(source) as f:
        df = pd.read_csv(f, parse_dates=False, low_memory=False, sep=';')

    from mdata.core.v2.shared_defs import SegmentConcepts
    from mdata.core.extensions.metadata.feature_typing import convert_df, FeatureDataType
    convert_df(df, {SegmentConcepts.Object: FeatureDataType.Categorical, SegmentConcepts.Index: FeatureDataType.Integer},
               inplace=True, copy=False)
    return df


def read_machine_data_v2(files: MDFiles, header_format: Union[Literal['infer'], HeaderFormatLiterals] = 'infer',
                         validity_checking=False) -> MDV2:
    from mdata.file_formats.csv.importing import read_raw_machine_data
    raw_md = read_raw_machine_data(files['header'], files['observations'], validity_checking=validity_checking,
                                   header_format=header_format)

    if (sg := files.get('segments')) is not None:
        raw_md.data.segments = read_raw_segments(sg)
    if (sgd := files.get('segment_data')) is not None:
        raw_md.data.segment_data = read_raw_segment_data(sgd)

    from mdata.core.v2 import raw_v2
    return raw_v2.create_machine_data_from_raw(raw_md)
