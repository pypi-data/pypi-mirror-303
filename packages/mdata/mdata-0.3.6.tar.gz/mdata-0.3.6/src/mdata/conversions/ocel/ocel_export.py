import pandas as pd

from mdata.core import MD, ObservationConcepts
from pm4py.objects.ocel.obj import OCEL, constants

import mdata.core.shared_defs


def create_ocel(md: MD):
    raise NotImplemented
    pd.DataFrame()
    os = md.observation_index[ObservationConcepts.Object].unique()
    for mt, tsc in md.measurement_series.items():
        i = 0
        m_obj = pd.DataFrame(tsc.df, columns=list(tsc.series_spec.features))
        m_obj = m_obj.assign(**{constants.DEFAULT_OBJECT_TYPE: tsc.series_spec.type_name, constants.DEFAULT_OBJECT_ID: i})
    for et, tsc in md.event_series.items():
        tsc.series_spec.features

    ...