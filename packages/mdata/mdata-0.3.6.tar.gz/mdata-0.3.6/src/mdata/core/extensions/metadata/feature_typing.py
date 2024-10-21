from __future__ import annotations

from enum import Enum

import pandas as pd


class FeatureDataTypeConversionException(Exception):
    pass


class FeatureDataType(Enum):
    Infer = 'infer'
    Unknown = 'unknown'
    Text = 'text'
    Integer = 'integer'
    Numeric = 'numeric'
    Boolean = 'boolean'
    Categorical = 'categorical'
    Datetime = 'datetime'
    Duration = 'duration'


target_numeric_types = {FeatureDataType.Integer: 'Int64', FeatureDataType.Numeric: 'Float64'}


def infer_type(series: pd.Series) -> FeatureDataType:
    converted = series.convert_dtypes()
    return get_type(converted)


def get_type(series: pd.Series) -> FeatureDataType:
    from pandas.api.types import is_bool_dtype, is_float_dtype, is_integer_dtype, is_datetime64_any_dtype, is_timedelta64_dtype, is_string_dtype

    dtype = series.dtype
    if is_string_dtype(dtype):
        return FeatureDataType.Text
    elif is_integer_dtype(dtype):
        return FeatureDataType.Integer
    elif is_float_dtype(dtype):
        return FeatureDataType.Numeric
    elif is_bool_dtype(dtype):
        return FeatureDataType.Boolean
    elif isinstance(dtype, pd.CategoricalDtype):
        return FeatureDataType.Categorical
    elif is_datetime64_any_dtype(dtype):
        return FeatureDataType.Datetime
    elif is_timedelta64_dtype(dtype):
        return FeatureDataType.Duration
    else:
        return FeatureDataType.Infer


def has_numeric_type(series: pd.Series) -> bool:
    return get_type(series) in target_numeric_types.keys()


def infer_types(df: pd.DataFrame) -> dict[str, FeatureDataType]:
    return {c: infer_type(df.loc[:, c]) for c in df.columns}


def get_types(df: pd.DataFrame) -> dict[str, FeatureDataType]:
    return {c: get_type(df.loc[:, c]) for c in df.columns}


def is_series_convertible(series: pd.Series, data_type: FeatureDataType):
    if (data_type == FeatureDataType.Integer) or (data_type == FeatureDataType.Numeric):
        try:
            conv = series.astype(target_numeric_types[data_type], errors='raise')
        except:
            return False
        return series.equals(conv)  # np.array_equal(series, conv)
    elif data_type == FeatureDataType.Boolean:
        try:
            conv = series.astype('bool', errors='raise')
        except:
            return False
        return series.equals(conv)  # np.array_equal(series, conv)
    elif data_type == FeatureDataType.Datetime:
        try:
            pd.to_datetime(series, errors='raise', format='ISO8601')
        except:
            return False
        return True
    elif data_type == FeatureDataType.Duration:
        try:
            pd.to_timedelta(series, errors='raise')
        except:
            return False
        return True
    return False


def convert_df(df: pd.DataFrame, data_types: dict[str, FeatureDataType], inplace=False, copy=True):
    res = pd.DataFrame(index=df.index) if not inplace else df

    for f, dt in data_types.items():
        try:
            if inplace:
                convert_series((df, f), dt, inplace=True)
            else:
                res[f] = convert_series((df, f), dt, inplace=False)
        except Exception as e:
            raise FeatureDataTypeConversionException(f'Conversion of feature \'{f}\' to {dt} failed:\n' + str(e))

    return res


def convert_series(arg: pd.Series | tuple[pd.DataFrame, str], data_type: FeatureDataType, inplace=True,
                   copy=True) -> pd.Series:
    s: pd.Series
    if type(arg) is tuple:
        df: pd.DataFrame
        df, feature = arg
        s = df.loc[:, feature]

        def upd_inplace(conv):
            df[feature] = conv
    else:
        s = arg

        def upd_inplace(conv):
            # TODO possibly not actually inplace
            s.loc[:] = conv

    conv = None

    if data_type is FeatureDataType.Integer or data_type is FeatureDataType.Numeric:
        conv = s.astype(target_numeric_types[data_type], copy=copy)
    elif data_type is FeatureDataType.Boolean:
        conv = s.astype(bool, copy=copy)
    elif data_type is FeatureDataType.Datetime:
        conv = pd.to_datetime(s, errors='raise', format='ISO8601')
    elif data_type is FeatureDataType.Duration:
        conv = pd.to_timedelta(s, errors='raise')
    elif data_type is FeatureDataType.Text:
        conv = s.astype(str, copy=copy)
    elif data_type is FeatureDataType.Categorical:
        if isinstance(s, pd.DataFrame):
            cdt = {c: pd.CategoricalDtype(s.loc[:, c].dropna().unique()) for c in s.columns}
        elif isinstance(s, pd.Series):
            cdt = pd.CategoricalDtype(s.dropna().unique())
        conv = s.astype(cdt, copy=copy)
    elif data_type is FeatureDataType.Infer:
        conv = s.convert_dtypes()

    if inplace:
        upd_inplace(conv)
        return s
    else:
        return conv
