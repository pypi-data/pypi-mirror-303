from __future__ import annotations

from collections.abc import Iterable
from enum import Enum
from typing import Literal, Self

import pandas as pd

from mdata.core.util import StringEnumeration

SeriesFeatureLabel = str
SeriesFeatureLabels = tuple[SeriesFeatureLabel, ...]
ObservationKindValue = Literal['E', 'M']


class ObservationKinds(StringEnumeration):
    E: ObservationKindValue = 'E'
    M: ObservationKindValue = 'M'


class ObservationKind(Enum):
    E = 'E'
    M = 'M'


SpecType = str
ObservationSpecIdentifier = tuple[ObservationKindValue, SpecType]
EventSpecLabel = str
MeasurementSpecLabel = str

class ConceptsEnum(StringEnumeration):

    @classmethod
    def base_columns(cls) -> list[str]:
        return []

class ObservationConcepts(ConceptsEnum):
    Time = 'time'
    Object = 'object'
    Kind = 'kind'
    Type = 'type'

    @classmethod
    def base_columns(cls) -> list[str]:
        return [ObservationConcepts.Time, ObservationConcepts.Object, ObservationConcepts.Kind, ObservationConcepts.Type]


class ExtendedObservationConcepts(ObservationConcepts):
    Index = 'observation_index'


def only_feature_columns(cols: Iterable[str], exclusion_list=None) -> list[str]:
    if exclusion_list is None:
        exclusion_list = ObservationConcepts.base_columns()
    return [c for c in cols if c not in exclusion_list]


def project_on_feature_columns(df: pd.DataFrame) -> pd.DataFrame:
    return df[only_feature_columns(df.columns)]


# manually connected to json schema in ../../file_formats
class Extensions(StringEnumeration):
    Metadata = 'metadata'
    Segments = 'segments'


class Extension(Enum):
    Metadata = 'metadata'
    Segments = 'segments'


class SeriesSpecMergeException(Exception):
    pass


class TimeseriesContainerMergeException(Exception):
    pass


class MachineDataMergeException(Exception):
    pass
