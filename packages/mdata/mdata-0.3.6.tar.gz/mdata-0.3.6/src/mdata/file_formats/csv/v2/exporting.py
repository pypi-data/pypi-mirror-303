import pandas as pd

from mdata.core import MD
from mdata.file_formats.io_utils import DataSink, write_df_to_sink
from mdata.file_formats.shared import MDFiles, HeaderFormatLiterals, HeaderFileFormats


def write_raw_segments(target: DataSink, df: pd.DataFrame) -> None:
    """
    Write Machine Data segments dataframe to `target`.

    :param target: file path or buffer to write header to
    :param df: dataframe to save
    """
    write_df_to_sink(df, target)


def write_raw_segment_data(target: DataSink, df: pd.DataFrame) -> None:
    """
    Write Machine Data segment data dataframe to `target`.

    :param target: file path or buffer to write header to
    :param df: dataframe to save
    """
    write_df_to_sink(df, target)


def write_machine_data_v2(md_files: MDFiles, md: MD, header_format: HeaderFormatLiterals = 'csv') -> None:
    """
    Write Machine Data instance `md` to specified header and data files.

    :param md_files: file paths or buffers to write header and data files to. Missing files are skipped.
    :param md: the Machine Data instance to save
    :param header_format: the header format to use
    """
    from mdata.core.v2 import raw_v2
    raw_md = raw_v2.convert_to_raw(md)
    if 'header' in md_files:
        from mdata.file_formats.csv.exporting import write_raw_header
        assert header_format in HeaderFileFormats
        write_raw_header(md_files['header'], raw_md.header, header_format)
    if 'observations' in md_files and raw_md.data.observations is not None:
        from mdata.file_formats.csv.exporting import write_raw_observations
        write_raw_observations(md_files['observations'], raw_md.data.observations)
    if 'segments' in md_files and raw_md.data.segments is not None:
        write_raw_segments(md_files['segments'], raw_md.data.segments)
    if 'segment_data' in md_files and raw_md.data.segment_data is not None:
        write_raw_segment_data(md_files['segment_data'], raw_md.data.segment_data)
