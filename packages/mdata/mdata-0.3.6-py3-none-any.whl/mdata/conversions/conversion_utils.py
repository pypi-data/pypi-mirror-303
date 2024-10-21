import os
from abc import abstractmethod, ABC
from collections.abc import Mapping
from typing import overload, Union, Optional, final

import pandas as pd

from mdata.core import MD, MDV2
from mdata.core.factory import ObservationSeriesDef, SegmentDataDef, SegmentsDef, extended_factory, \
    ExtendedFactory
from mdata.core.header import Meta
from mdata.core.v2.protocols_v2 import MachineDataV2Protocol
from mdata.file_formats.formats import ExportFormatLiteralsV2, ExportFormatsV2
from mdata.file_formats.shared import HeaderFormatLiterals, HeaderFileFormats, mk_canon_filenames_v2, MDFiles

string_cleaning_transformation_dict = str.maketrans(':/,.-', '_____', ' \n\r')


@overload
def clean_string_identifier(s: str) -> str: ...


@overload
def clean_string_identifier(s: pd.Series) -> pd.Series: ...


def clean_string_identifier(s: Union[str, pd.Series]) -> Union[str, pd.Series]:
    if type(s) is str:
        return str.translate(s, string_cleaning_transformation_dict).strip(' _')
    elif isinstance(s, pd.Series):
        return s.str.translate(string_cleaning_transformation_dict).str.strip(' _')
    elif pd.api.types.is_list_like(s):
        return pd.Series([clean_string_identifier(e) for e in s])


def parse_datetime_inplace(df: pd.DataFrame, column: str, force_utc=True) -> pd.DataFrame:
    df[column] = pd.to_datetime(df.loc[:, column], errors='coerce', utc=force_utc)
    # feature_typing.convert_df(df, {column: feature_typing.FeatureDataType.Datetime}, inplace=True)
    return df


class ConversionTemplate(ABC):
    """
    A base class for arbitrary conversions of some input to a Machine Data instance.
    """
    factory: ExtendedFactory = extended_factory

    def __init__(self, dataset_name: str, **conversion_kwargs) -> None:
        self.dataset_name = dataset_name
        self.conversion_kwargs = conversion_kwargs
        self._md = None

    @abstractmethod
    def convert(self, cache_result=True, **kwargs) -> MDV2:
        ...

    @property
    def machine_data(self) -> MDV2:
        if self._md is None:
            self._md = self.convert(cache_result=True, **self.conversion_kwargs)
        return self._md

    @final
    def export(self, path: str = None, file_format: ExportFormatLiteralsV2 = ExportFormatsV2.ZIP,
               header_format: HeaderFormatLiterals = HeaderFileFormats.CSV) -> None:
        """
        Export the Machine Data instance that this conversion generates.
        Uses the cached instance if the conversion computation was triggered before.

        :param path: base path + filename that suffixes may be appended to, if `None`, `self.dataset_name` is used.
        :param file_format: file format to export to
        :param header_format: header file format to use
        """

        if path is None:
            path = self.dataset_name
        else:
            path = os.path.join(path, self.dataset_name)

        from mdata.io import write_machine_data_v2, \
            write_machine_data_zip

        match file_format:
            case ExportFormatsV2.ZIP:
                write_machine_data_zip(path, self.machine_data, header_format=header_format)
            case ExportFormatsV2.FOLDER:
                write_machine_data_v2(mk_canon_filenames_v2(path, header_format=header_format), self.machine_data,
                                      header_format=header_format)


class IntermediateConversionTemplate(ConversionTemplate, ABC):
    """
    A base class for arbitrary conversions which support the intermediate definition of separate observation series to Machine Data.
    """

    @abstractmethod
    def convert_to_intermediate(self, **kwargs) -> tuple[
        list[ObservationSeriesDef], list[SegmentsDef], list[SegmentDataDef], Meta]: ...

    def convert(self, cache_result=True, **kwargs) -> MD:
        """Create a Machine Data instance using the intermediate conversion."""
        o_series, s_defs, sd_series, meta = self.convert_to_intermediate(**kwargs)
        md = self.factory.make_from_data(*o_series, meta=meta, segments_defs=s_defs, segment_data_defs=sd_series,
                                         **kwargs.get('factory_kwargs', {}))
        if cache_result:
            self._md = md
        return md


# noinspection PyMethodMayBeStatic
class SingleSourceConversionTemplate(IntermediateConversionTemplate, ABC):
    """
    A base class for typical conversions from data stored at a given path into a Machine Data instance.
    """

    def __init__(self, dataset_name: str, path: str, **kwargs) -> None:
        super().__init__(dataset_name, **kwargs)
        self.path = path
        self._md = None

    @abstractmethod
    def read_data(self, path: str, **kwargs) -> pd.DataFrame:
        """
        Read data file(s) from whichever format to a dataframe.
        All necessary preprocessing of the data should be separated into the corresponding methods.
        """
        ...

    @property
    def initial_column_renaming_dict(self) -> Optional[Mapping[str, str]]:
        """Optional column renaming dict to be applied right after reading the dataframe."""
        return None

    def fix_datatypes(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        If necessary, fix dataframe column datatypes, e.g., timestamp conversions.
        """
        return df

    def trim_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        If necessary, filter out missing values, irrelevant/duplicated columns, etc.
        """
        return df

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        If necessary, map/transform values to a more suitable representation, e.g., escape strings, unpack json dicts.
        """
        return df

    def transform_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        If necessary, transform (merge/split/map) or resample rows. May be used as a pre-processing step to form
        sensible measurement specs.
        """
        return df

    def define_series(self, df: pd.DataFrame) -> tuple[
        list[ObservationSeriesDef], list[SegmentsDef], list[SegmentDataDef]]:
        """
        Derive/define the mandatory machine data concepts `mdata.core.MDConcepts` and optionally split the dataframe
        into series.
        """
        return [ObservationSeriesDef(df=df)], [], []

    def define_metadata(self, path: str, df: pd.DataFrame) -> Meta:
        """
        Optionally, define additional metadata, like the extensions used, to be saved in the Machine Data instance.
        """
        return Meta()

    @final
    def convert_to_intermediate(self, **kwargs) -> tuple[
        list[ObservationSeriesDef], list[SegmentsDef], list[SegmentDataDef], Meta]:
        df = self.read_data(self.path, **kwargs)
        if renaming_dict := self.initial_column_renaming_dict:
            df.rename(columns=renaming_dict, inplace=True)
        df = self.fix_datatypes(df)
        df = self.trim_data(df)
        df = self.clean_data(df)
        df = self.transform_data(df)
        o_series, s_defs, sd_series = self.define_series(df)
        meta = self.define_metadata(self.path, df)
        return o_series, s_defs, sd_series, meta

    @final
    def convert(self, cache_result=True, **kwargs) -> MD:
        """Convert the file(s) at `self.path` into a Machine Data instance, using the overloaded methods."""
        o_series, s_def, sd_series, meta = self.convert_to_intermediate(**kwargs)
        md = self.factory.make_from_data(*o_series, meta=meta, segments_defs=s_def, segment_data_defs=sd_series,
                                         **kwargs.get('factory_kwargs', {}))
        if cache_result:
            self._md = md
        return md


class MultiSourceConversion(IntermediateConversionTemplate):
    """
    Efficiently combine multiple independent conversions into one.
    """

    def __init__(self, dataset_name: str, *sub_conversions: IntermediateConversionTemplate) -> None:
        super().__init__(dataset_name)
        self.sub_conversions = list(sub_conversions)

    def convert_to_intermediate(self, **kwargs) -> tuple[
        list[ObservationSeriesDef], list[SegmentsDef], list[SegmentDataDef], Meta]:
        combined_defs = [], [], []
        combined_meta = Meta()
        for sub_conversion in self.sub_conversions:
            *defs, meta = sub_conversion.convert_to_intermediate()
            for l, ll in zip(combined_defs, defs):
                l.extend(ll)
            combined_meta = combined_meta.merge(meta)
        return *combined_defs, combined_meta


class ComposeFromMultiFiles(ConversionTemplate):
    """
    Load multiple independent Machine Data files and merge them "vertically", i.e., all observations are simply
    appended into one resulting Machine Data instance.
    This is another useful way to convert data from multiple sources.
    """

    def __init__(self, dataset_name: str, *paths: tuple[str, HeaderFormatLiterals] | MDFiles) -> None:
        super().__init__(dataset_name)
        assert len(paths) > 0
        self.paths = list(paths)

    def convert(self, cache_result=True, **kwargs) -> MD:
        from mdata.io import read_machine_data_v2, read_machine_data_zip
        mds = []
        for p in self.paths:
            if type(p) is MDFiles:
                mds.append(read_machine_data_v2(p))
            else:
                f, h = p
                mds.append(read_machine_data_zip(f, header_format=h))

        md = MachineDataV2Protocol.lifted_merge(mds, axis='vertical', copy=False)

        if cache_result:
            self._md = md

        return md
