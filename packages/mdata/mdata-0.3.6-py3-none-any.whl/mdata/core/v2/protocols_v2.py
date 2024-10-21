from typing import overload


from mdata.core.protocols import *
from .header_v2 import SegmentDataSpec, SegmentSpec, HeaderV2
from .shared_defs import SegmentProperty, SegmentSpecType, \
    SegmentDataSpecType, SpecIdentifier
from ..util import StrIndexer, Copyable
from ..shared_protocols import SeriesSpecProtocol, SeriesViewProtocol, SeriesContainerProtocol

class SegmentSeriesSpecProtocol(Copyable, Protocol):
    """
    Immutable object containing the definition of a segment instance series.
    """

    @classmethod
    def of(cls, label: SegmentSpecType, base: SegmentSpec) -> Self:
        """Create a new instance from a label and base `SegmentSpec`."""
        ...

    @property
    @abstractmethod
    def type_name(self) -> SegmentSpecType: ...

    @property
    def identifier(self) -> SegmentSpecType:
        """The identifier, equal to the `label`, of this spec."""
        return self.type_name

    @property
    @abstractmethod
    def base(self) -> SegmentSpec:
        """The underlying `SegmentSpec` as defined a Machine Data header."""
        ...

    @property
    @abstractmethod
    def properties(self) -> frozenset[SegmentProperty]: ...

    @property
    @abstractmethod
    def long_name(self) -> str: ...


SSSpec = TypeVar('SSSpec', bound=SegmentSeriesSpecProtocol, covariant=True)


class SegmentDataSpecProtocol(SeriesSpecProtocol[SegmentDataSpecType, SegmentDataSpec], Protocol):
    """
    Immutable object containing information derived from a segment data spec.
    Used to store auxiliary structural metadata related to a dataframe.
    """

    @classmethod
    def of(cls, label: SpecType, base_spec: SegmentDataSpec) -> Self:
        return super().of(label, base_spec)

    @property
    @abstractmethod
    def type_name(self) -> SegmentDataSpecType:
        """The label of this segment data spec."""
        ...

    @property
    def identifier(self) -> SegmentDataSpecType:
        """The identifier of this spec. Equal to `self.label`."""
        return self.type_name

    @property
    @abstractmethod
    def base(self) -> SegmentDataSpec:
        """The underlying `SegmentDataSpec` as defined in the Machine Data header."""
        ...


SDSSpec = TypeVar('SDSSpec', bound=SegmentDataSpecProtocol, covariant=True)


class SegmentDataSeriesViewProtocol(SeriesViewProtocol[SDSSpec], Protocol[SDSSpec]):

    @property
    @abstractmethod
    def series_spec(self) -> SDSSpec:
        ...

    @abstractmethod
    def feature_column_view(self, *, add_spec_id_prefix: bool = False, use_long_names: bool = False,
                            **kwargs: Any) -> pd.DataFrame:
        ...

    @classmethod
    @abstractmethod
    def of(cls, series_spec: SDSSpec, df: pd.DataFrame, **kwargs: Any) -> Self:
        ...


SDSView = TypeVar('SDSView', bound=SegmentDataSeriesViewProtocol[Any], covariant=True)


class SegmentDataSeriesContainerProtocol(SeriesContainerProtocol[SDSSpec, SDSView], Protocol[SDSSpec, SDSView]):

    @property
    @abstractmethod
    def series_spec(self) -> SDSSpec:
        ...

    @property
    @abstractmethod
    def segment_data_instance_count(self) -> int:
        ...

    @abstractmethod
    def view(self, *args: Any, **kwargs: Any) -> SDSView:
        ...

    @abstractmethod
    def __getitem__(self, item: str) -> SDSView:
        ...


SDSContainer = TypeVar('SDSContainer', bound=SegmentDataSeriesContainerProtocol[Any, Any], covariant=True)


class SegmentSeriesContainerProtocol(Protocol[SSSpec]):

    @classmethod
    def of(cls, segment_specs: Mapping[SegmentSpecType, SSSpec], df: pd.DataFrame) -> Self: ...

    @classmethod
    def empty(cls) -> Self: ...

    @property
    @abstractmethod
    def segment_instance_count(self) -> int: ...

    @property
    @abstractmethod
    def df(self) -> pd.DataFrame: ...

    @df.setter
    @abstractmethod
    def df(self, value: pd.DataFrame) -> None: ...

    @property
    @abstractmethod
    def segment_specs(self) -> Mapping[SegmentSpecType, SSSpec]:
        ...

    @property
    @abstractmethod
    def objects(self) -> Set[str]:
        ...

    @abstractmethod
    def view(self, segment_label: SegmentSpecType, objs: StrIndexer = slice(None)) -> pd.DataFrame: ...

    @abstractmethod
    def gen_interval_index(self, segment_label: SegmentSpecType, obj: StrIndexer) -> pd.MultiIndex: ...

    @overload
    def segment_df(self, observations: pd.DataFrame, by: SegmentSpecType, obj: str,
                   return_segment_intervals: Literal[False] = False) -> pd.DataFrame:
        ...

    @overload
    def segment_df(self, observations: pd.DataFrame, by: SegmentSpecType, obj: str,
                   return_segment_intervals: Literal[True]) -> tuple[pd.DataFrame, pd.MultiIndex]:
        ...

    def segment_df(self, observations: pd.DataFrame, by: SegmentSpecType, obj: str,
                   return_segment_intervals=False) -> pd.DataFrame | tuple[pd.DataFrame, pd.MultiIndex]:
        ...

    @abstractmethod
    def segment(self, df: TSContainer, by: SegmentSpecType, objs: StrIndexer = None) -> TSContainer: ...


SSContainer = TypeVar('SSContainer', bound=SegmentSeriesContainerProtocol[Any], covariant=True)


class MachineDataV2Protocol(MachineDataProtocol[ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC], Protocol[ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC, SSSpec, SSContainer, SDSSpec, SDSView, SDSContainer]):

    @property
    @abstractmethod
    def segment_specs(self) -> Mapping[SegmentSpecType, SSSpec]:
        ...

    @property
    @abstractmethod
    def segments(self) -> SSContainer:
        ...

    @property
    @abstractmethod
    def segment_data_specs(self) -> Mapping[SegmentSpecType, SDSSpec]:
        ...

    @property
    @abstractmethod
    def segment_data(self) -> Mapping[SegmentDataSpecType, SDSContainer]:
        ...

    @property
    @abstractmethod
    def header(self) -> HeaderV2:
        ...

    @property
    @abstractmethod
    def event_series(self) -> Mapping[EventSpecLabel, ETSC]:
        ...

    @abstractmethod
    def project(self, *,
                measurement_feature_selection: Optional[Mapping[
                    MeasurementSpecLabel, bool | Collection[SeriesFeatureLabel]]] = None,
                event_feature_selection: Optional[
                    Mapping[EventSpecLabel, bool | Collection[SeriesFeatureLabel]]] = None,
                project_underlying_dfs=False, copy_underlying_dfs=False,
                segment_data_selection: Optional[Mapping[
                    SegmentSpecType, bool | Collection[SeriesFeatureLabel]]] = None, **kwargs) -> Self:
        """
        Project this Machine Data instance to a subset of observation features.
        Returns a new instance that can be independent of `self` if `copy_underlying_dfs` is used.

        :param measurement_feature_selection: per measurement spec label, a selection of features to keep (boolean True/False = all/no features)
        :param event_feature_selection: per event spec label, a selection of features to keep (boolean True/False = all/no features)
        :param segment_data_selection: per segment data label, a selection of features to keep (boolean True/False = all/no features)
        :param project_underlying_dfs: whether to project dataframes of the timeseries containers or leave them untouched
        :param copy_underlying_dfs: whether to copy the timeseries containers' dataframes, or use views
        :return: a new projected Machine Data instance of the same type
        """
        ...

MDV2 = TypeVar('MDV2', bound='MachineDataV2Protocol[Any, Any, Any, Any, Any, Any, Any, Any, Any, Any, Any]')
