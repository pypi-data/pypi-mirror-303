from typing import TypedDict

import pandas as pd

from mdata.core import MD
from mdata.core.shared_defs import ObservationConcepts
from .detect_milling_engagagement import *


class SpindleParameters(TypedDict, total=False):
    spindle_speed_feature: str
    spindle_current_feature: str
    mean_limit: float
    step: int


def detect_engagement_md(md: MD, object: str, measurement_spec: str,
                         **spindle_param: SpindleParameters) -> pd.DataFrame:
    ms = md.view_measurement_series(measurement_spec, obj=object)
    df = ms.df
    start_bounds, end_bounds, data = detect_engagement(df, timeIdentifier=ObservationConcepts.Time, **spindle_param)
    result_df = pd.DataFrame.from_dict({'start_bounds': start_bounds, 'end_bounds': end_bounds, 'data': data}, orient='columns')
    return result_df
