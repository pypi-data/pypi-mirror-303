from __future__ import annotations

from abc import abstractmethod
from collections.abc import Set
from typing import Protocol, Iterable, Collection, Literal, Mapping, TypeVar, ClassVar, Optional, Self, Any, \
    runtime_checkable, Generic

import pandas as pd

from mdata.core.header import ObservationSpec, Meta, Header, DatapointSpec
from mdata.core.shared_defs import SeriesFeatureLabel, ObservationKindValue, \
    ObservationKind, SpecType, ObservationSpecIdentifier, EventSpecLabel, MeasurementSpecLabel, Extension
from mdata.core.shared_protocols import SeriesSpecProtocol, SeriesViewProtocol, SeriesContainerProtocol, P, SSpec
from mdata.core.util import SlimMapping, Copyable


@runtime_checkable
class ObservationKindSpecific(Protocol):
    observation_kind: ClassVar[ObservationKind]
    #@property
    #@classmethod
    #@abstractmethod
    #def observation_type(cls) -> ObservationType: ...


@runtime_checkable
class EventSpecific(Protocol):
    E: ObservationKind = ObservationKind.E
    observation_kind: ClassVar[ObservationKind] = E


@runtime_checkable
class MeasurementSpecific(Protocol):
    M: ObservationKind = ObservationKind.M
    observation_kind: ClassVar[ObservationKind] = M


class TimeseriesSpecProtocol(ObservationKindSpecific, SeriesSpecProtocol[ObservationSpecIdentifier, ObservationSpec],
                             Protocol):
    """
    Immutable object containing information derived from an observation spec.
    Used to store auxiliary structural metadata related to a dataframe.
    Implementations are specific to an observation type.
    """

    @property
    @abstractmethod
    def base(self) -> ObservationSpec:
        """The underlying `ObservationSpec` as defined a Machine Data header."""
        ...

    @property
    @abstractmethod
    def identifier(self) -> ObservationSpecIdentifier:
        """The identifier, i.e., `(type, label)` tuple of this spec."""
        ...


TSSpec = TypeVar('TSSpec', bound=TimeseriesSpecProtocol, covariant=True)

class TimeseriesViewProtocol(ObservationKindSpecific, SeriesViewProtocol[TSSpec], Protocol[TSSpec]):
    @abstractmethod
    def feature_column_view(self, *, add_spec_id_prefix: bool = False,
                            use_long_names: bool = False, include_time_col: bool = True,
                            include_object_col: bool = False,
                            **kwargs) -> pd.DataFrame:
        """
        Generates a view on the underlying dataframe.

        :param include_time_col: whether to include the `MDConcepts.Time` column
        :param include_object_col: whether to include the `MDConcepts.Object` column
        :param add_spec_id_prefix: whether to prefix the column names with the spec id (useful for avoiding name collisions when joining dataframes)
        :param use_long_names: whether to rename the columns to use the "long" feature names specified in `self.timeseries_spec`
        """

    @property
    @abstractmethod
    def series_spec(self) -> TSSpec:
        ...

    @property
    def observation_count(self) -> int:
        """The number of contained observations. Equivalently, length of `self.df`."""
        return len(self)


TSView = TypeVar('TSView', bound=TimeseriesViewProtocol[Any])

TSContainer = TypeVar('TSContainer', bound='TimeseriesContainerProtocol[Any, Any]')


class TimeseriesContainerProtocol(ObservationKindSpecific, SeriesContainerProtocol[TSSpec, TSView],
                                  Protocol[TSSpec, TSView]):

    @abstractmethod
    def view(self, *args: P.args, **kwargs: P.kwargs) -> TSView:
        ...

    @abstractmethod
    def __getitem__(self, item: str) -> TSView:
        ...


ETSSpec = TypeVar('ETSSpec', bound=TimeseriesSpecProtocol, covariant=True)
MTSSpec = TypeVar('MTSSpec', bound=TimeseriesSpecProtocol, covariant=True)
ETSView = TypeVar('ETSView', bound=TimeseriesViewProtocol[Any], covariant=True)
MTSView = TypeVar('MTSView', bound=TimeseriesViewProtocol[Any], covariant=True)
ETSC = TypeVar('ETSC', bound=TimeseriesContainerProtocol[Any, Any], covariant=True)
MTSC = TypeVar('MTSC', bound=TimeseriesContainerProtocol[Any, Any], covariant=True)

MD = TypeVar('MD', bound='MachineDataProtocol[Any, Any, Any, Any, Any, Any]')


class MachineDataProtocol(SlimMapping[ObservationSpecIdentifier, ETSC | MTSC], Copyable,
                          Protocol[ETSSpec, ETSView, ETSC, MTSSpec, MTSView, MTSC]):
    """
    The base interface for all Machine Data representation classes.
    Such classes store header information, observation specs and containers.
    They provide convenience methods to access sub objects' features such as generating views on the data.

    :cvar supported extensions: The extensions explicitly supported by an implementing class.
    """
    supported_extensions: ClassVar[frozenset[Extension]]

    @property
    @abstractmethod
    def meta(self) -> Meta:
        """The header metadata."""
        ...

    @property
    @abstractmethod
    def event_series(self) -> Mapping[EventSpecLabel, ETSC]:
        """A mapping of event labels the corresponding event containers."""
        ...

    @property
    @abstractmethod
    def measurement_series(self) -> Mapping[MeasurementSpecLabel, MTSC]:
        """A mapping of measurement labels to the corresponding measurement containers."""
        ...

    @abstractmethod
    def __getitem__(self, item: ObservationSpecIdentifier) -> ETSC | MTSC:
        ...

    # @deprecated
    @classmethod
    @abstractmethod
    def of(cls, meta: Meta = Meta(), events: Iterable[ETSC] = (), measurements: Iterable[MTSC] = (),
           **kwargs: Any) -> Self:
        """Creates a new instance holding the specified event/measurement containers and meta information."""
        ...

    @property
    @abstractmethod
    def header(self) -> Header:
        """A complete Machine Data Header of this instance."""
        ...

    @property
    @abstractmethod
    def observation_index(self) -> pd.DataFrame:
        """An internal index over all contained observations."""
        ...

    @property
    @abstractmethod
    def series_containers(self) -> Set[ETSC | MTSC]:
        """The combined set of event as well as measurement containers."""
        ...

    @property
    @abstractmethod
    def observation_count(self) -> int:
        """The number of observations."""
        ...

    @property
    @abstractmethod
    def objects(self) -> Set[str]:
        """The set of object identifiers that occur in the instance."""
        ...

    @property
    @abstractmethod
    def event_specs(self) -> Mapping[EventSpecLabel, ETSSpec]:
        """A mapping of event spec labels to their timeseries spec objects."""
        ...

    @property
    @abstractmethod
    def measurement_specs(self) -> Mapping[MeasurementSpecLabel, MTSSpec]:
        """A mapping of measurement spec labels to their timeseries spec objects."""
        ...

    @abstractmethod
    def get_spec(self, identifier: ObservationSpecIdentifier) -> ETSSpec | MTSSpec:
        """
        Returns the timeseries spec with id `identifier`.

        :param identifier: the id of the selected timeseries spec
        :rtype: an implementation of `TimeseriesSpecProtocol`
        """
        ...

    @abstractmethod
    def get_events(self, label: EventSpecLabel) -> ETSC:
        """
        Returns the event container of spec `label`.

        :param label: label of selected event spec
        :rtype: implementation of `TimeseriesContainerProtocol`
        """
        ...

    @abstractmethod
    def get_measurements(self, label: MeasurementSpecLabel) -> MTSC:
        """
        Returns the measurement container of spec `label`.

        :param label: label of selected measurement spec
        :rtype: implementation of `TimeseriesContainerProtocol`
        """
        ...

    @abstractmethod
    def view_event_series(self, label: EventSpecLabel, **kwargs) -> ETSView:
        """
        Generates a sliced view on the events of spec `label`.
        Implementations can have different arguments and thus slicing capabilities.

        :rtype: implementation of TimeseriesViewProtocol
        :param label: event spec label
        :param kwargs: variable attribute values/slice definition
        """
        ...

    @abstractmethod
    def view_measurement_series(self, label: MeasurementSpecLabel, **kwargs) -> MTSView:
        """
        Generates a sliced view on the measurements of spec `label`.
        Implementations can have different arguments and thus slicing capabilities.

        :rtype: implementation of TimeseriesViewProtocol_
        :param label: measurement spec label
        :param kwargs: variable attribute values/slice definition
        """
        ...

    @abstractmethod
    def recalculate_index(self, override_categorical_types=True, sort_by_time=True, **kwargs):
        """Recalculates the internal index over all contained observations and specs. Typically called automatically."""
        ...

    @abstractmethod
    def fit_to_data(self, ignore_index=False):
        """
        Updates immutable objects such as timeseries specs to be in sync with the underlying mutable dataframes.
        Depending on `ignore_index`, propagate changes to this object's index to series containers, or override this
        index to reflect potentially filtered or extended container dataframes.

        :param ignore_index: whether to override this object's internal index or update container indices with this index
        """
        ...

    @abstractmethod
    def create_joined_observations_df(self, event_labels: Iterable[EventSpecLabel] | bool | None = None,
                                      measurement_labels: Iterable[MeasurementSpecLabel] | bool | None = None,
                                      prefix_columns_to_avoid_collisions=True, copy=False) -> pd.DataFrame:
        """
        Generates a joined dataframe of the `self.index_frame` and the selected event/measurement container
        dataframes which contain the features of their respective spec.

        :param event_labels: event series to include
        :param measurement_labels: measurement series to include
        :param prefix_columns_to_avoid_collisions: whether to rename the joined feature columns with their spec identifier
        :param copy: whether to return a copy or views on the joined dataframes
        """
        ...

    @abstractmethod
    def create_observation_index_view(self,
                                      kinds: Optional[ObservationKindValue | Iterable[ObservationKindValue]] = None,
                                      objs: Optional[str | Iterable[str]] = None,
                                      types: Optional[SpecType | Iterable[SpecType]] = None) -> pd.DataFrame:
        """
        Generates a filtered view on the `self.index_frame`.

        :param kinds: one, or a selection of, observation types
        :param objs: one, or a selection of, object identifiers
        :param types: one, or a selection of, observation types
        """
        ...

    @abstractmethod
    def project(self, *,
                measurement_feature_selection: Optional[Mapping[
                    MeasurementSpecLabel, bool | Collection[SeriesFeatureLabel]]] = None,
                event_feature_selection: Optional[
                    Mapping[EventSpecLabel, bool | Collection[SeriesFeatureLabel]]] = None,
                project_underlying_dfs=False, copy_underlying_dfs=False, **kwargs) -> Self:
        """
        Project this Machine Data instance to a subset of observation features.
        Returns a new instance that can be independent of `self` if `copy_underlying_dfs` is used.

        :param measurement_feature_selection: per measurement spec label, a selection of features to keep (boolean True/False = all/no features)
        :param event_feature_selection: per event spec label, a selection of features to keep (boolean True/False = all/no features)
        :param project_underlying_dfs: whether to project dataframes of the timeseries containers or leave them untouched
        :param copy_underlying_dfs: whether to copy the timeseries containers' dataframes, or use views
        :return: a new projected Machine Data instance of the same type
        """
        ...

    @abstractmethod
    def is_mergeable(self, other: MD) -> bool:
        """Checks whether `self` and `other` are mergeable Machine Data instances."""
        ...

    @abstractmethod
    def merge(self, other: Self,
              axis: Literal['horizontal', 'vertical'] = 'horizontal', copy: bool = True,
              suppress_index_creation=False) -> Self:
        """
        Merges `self` and `other` along the given `axis`.

        :param other: the other `MachineData` instance to merge with
        :param axis: whether to merge "horizontally" or "vertically"
                - `horizontal` extends shared specs and their observations by the additional features defined in `other`.
                - `vertical` appends the observations of `other`. Shared spec identifiers must refer to equivalent specs.
        :param copy: if `copy=True`, internal dataframes are copied, and an independent instance is returned
        :param suppress_index_creation: if `True`, the index is only lazily computed in the resulting merged instance
        """
        ...

    @classmethod
    def lifted_merge(cls, machine_datas: Iterable[MD], axis: Literal['horizontal', 'vertical'] = 'horizontal',
                     copy: bool = True, suppress_index_creation=False) -> MD:
        assert axis in {'horizontal', 'vertical'}
        machine_datas = list(machine_datas)
        if len(machine_datas) > 0:
            current = machine_datas.pop(0)
            last = machine_datas.pop()
            for md in machine_datas:
                current = current.merge(md, axis=axis, copy=False, suppress_index_creation=True)
            return current.merge(last, axis=axis, copy=copy, suppress_index_creation=suppress_index_creation)

    @abstractmethod
    def summary(self) -> str:
        """Generates a brief textual overview of the data contained in this instance."""
        ...
