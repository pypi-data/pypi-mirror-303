import zipfile

from mdata.core.v2.raw_v2 import RawMD, DataPartition
from ..csv.importing import read_raw_header_any, read_raw_observations
from ..csv.v2.importing import read_raw_segments, read_raw_segment_data
from ..io_utils import ByteSource, use_bytes_io
from ..shared import HeaderFormatLiterals, HeaderFileFormats, mk_canon_filenames_v2


def read_raw_machine_data_zip(source: ByteSource,
                              header_format: HeaderFormatLiterals = HeaderFileFormats.CSV) -> RawMD:
    md_files = mk_canon_filenames_v2(header_format=header_format)
    parts = {}

    with use_bytes_io(source, expected_file_ext='.zip', mode='rb') as f:
        with zipfile.ZipFile(f, 'r', compression=zipfile.ZIP_DEFLATED) as zf:
            with zf.open(md_files['header']) as h:
                parts['header'] = read_raw_header_any(h, header_format=header_format)
            files_in_zip = set(zf.namelist())
            if md_files['observations'] in files_in_zip:
                with zf.open(md_files['observations']) as obs:
                    parts['observations'] = read_raw_observations(obs)
            if md_files['segments'] in files_in_zip:
                with zf.open(md_files['segments']) as sg:
                    parts['segments'] = read_raw_segments(sg)
            if md_files['segment_data'] in files_in_zip:
                with zf.open(md_files['segment_data']) as sgd:
                    parts['segment_data'] = read_raw_segment_data(sgd)

    return RawMD(parts.pop('header'), DataPartition(**parts))


def read_machine_data_zip(source: ByteSource, header_format: HeaderFormatLiterals = HeaderFileFormats.CSV,
                          validity_checking=False):
    from mdata.core.v2.raw_v2 import create_machine_data_from_raw
    raw_md_v2 = read_raw_machine_data_zip(source, header_format)
    if validity_checking:
        raise NotImplemented
    return create_machine_data_from_raw(raw_md_v2)
