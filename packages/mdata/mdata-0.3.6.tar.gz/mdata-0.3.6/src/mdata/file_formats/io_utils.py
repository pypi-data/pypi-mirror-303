from __future__ import annotations

import datetime
import io
import os
from contextlib import contextmanager
from typing import TextIO, BinaryIO, Generator

import pandas as pd


def ensure_directory_exists(path):
    dirname = os.path.dirname(path)
    if dirname != '' and not os.path.exists(dirname):
        os.makedirs(dirname, exist_ok=True)


def ensure_ext(path, desired_ext, override_ext=True):
    p, e = os.path.splitext(path)
    if e is None or e == '' or (override_ext and (e != desired_ext)):
        return path + desired_ext
    else:
        return path


FilePath = str | os.PathLike[str]
ReadOnlyByteSource = bytes | memoryview
ByteSource = FilePath | BinaryIO | io.BufferedIOBase | ReadOnlyByteSource
TextSource = FilePath | TextIO | io.TextIOBase
DataSource = ByteSource | TextSource

ByteSink = FilePath | BinaryIO | io.BufferedIOBase
TextSink = FilePath | TextIO | io.TextIOBase
DataSink = ByteSink | TextSink


@contextmanager
def open_readonly_byte_buffer(arg: ReadOnlyByteSource) -> Generator[io.BytesIO, None, None]:
    if isinstance(arg, memoryview):
        arg = arg.tobytes()
    if isinstance(arg, bytes):
        with io.BytesIO(arg) as f:
            yield f


@contextmanager
def open_file(arg: FilePath, expected_file_ext: str, mode, create_file_if_necessary=False, encoding='utf-8', **kwargs) -> Generator[
    BinaryIO | TextIO, None, None]:
    arg = ensure_ext(arg, desired_ext=expected_file_ext, override_ext=False)
    if create_file_if_necessary:
        ensure_directory_exists(arg)
    with open(arg, mode, encoding=encoding, **kwargs) as f:
        yield f


@contextmanager
def use_bytes_io(arg: ByteSource | ByteSink, expected_file_ext='.zip', mode='rb', create_file_if_necessary=False) -> \
        Generator[
            io.BufferedIOBase, None, None]:
    if isinstance(arg, ReadOnlyByteSource):
        assert mode == 'rb'
        with open_readonly_byte_buffer(arg) as buf:
            yield buf
    elif isinstance(arg, str | os.PathLike):
        with open_file(arg, expected_file_ext=expected_file_ext, mode=mode,
                             create_file_if_necessary=create_file_if_necessary, encoding=None) as buf:
            yield buf
    else:
        yield arg


@contextmanager
def use_string_io(arg: DataSource | DataSink, expected_file_ext, mode='r',
                  encoding='utf-8',
                  create_file_if_necessary=False, **kwargs) -> \
        Generator[
            io.TextIOBase | TextIO, None, None]:
    if isinstance(arg, ReadOnlyByteSource):
        assert mode == 'r'
        with open_readonly_byte_buffer(arg) as f:
            kwargs.pop('newline', None)
            yield io.TextIOWrapper(f, encoding=encoding, newline=None, **kwargs)
    elif isinstance(arg, str | os.PathLike):
        with open_file(arg, expected_file_ext=expected_file_ext, mode=mode,
                       create_file_if_necessary=create_file_if_necessary, encoding=encoding, **kwargs) as f:
            yield f
    elif isinstance(arg, io.BufferedIOBase | BinaryIO):
        kwargs.pop('newline', None)
        yield io.TextIOWrapper(arg, encoding=encoding, newline=None, **kwargs)
    else:
        yield arg


@contextmanager
def use_for_pandas_io(arg: DataSource | DataSink) -> Generator[FilePath | TextIO | BinaryIO, None, None]:
    if isinstance(arg, ReadOnlyByteSource):
        with open_readonly_byte_buffer(arg) as bf:
            yield bf
    else:
        yield arg


def write_df_to_sink(df: pd.DataFrame, target: DataSink) -> None:
    """
    Write DataFrame to any file-like target. Can be binary/text and in-memory or on-disk file.

    :param df: dataframe to write
    :param target: target file-like object
    """
    if isinstance(target, str | os.PathLike):
        ensure_directory_exists(target)
        from mdata.file_formats.shared import as_ext, HeaderFileFormats
        target = ensure_ext(target, as_ext(HeaderFileFormats.CSV))
    df.to_csv(target, index=False, date_format='%Y-%m-%dT%H:%M:%SZ', sep=';') # TODO make sure timestamps are in ISO format


class UnsupportedWritingTarget(Exception):
    def __init__(self, arg) -> None:
        super().__init__(f'Cannot write to {arg} of type {type(arg)}.')
