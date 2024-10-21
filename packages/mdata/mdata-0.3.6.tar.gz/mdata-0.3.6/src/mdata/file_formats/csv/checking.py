import os
from collections import defaultdict
from json import JSONDecodeError

import jsonschema
from yaml import YAMLError

import mdata.file_formats.shared
from mdata.core import raw
from mdata.core.extensions import registry, metadata, segments_ext, directionality_ext
from mdata.core.shared_defs import ObservationKinds, ObservationConcepts
from mdata.file_formats.io_utils import DataSource
from .importing import read_raw_observations, read_machine_data, read_machine_data_canonical
from ..shared import read_json_dict_from
from ..validity_checking_utils import *


def is_valid_canonical_file_pair(base_path):
    try:
        read_machine_data_canonical(base_path, validity_checking=True)
    except ValidityCheckingException:
        return False
    return True


def is_valid_file_pair(header_path, data_path):
    try:
        read_machine_data(header_path, data_path, validity_checking=True)
    except ValidityCheckingException:
        return False
    return True


def check_if_readable_header_definition_file(file: DataSource, do_full_check=True):
    seen = defaultdict(set)
    try:
        lines_from = mdata.file_formats.shared.read_csv_lines_from(file)
    except Exception as e:
        raise MalformedHeaderFileException('Unparseable csv:\n' + str(e))
    if do_full_check:
        for k, row in enumerate(lines_from, start=1):
            if row[0] == ObservationConcepts.Kind and row[1] == ObservationConcepts.Type:
                # skip header if included
                continue

            row_identifier = row[0]
            non_empty_idx = [0]
            if row_identifier in ObservationKinds or row_identifier in {segments_ext.CSV_KEY,
                                                                        segments_ext.CSV_KEY_DATA}:
                label = row[1]
                non_empty_idx.append(1)
                if label in seen[row_identifier]:
                    if row_identifier in ObservationKinds:
                        raise MalformedHeaderFileException(f'Duplicate observation specification in line {k}.')
                    elif row_identifier == segments_ext.CSV_KEY:
                        raise MalformedHeaderFileException(f'Duplicate segment specification in line {k}.')
                    elif row_identifier == segments_ext.CSV_KEY_DATA:
                        raise MalformedHeaderFileException(f'Duplicate segment data specification in line {k}.')
                seen[row_identifier].add(label)
            elif row_identifier == registry.CSV_KEY:
                if True in seen[row_identifier]:
                    raise MalformedHeaderFileException(f'Duplicate extension declaration in line {k}.')
                seen[row_identifier].add(True)
            elif row_identifier == metadata.CSV_KEY:
                non_empty_idx.extend([1, 2, 3, 4, 5])
                spec_type = row[2]
                if spec_type in ObservationKinds or spec_type in {segments_ext.CSV_KEY, segments_ext.CSV_KEY_DATA}:
                    if spec_type == segments_ext.CSV_KEY_DATA and row[1] == 'properties':
                        # is permitted to be empty, i.e., empty list
                        non_empty_idx.pop()
                        e = tuple(row[1:4])
                    else:
                        e = tuple(row[1:5])
                else:
                    raise MalformedHeaderFileException(f'Invalid symbol in metadata declaration in line {k}.')
                if row[3] not in seen[spec_type]:
                    raise MalformedHeaderFileException(f'Metadata declaration for undefined spec in line {k}.')
                if e in seen[row_identifier]:
                    raise MalformedHeaderFileException(f'Duplicate metadata declaration in line {k}.')
                seen[row_identifier].add(e)
            elif row_identifier == directionality_ext.CSV_KEY:
                non_empty_idx.extend([1, 2, 3])
                if row[2] not in directionality_ext.Directions:
                    raise MalformedHeaderFileException(f'Invalid directionality declaration in line {k}.')
                label = (row[1], row[2])
                if label in seen[row_identifier]:
                    raise MalformedHeaderFileException(f'Duplicate directionality declaration in line {k}.')
                seen[row_identifier].add(label)
            else:
                raise MalformedHeaderFileException(f'Invalid specification symbol in first column in line {k}.')
            if any(row[i] == '' for i in non_empty_idx):
                raise MalformedHeaderFileException(f'Incomplete specification line in Line {k}.')
    return True


def check_if_readable_header_definition_file_yaml(file: DataSource, do_full_check=True):
    try:
        header = mdata.file_formats.shared.read_yaml_dict_from(file, swallow_exceptions=False)
        if do_full_check:
            check_if_valid_raw_header(header)
    except YAMLError as e:
        raise MalformedHeaderFileException('Unparseable yaml:\n' + str(e))

    return True


def check_if_readable_header_definition_file_json(file: DataSource, do_full_check=True) -> bool:
    try:
        header = mdata.file_formats.shared.read_json_dict_from(file, swallow_exceptions=False)
        if do_full_check:
            check_if_valid_raw_header(header)
    except JSONDecodeError as e:
        raise MalformedHeaderFileException('Unparseable json:\n' + str(e))
    return True


header_schema = read_json_dict_from(os.path.join(os.path.dirname(__file__), '..', 'header_schema_v2.json'))


def check_if_valid_raw_header(raw_header: raw.RawHeaderSpec):
    try:
        jsonschema.validate(raw_header, header_schema)
    except jsonschema.exceptions.ValidationError as e:
        raise MalformedHeaderFileException('Schema validation failed.\n' + str(e))
    return True


def check_if_valid_data_file(path):
    df = read_raw_observations(path)
    check_if_valid_raw_observation_data(df)
    return True


def check_if_valid_raw_observation_data(df):
    if any(c not in df.columns for c in ObservationConcepts.base_columns()):
        raise MalformedDataFileException(
            f'Data is missing base column(s): {set(ObservationConcepts.base_columns()) - set(df.columns)}.')
    check_time_column(df)
    placeholder_cols = get_placeholder_cols(df)
    to_be_cols = gen_feature_column_names(len(placeholder_cols))
    if any(a != b for a, b in zip(placeholder_cols, to_be_cols)):
        raise MalformedDataFileException('Placeholder feature columns have unexpected labels.')
    return True
