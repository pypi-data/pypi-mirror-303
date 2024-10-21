from __future__ import annotations

import io
import os.path
import typing
from typing import Literal, Union, Mapping

import pandas as pd

from mdata.core import raw, ObservationConcepts, MD
from mdata.core.extensions import metadata_ext, directionality_ext, registry
from mdata.core.shared_defs import ObservationKinds
from mdata.core.v2 import raw_v2
from mdata.file_formats.io_utils import DataSource, use_for_pandas_io, FilePath
from ..shared import mk_canon_filenames_v1, possibly_replace_observation_df_columns, HeaderFormatLiterals, \
    HeaderFileFormats
from ...core.v2.shared_defs import SegmentDefinitionTypes


def read_raw_observations(source: DataSource) -> pd.DataFrame:
    """
    Load and read Machine Data observation dataframe from `source`.
    Supports virtual files, as `DataSource` can be a file path, memoryview, or bytes/str buffer.
    """

    with use_for_pandas_io(source) as f:
        df = pd.read_csv(f, parse_dates=False, low_memory=False, sep=';')
    possibly_replace_observation_df_columns(df)
    from mdata.core.extensions.metadata.feature_typing import convert_df, FeatureDataType
    convert_df(df, {ObservationConcepts.Time: FeatureDataType.Datetime}, inplace=True, copy=False)
    return df


def read_raw_header(header_source: DataSource,
                    header_format: Union[Literal['infer'], HeaderFormatLiterals] = 'infer',
                    validity_checking=False) -> raw_v2.RawHeaderSpecV2:
    """
    Load and read Machine Data header from `source`.
    Supports virtual files, as `DataSource` can be a file path, memoryview, or bytes/str buffer.
    """

    if header_format == 'infer' and isinstance(header_source, FilePath):
        header_format = HeaderFileFormats[os.path.splitext(header_source)[1][1:]]

    if header_format not in HeaderFileFormats:
        from mdata.file_formats.validity_checking_utils import UnsupportedHeaderFileFormat
        raise UnsupportedHeaderFileFormat(header_format)

    header_format = typing.cast(HeaderFormatLiterals, header_format)

    if validity_checking:
        def do_file_checks():
            if header_format == HeaderFileFormats.CSV:
                from .checking import check_if_readable_header_definition_file
                check_if_readable_header_definition_file(header_source)
            elif header_format == HeaderFileFormats.JSON:
                from .checking import check_if_readable_header_definition_file_json
                check_if_readable_header_definition_file_json(header_source)
            elif header_format == HeaderFileFormats.YAML:
                from .checking import check_if_readable_header_definition_file_yaml
                check_if_readable_header_definition_file_yaml(header_source)

        if isinstance(header_source, io.IOBase):
            if header_source.seekable():
                do_file_checks()
                header_source.seek(0)
            else:
                print('skipped file validity checking due to working on non-seekable buffer')
        else:
            do_file_checks()

    return read_raw_header_any(header_source, header_format)


def read_raw_machine_data(header_source: DataSource, data_source: DataSource, validity_checking=True,
                          header_format: Union[Literal['infer'], HeaderFormatLiterals] = 'infer') -> raw_v2.RawMD:
    raw_header = read_raw_header(header_source, header_format, validity_checking=validity_checking)

    if validity_checking:
        assert raw_header is not None
        from .checking import check_if_valid_raw_header
        check_if_valid_raw_header(raw_header)

    raw_obs = read_raw_observations(data_source)

    if raw_obs is not None and validity_checking:
        from .checking import check_if_valid_raw_observation_data
        from mdata.file_formats.validity_checking_utils import check_header_data_compatibility
        check_if_valid_raw_observation_data(raw_obs)
        check_header_data_compatibility(raw_header, raw_obs)

    return raw_v2.RawMD(raw_header, raw_v2.DataPartition(observations=raw_obs))


def read_machine_data(header_source: DataSource, data_source: DataSource, validity_checking=True,
                      header_format: Union[Literal['infer'], HeaderFormatLiterals] = 'infer') -> MD:
    """
    Load and read Machine Data instance from `header_source` and `data_source`.
    Supports file paths as well as various byte or str buffers/memoryviews (virtual files).

    :param header_source: `DataSource` for the header file
    :param data_source: `DataSource` for the data file
    :param validity_checking: whether to explicitly check data format validity constraints
    :param header_format: header format to expect. 'infer' is only valid for a path-specified `header_source`.
    :return: a Machine Data instance
    """
    raw_md = read_raw_machine_data(header_source, data_source, validity_checking=validity_checking,
                                   header_format=header_format)

    return raw.create_machine_data_from_raw(raw_md.header, raw_md.data.observations)


def read_machine_data_canonical(base_path, validity_checking=True,
                                header_format: HeaderFormatLiterals = HeaderFileFormats.CSV) -> MD:
    """
    Load and read Machine Data from `base_path` extended with canonical suffixes '_header.[`header_format`]' and '_data.csv' for header and data file respectively.
    See `read_machine_data`.
    """
    md_files = mk_canon_filenames_v1(base_path, header_format=header_format)
    return read_machine_data(md_files['header'], md_files['observations'], validity_checking=validity_checking,
                             header_format=header_format)


def read_raw_header_any(source: DataSource,
                        header_format: HeaderFormatLiterals = HeaderFileFormats.CSV) -> raw_v2.RawHeaderSpecV2:
    """
    Parse header file in `header_format` from `source` into `RawHeaderSpec` dictionary.
    Supports virtual files, as `DataSource` can be a file path, memoryview, or bytes/str buffer.
    """
    if header_format == HeaderFileFormats.CSV:
        return read_raw_header_csv(source)
    elif header_format == HeaderFileFormats.JSON:
        return read_raw_header_json(source)
    elif header_format == HeaderFileFormats.YAML:
        return read_raw_header_yaml(source)


def read_raw_header_json(source: DataSource) -> raw_v2.RawHeaderSpecV2:
    """
    Parse json from `source` into `RawHeaderSpec` dictionary.
    Supports virtual files, as `DataSource` can be a file path, memoryview, or byte/str buffer.
    """
    from ..shared import read_json_dict_from
    return raw_v2.RawHeaderSpecV2(**read_json_dict_from(source))


def read_raw_header_yaml(source: DataSource) -> raw_v2.RawHeaderSpecV2:
    """
    Parse yaml from `source` into `RawHeaderSpec` dictionary.
    Supports virtual files, as `DataSource` can be a file path, memoryview, or byte/str buffer.
    """
    from ..shared import read_yaml_dict_from
    return raw_v2.RawHeaderSpecV2(**read_yaml_dict_from(source))


def read_raw_header_csv(source: DataSource) -> raw_v2.RawHeaderSpecV2:
    """
    Parse csv from `source` into `RawHeaderSpec` dictionary.
    Supports virtual files, as `DataSource` can be a file path, memoryview, or byte/str buffer.
    """

    result = raw_v2.RawHeaderSpecV2(event_specs={}, measurement_specs={})

    def get_datapointspec_dict(row: list[str]):
        subdict = None
        type_spec_key = row.pop(0)
        if type_spec_key == ObservationKinds.E:
            subdict = result['event_specs']
        elif type_spec_key == ObservationKinds.M:
            subdict = result['measurement_specs']
        elif type_spec_key == SegmentDefinitionTypes.SegmentData:
            if 'segment_data_specs' not in result:
                result['segment_data_specs'] = {}
            subdict = result['segment_data_specs']
        return subdict

    def get_segmentspec_list(row: list[str]):
        type_spec_key = row.pop(0)
        if type_spec_key == SegmentDefinitionTypes.Segments:
            if 'segment_specs' not in result:
                result['segment_specs'] = []
            return result['segment_specs']

    def get_directionality_set(row: list[str]):
        type_spec_key = row.pop(0)
        if type_spec_key == directionality_ext.CSV_KEY:
            if 'directionality' not in result:
                result['directionality'] = raw_v2.RawDirectionalitySpecs.empty()
            import typing
            direction_key = typing.cast(directionality_ext.DirectionsShortNames, row.pop(0))
            direction = directionality_ext.Directions.long_names[direction_key]
            return result['directionality'][direction]

    from ..shared import read_csv_lines_from
    for row in read_csv_lines_from(source):
        statement_identifier = row[0]
        if statement_identifier == registry.CSV_KEY:
            row.pop(0)
            result['extensions'] = [e for e in row if e != '']
        elif statement_identifier in {ObservationKinds.E, ObservationKinds.M, SegmentDefinitionTypes.SegmentData}:
            specs = get_datapointspec_dict(row)
            label = row.pop(0)
            features = []
            while len(row) > 1 and (s := row.pop(0)) != '':
                f, dt = s, row.pop(0)
                if dt == '':
                    dt = 'unknown'
                features.append({f: raw.FeatureMetadata(data_type=dt)})
            specs[label] = features
        elif statement_identifier == SegmentDefinitionTypes.Segments:
            relevant_list = get_segmentspec_list(row)
            label = row.pop(0)
            relevant_list.append(label)
        elif statement_identifier == directionality_ext.CSV_KEY:
            relevant_set = get_directionality_set(row)
            label = row.pop(0)
            relevant_set.add(label)
        elif statement_identifier == metadata_ext.CSV_KEY:
            row.pop(0)
            key = row.pop(0)
            if row[0] in {ObservationKinds.E, ObservationKinds.M, SegmentDefinitionTypes.SegmentData}:
                spec_dict = get_datapointspec_dict(row)
                features = spec_dict[row.pop(0)]
                target_feature = row.pop(0)
                value = row.pop(0)
                for j, f_spec in enumerate(features):
                    if type(f_spec) is str and target_feature == f_spec:
                        features[j] = {target_feature: raw.FeatureMetadata(**{key: value})}
                        break
                    elif isinstance(f_spec, Mapping) and target_feature in f_spec:
                        f_spec[target_feature][key] = value
                        break
            elif row[0] == SegmentDefinitionTypes.Segments:
                relevant_list = get_segmentspec_list(row)
                label = row.pop(0)
                i = relevant_list.index(label)
                if i >= 0:
                    if key == 'properties':
                        value = [p for p in row if p != '']
                    else:
                        value = row.pop(0)
                    ss = relevant_list[i]
                    if type(ss) is str and label == ss:
                        relevant_list[i] = {label: raw_v2.SegmentMetadata(**{key: value})}
                    elif isinstance(ss, Mapping) and label in ss:
                        ss[label][key] = value

    return result
