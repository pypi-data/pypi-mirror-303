from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd

#if TYPE_CHECKING:
from mdata.core.v2.shared_defs import SegmentProperties, SegmentPropertyValue, SegmentProperty


def derive_segments_properties(df: pd.DataFrame,
                               claimed: set[SegmentPropertyValue | SegmentProperties | SegmentProperty] = None) -> \
frozenset[SegmentProperty]:
    claimed = {SegmentProperty(sp) for sp in claimed}
    # TODO improve/complete, also with regards to asserting the claims
    from mdata.core.v2.shared_defs import SegmentConcepts
    res = claimed | {SegmentProperty.Monotonic, SegmentProperty.Complete}
    for o, idx in df.groupby(SegmentConcepts.Object).groups.items():
        segment_series = df.loc[idx].sort_values(SegmentConcepts.Index)
        is_mono = segment_series[SegmentConcepts.Start].is_monotonic_increasing
        if not is_mono:
            res.remove(SegmentProperty.Monotonic)

        max_index = segment_series[SegmentConcepts.Index].max()
        complete_indices = segment_series[SegmentConcepts.Index].sort_values().equals(pd.RangeIndex(max_index))
        if not complete_indices:
            res.remove(SegmentProperty.Complete)

    return frozenset(res)
