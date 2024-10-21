"""
This module offers Machine Data instance creation functionality via high-level factory interfaces.
Used to convert external datasets to the Machine Data format.
"""
from .casting import as_base, as_v2, as_supports
# noinspection PyUnresolvedReferences
from .factories import ObservationSeriesDef, ObservationConcepts, ObservationKinds, \
    define_observation_series_defs_by_groupby, Meta, Extension
from .instance import base_factory, get_factory, extended_factory, Factory, ExtendedFactory
from .factories_v2 import define_segment_data_series_defs_by_groupby, SegmentConcepts, SegmentDataDef, SegmentsDef
