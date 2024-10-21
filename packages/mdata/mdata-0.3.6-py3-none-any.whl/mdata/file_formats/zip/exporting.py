import zipfile

from ..csv.importing import read_raw_header_any, read_raw_observations
from ..csv.v2.importing import read_raw_segments, read_raw_segment_data
from ..io_utils import ByteSource, use_bytes_io, ByteSink
from ..shared import HeaderFormatLiterals, mk_canon_filenames_v2
from ...core import MD
from ...core.v2 import raw_v2


def write_machine_data_zip(target: ByteSink, md: MD, header_format: HeaderFormatLiterals = 'csv') -> None:
    md_files = mk_canon_filenames_v2(header_format=header_format)
    raw_md = raw_v2.convert_to_raw(md)

    with use_bytes_io(target, expected_file_ext='.zip', mode='wb', create_file_if_necessary=True) as f:
        with zipfile.ZipFile(f, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
            with zf.open(md_files['header'], 'w') as h:
                from mdata.file_formats.csv.exporting import write_raw_header
                write_raw_header(h, raw_md.header, header_format)
            if raw_md.data.observations is not None:
                with zf.open(md_files['observations'], 'w') as obs:
                    from mdata.file_formats.csv.exporting import write_raw_observations
                    write_raw_observations(obs, raw_md.data.observations)
            if raw_md.data.segments is not None:
                with zf.open(md_files['segments'], 'w') as sg:
                    from mdata.file_formats.csv.v2.exporting import write_raw_segments
                    write_raw_segments(sg, raw_md.data.segments)
            if raw_md.data.segment_data is not None:
                with zf.open(md_files['segment_data'], 'w') as sgd:
                    from mdata.file_formats.csv.v2.exporting import write_raw_segment_data
                    write_raw_segment_data(sgd, raw_md.data.segment_data)
