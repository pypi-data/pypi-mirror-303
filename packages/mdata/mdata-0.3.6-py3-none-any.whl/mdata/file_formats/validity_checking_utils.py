import pandas as pd

import mdata.core.shared_defs
from mdata.core import MD, ObservationConcepts
from mdata.core.extensions.metadata.feature_typing import is_series_convertible
from mdata.core.header import create_header_from_raw, FeatureSpec, ObservationSpec
from mdata.core.raw import gen_feature_column_names, \
    RawHeaderSpec
from mdata.core.shared_defs import ObservationConcepts


class ValidityCheckingException(Exception):
    pass


class SyntacticValidityException(ValidityCheckingException):
    pass


class SemanticValidityException(ValidityCheckingException):
    pass


class UnsupportedHeaderFileFormat(SyntacticValidityException):
    pass


class MalformedHeaderFileException(SyntacticValidityException):
    pass


class MalformedDataFileException(SyntacticValidityException):
    pass


class InsufficientHeader(SemanticValidityException):
    pass


class InconsistentTimeseriesType(SemanticValidityException):
    pass


def get_placeholder_cols(df):
    return [c for c in df.columns if c not in ObservationConcepts.base_columns()]


def check_header_data_compatibility(header: RawHeaderSpec, data: pd.DataFrame, do_typechecking=False):
    header = create_header_from_raw(header)
    placeholder_cols = get_placeholder_cols(data)
    to_be_cols = gen_feature_column_names(len(placeholder_cols))
    for group, idx in data.groupby([ObservationConcepts.Kind, ObservationConcepts.Type]).groups.items():
        tpy, label = group
        spec: ObservationSpec = header.lookup_spec(tpy, label)
        if spec is None:
            raise InsufficientHeader(f"({tpy},{label}) is not declared in {header}")
        f_len = len(spec)
        for i, c in enumerate(placeholder_cols):
            assert c == to_be_cols[i]
            if i < f_len:
                f: FeatureSpec = spec.features[i]
                if do_typechecking and f.data_type is not None:
                    is_series_convertible(data.loc[idx, c], f.data_type)
            if i >= f_len and not data.loc[idx, c].isna().all():
                raise InconsistentTimeseriesType
    return True


def check_time_column(data: pd.DataFrame):
    import pandas.core.dtypes.common
    if not pandas.core.dtypes.common.is_datetime64_any_dtype(data['time']):
        raise MalformedDataFileException('Time column could not be parsed as datetime.')
