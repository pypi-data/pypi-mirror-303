import csv
import json
import sys
import typing
from typing import Optional, Any

import pandas as pd
import yaml

from mdata.core import raw, MD, ObservationKinds, ObservationConcepts
from mdata.core.extensions import metadata
from ..io_utils import DataSink, UnsupportedWritingTarget, use_string_io, FilePath, write_df_to_sink
from ..shared import as_ext, HeaderFileFormats, DictHeaderFormatLiterals, DictHeaderFormats, HeaderFormatLiterals, \
    mk_canon_filenames_v1
from ...core.extensions.metadata.feature_typing import FeatureDataType
from ...core.v2 import raw_v2
from ...core.v2.shared_defs import SegmentDefinitionTypes


def pad_lengths(lol: list[list[str]]):
    max_len = max(map(len, lol), default=0)
    return [li + [''] * (max_len - len(li)) for li in lol]


def write_raw_header_csv(target: DataSink, header: raw.RawHeaderSpec | raw_v2.RawHeaderSpecV2) -> None:
    """
    Write raw header dictionary `header` to `target` in csv format.

    :param target: the file path or buffer to write to
    :param header: header to save
    """
    try:
        with use_string_io(target, expected_file_ext=as_ext(HeaderFileFormats.CSV), mode='w',
                           create_file_if_necessary=True, newline=None) as csvfile:
            writer = csv.writer(csvfile, lineterminator='\n', delimiter=';')
            extensions = header.get('extensions', [])
            use_metadata = False or 'metadata' in extensions
            rows = []

            observation_specs = list(zip([ObservationKinds.E, ObservationKinds.M],
                                         [header['event_specs'].items(), header['measurement_specs'].items()]))

            max_len = max((len(s) for kind, specs in observation_specs for _, s in specs), default=0)
            if 'segment_data_specs' in header:
                header: raw_v2.RawHeaderSpecV2
                max_len = max(max_len, max(len(spec) for typ, spec in header['segment_data_specs'].items()))
            rows.append(
                [ObservationConcepts.Kind, ObservationConcepts.Type] + raw.gen_typed_feature_column_names(max_len))

            def handle_datapoint_spec(kind, typ, spec):
                row = [kind, typ]
                for f in spec:
                    if type(f) is str:
                        row.extend((f, FeatureDataType.Infer.value))
                    elif isinstance(f, dict):
                        f, fmeta = next(iter(f.items()))
                        dt: FeatureDataType = fmeta['data_type']
                        row.extend((f, dt))
                rows.append(row)

            for kind, specs in observation_specs:
                for typ, spec in specs:
                    handle_datapoint_spec(kind, typ, spec)

            if 'segment_specs' in header:
                header: raw_v2.RawHeaderSpecV2
                for concept in header['segment_specs']:
                    rows += [
                        [SegmentDefinitionTypes.Segments, concept if type(concept) is str else next(iter(concept))]]
            if 'segment_data_specs' in header:
                header: raw_v2.RawHeaderSpecV2
                for typ, spec in header['segment_data_specs'].items():
                    handle_datapoint_spec(SegmentDefinitionTypes.SegmentData, typ, spec)

            # if len(extensions) > 0:
            #     rows.append([registry.CSV_KEY] + [e for e in extensions])

            if use_metadata:
                for kind, specs in observation_specs:
                    for label, spec in specs:
                        for f in spec:
                            if isinstance(f, dict):
                                if (pn := f.get('long_name')) is not None:
                                    rows.append([metadata.CSV_KEY, 'long_name', kind, label, f, pn])
                                if (dt := f.get('data_type')) is not None:
                                    rows.append([metadata.CSV_KEY, 'data_type', kind, label, f, dt])

            writer.writerows(pad_lengths(rows))
    except Exception:
        tb: Any = sys.exc_info()[2]
        raise UnsupportedWritingTarget(target).with_traceback(tb)


def write_raw_header_dict(target: DataSink, header: raw.RawHeaderSpec | raw_v2.RawHeaderSpecV2,
                          dict_header_format: DictHeaderFormatLiterals = HeaderFileFormats.JSON) -> None:
    """
    Write raw header dictionary `header` to `target`.

    :param target: file path or buffer to write to
    :param header: header to save
    :param dict_header_format: the header format to use
    """
    assert dict_header_format in DictHeaderFormats

    try:
        with use_string_io(target, mode='w', expected_file_ext=as_ext(dict_header_format),
                           create_file_if_necessary=True) as f:
            if dict_header_format == HeaderFileFormats.JSON:
                json.dump(header, f, indent=2)
            elif dict_header_format == HeaderFileFormats.YAML:
                s = yaml.dump(header, default_flow_style=False)
                f.write(s)
    except Exception:
        tb: Any = sys.exc_info()[2]
        raise UnsupportedWritingTarget(target).with_traceback(tb)


def write_raw_header(target: DataSink, header: raw.RawHeaderSpec | raw_v2.RawHeaderSpecV2,
                     header_format: HeaderFormatLiterals) -> None:
    if header_format == HeaderFileFormats.CSV:
        write_raw_header_csv(target, header)
    elif header_format in DictHeaderFormats:
        header_format = typing.cast(DictHeaderFormatLiterals, header_format)
        write_raw_header_dict(target, header, header_format)


def write_raw_observations(target: DataSink, df: pd.DataFrame) -> None:
    """
    Write Machine Data observation dataframe to `target`.

    :param target: file path or buffer to write header to
    :param df: dataframe to save
    """

    # from mdata.core import ObservationConcepts
    # df[ObservationConcepts.Time] = df[ObservationConcepts.Time].dt.isoformat()
    write_df_to_sink(df, target)


def write_machine_data(base_path: FilePath, md: MD,
                       header_format: HeaderFormatLiterals = HeaderFileFormats.CSV) -> None:
    """
    Write Machine Data instance `md` to `base_path`, extended with canonical '_header.[`header_format`]' and '_data.csv' suffixes.
    See `write_machine_data_custom`.
    """
    md_files = mk_canon_filenames_v1(base_path, header_format=header_format)
    write_machine_data_custom(md_files['header'], md_files['observations'], md, header_format)


def write_machine_data_custom(header_target: Optional[DataSink], data_target: Optional[DataSink],
                              md: MD,
                              header_format: HeaderFormatLiterals) -> None:
    """
    Write Machine Data instance `md` to specified header and data files.

    :param header_target: file path or buffer to write header to. Skipped if None
    :param data_target: file path or buffer to write observations to. Skipped if None
    :param md: the Machine Data instance to save
    :param header_format: the header format to use
    """
    raw_header = raw.convert_to_raw_header(md)
    assert header_format in HeaderFileFormats
    if header_target is not None:
        write_raw_header(header_target, raw_header, header_format=header_format)
    if data_target is not None:
        write_raw_observations(data_target, raw.convert_to_raw_data_legacy(md))


def write_header_file(base_path: FilePath, md: MD, header_format: HeaderFormatLiterals = 'csv') -> None:
    """
    Write Machine Data header to `base_path` extended with canonical header suffix '_header.[`header_format`]'.
    """
    header_file = mk_canon_filenames_v1(base_path, header_format=header_format)['header']
    write_raw_header(header_file, raw.convert_to_raw_header(md), header_format=header_format)


def write_data_file(base_path: FilePath, md: MD) -> None:
    """
    Write Machine Data observation data to `base_path` extended with canonical data suffix '_data.csv'.
    """
    data_file = mk_canon_filenames_v1(base_path)['observations']
    write_raw_observations(data_file, raw.convert_to_raw_data_legacy(md))
