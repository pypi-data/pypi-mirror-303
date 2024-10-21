from enum import Enum
from typing import TypeAlias, Literal, Union, Self

from mdata.core.shared_defs import SpecType, ObservationKindValue, ConceptsEnum
from mdata.core.util import StringEnumeration

SegmentDefinitionTypeValue = Literal['S', 'SD']
SegmentPropertyValue = str
DataTypeLabelValue = Union[ObservationKindValue, SegmentDefinitionTypeValue]
SpecIdentifier = tuple[DataTypeLabelValue, SpecType]


class SegmentDefinitionTypes(StringEnumeration):
    Segments: SegmentDefinitionTypeValue = 'S'
    SegmentData: SegmentDefinitionTypeValue = 'SD'


class SegmentDefinitionType(Enum):
    Segments = 'S'
    SegmentData = 'SD'


class SegmentConcepts(ConceptsEnum):
    Object = 'object'
    Concept = 'concept'
    Index = 'segment_index'
    Start = 'start'
    End = 'end'

    @classmethod
    def base_columns(cls) -> list[str]:
        return [SegmentConcepts.Object, SegmentConcepts.Concept, SegmentConcepts.Index, SegmentConcepts.Start,
                SegmentConcepts.End]


class SegmentDataConcepts(ConceptsEnum):
    Type = 'type'
    Object = 'object'
    Concept = 'concept'
    Index = 'segment_index'

    @classmethod
    def base_columns(cls) -> list[str]:
        return [SegmentDataConcepts.Object, SegmentDataConcepts.Concept, SegmentDataConcepts.Index,
                SegmentDataConcepts.Type]


class ExtendedSegmentConcepts(SegmentConcepts):
    SegmentInterval = 'segment_interval'


class SegmentProperties(StringEnumeration):
    Monotonic: SegmentPropertyValue = 'monotonic'
    Disjoint: SegmentPropertyValue = 'disjoint'
    Seamless: SegmentPropertyValue = 'seamless'
    Complete: SegmentPropertyValue = 'complete'


class SegmentProperty(Enum):
    Monotonic = 'monotonic'
    Disjoint = 'disjoint'
    Seamless = 'seamless'
    Complete = 'complete'


SegmentSpecType: TypeAlias = SpecType
SegmentDataSpecType: TypeAlias = SpecType
