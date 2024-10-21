from __future__ import annotations

import os
from collections.abc import Mapping
from typing import TypedDict, Optional, Literal, Union

import pandas as pd

from mdata.core.util import StringEnumeration
from .io_utils import DataSource, use_string_io, DataSink


class HeaderFileFormats(StringEnumeration):
    CSV: HeaderFormatLiterals = 'csv'
    JSON: DictHeaderFormatLiterals = 'json'
    YAML: DictHeaderFormatLiterals = 'yaml'


def as_ext(header_format: HeaderFormatLiterals) -> str:
    return '.' + header_format


DictHeaderFormatLiterals = Literal['json', 'yaml']
HeaderFormatLiterals = Union[Literal['csv'], DictHeaderFormatLiterals]
DictHeaderFormats = {HeaderFileFormats.JSON, HeaderFileFormats.YAML}


def possibly_replace_observation_df_columns(df: pd.DataFrame) -> pd.DataFrame:
    from mdata.core.raw import gen_feature_column_names
    from mdata.core import ObservationConcepts
    if len(df.columns) >= len(ObservationConcepts.base_columns()):
        if df.columns[0] != ObservationConcepts.Time:  # TODO possibly improve condition here to check for numeric cols
            k = len(df.columns) - len(ObservationConcepts.base_columns())
            df.columns = ObservationConcepts.base_columns() + gen_feature_column_names(k)
    return df


class MDFiles(TypedDict, total=False):
    header: DataSource | DataSink
    observations: DataSource | DataSink
    segments: DataSource | DataSink
    segment_data: DataSource | DataSink


def mk_canon_filenames_v1(base_path, header_format: HeaderFormatLiterals = HeaderFileFormats.CSV) -> MDFiles:
    p, e = os.path.splitext(base_path)
    return MDFiles(header=p + '_header' + as_ext(header_format), observations=p + '_data.csv')


def mk_canon_filenames_v2(base_path=None, header_format: HeaderFormatLiterals = HeaderFileFormats.CSV) -> MDFiles:

    def localize(s):
        if base_path is not None:
            return os.path.join(base_path, s)
        else:
            return s

    return MDFiles(header=localize('header' + as_ext(header_format)), observations=localize('observations.csv'), segments=localize('segments.csv'),
                   segment_data=localize('segment_data.csv'))


def read_csv_lines_from(arg: DataSource) -> list[list[str]]:
    import csv
    with use_string_io(arg, expected_file_ext=as_ext(HeaderFileFormats.CSV), mode='r') as source:
        reader = csv.reader(source, dialect='excel', delimiter=';')
        return [r for r in reader]


def read_yaml_dict_from(arg: DataSource, swallow_exceptions=True) -> Optional[Mapping]:
    import yaml
    from yaml import YAMLError
    try:
        with use_string_io(arg, expected_file_ext=as_ext(HeaderFileFormats.YAML), mode='r') as source:
            return yaml.load(source, yaml.BaseLoader)
    except YAMLError as e:
        if swallow_exceptions:
            return None
        else:
            raise e


def read_json_dict_from(arg: DataSource, swallow_exceptions=True) -> Optional[Mapping]:
    import json
    from json import JSONDecodeError
    try:
        with use_string_io(arg, expected_file_ext=as_ext(HeaderFileFormats.JSON), mode='r') as source:
            return json.load(source)
    except JSONDecodeError as e:
        if swallow_exceptions:
            return None
        else:
            raise e
