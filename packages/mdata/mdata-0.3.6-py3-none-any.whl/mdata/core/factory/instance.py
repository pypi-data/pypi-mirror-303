from __future__ import annotations

from collections.abc import Set
from typing import TypeVar, overload

from mdata.core import MachineDataV1
from mdata.core.base_machine_data import EventTimeseriesSpec, EventTimeseriesView, EventTimeseriesContainer, \
    MeasurementTimeseriesSpec, MeasurementTimeseriesView, MeasurementTimeseriesContainer
from mdata.core.factory.factories import Factory
from mdata.core.factory.factories_v2 import ExtendedFactory
from mdata.core.shared_defs import Extension
from mdata.core.v2.header_v2 import SegmentDataSpec
from mdata.core.v2.machine_data_v2 import MachineDataV2, SegmentDataContainer, SegmentSeriesSpec, \
    SegmentsContainer, SegmentDataSeriesView

"""
Factory to create instances of `BaseMachineData`, the baseline MachineData implementation. 
"""
base_factory = Factory[EventTimeseriesSpec, EventTimeseriesView, EventTimeseriesContainer, MeasurementTimeseriesSpec,
MeasurementTimeseriesView, MeasurementTimeseriesContainer, MachineDataV1](EventTimeseriesSpec,
                                                                          EventTimeseriesView,
                                                                          EventTimeseriesContainer,
                                                                          MeasurementTimeseriesSpec,
                                                                          MeasurementTimeseriesView,
                                                                          MeasurementTimeseriesContainer,
                                                                          MachineDataV1)

"""
Factory to create instances of `MachineDataV2`, the extended MachineData implementation. 
"""
extended_factory = ExtendedFactory[
    EventTimeseriesSpec, EventTimeseriesView, EventTimeseriesContainer, MeasurementTimeseriesSpec,
    MeasurementTimeseriesView, MeasurementTimeseriesContainer, MachineDataV1, SegmentSeriesSpec, SegmentsContainer,
    SegmentDataSpec,
    SegmentDataSeriesView, SegmentDataContainer, MachineDataV2](EventTimeseriesSpec,
                                                                EventTimeseriesView,
                                                                EventTimeseriesContainer,
                                                                MeasurementTimeseriesSpec,
                                                                MeasurementTimeseriesView,
                                                                MeasurementTimeseriesContainer, MachineDataV1,
                                                                SegmentSeriesSpec,
                                                                SegmentsContainer,
                                                                SegmentDataSpec,
                                                                SegmentDataSeriesView, SegmentDataContainer,
                                                                MachineDataV2)

factories = [base_factory, extended_factory]


class UnsupportedExtensionsException(Exception):
    pass


F = TypeVar('F', bound=Factory)


@overload
def get_factory(extensions: Set[Extension] = frozenset()) -> Factory:
    ...


@overload
def get_factory(extensions: Set[Extension]) -> ExtendedFactory:
    ...


def get_factory(extensions: Set[Extension]) -> Factory | ExtendedFactory:
    suitable_factories = [f for f in factories if f.supported_extensions >= extensions]
    if not suitable_factories:
        raise UnsupportedExtensionsException('No Machine Data implementation supports the required extensions.')
    else:
        return suitable_factories[0]
