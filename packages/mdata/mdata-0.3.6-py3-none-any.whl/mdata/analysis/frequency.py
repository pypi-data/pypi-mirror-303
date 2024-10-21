from collections.abc import Set
from typing import overload

import numpy as np
import pandas as pd

from mdata.core import MD, ObservationConcepts, as_base
from mdata.core.shared_defs import MeasurementSpecLabel

Hz = float


@overload
def compute_measurement_timedeltas(md: MD, per_object=False) -> dict[str, pd.Series]:
    ...


@overload
def compute_measurement_timedeltas(md: MD, per_object=True) -> dict[str, dict[str, pd.Series]]:
    ...


def compute_measurement_timedeltas(md: MD, per_object=False):
    md = as_base(md)
    res = {}
    for m, tsc in md.measurement_series.items():
        if per_object:
            res[m] = {o: tsc.view(o).df[ObservationConcepts.Time].diff() for o in tsc.objects}
        else:
            res[m] = tsc.df[ObservationConcepts.Time].diff()
    return res


def estimate_measurement_frequencies(md: MD) -> dict[MeasurementSpecLabel, Hz]:
    res = {}
    for m, diffs in compute_measurement_timedeltas(md).items():
        values = diffs.sort_values()
        n = len(values)
        med = diffs.iloc[int(n//2)]
        inner_values = values.iloc[int(0.05 * n):int(0.95 * n)]
        f_mean = inner_values.mean()
        f_med = inner_values.median()
        std = inner_values.std()
        if abs(f_med - f_mean) > std:
            print('mean and median differ significantly', med, f_mean, f_med, std)
        s = pd.Timedelta.total_seconds(f_mean)
        res[m] = 1 / s if s > 0 else np.inf
    return res


def estimate_measurement_deadzones(md: MD, measurement_specs: Set[MeasurementSpecLabel]):
    md = as_base(md)
    res = {}
    for m, deltas in compute_measurement_timeedeltas(md).items():
        low, med, high = deltas.quantile([0.05, 0.5, 0.95])
        mean_wo_outliers = deltas[low <= deltas <= high].mean()
        std_wo_outliers = deltas[low <= deltas <= high].std()
        threshold = mean_wo_outliers + std_wo_outliers * 1.6
        idx = deltas.index.take(deltas > threshold)
        print(idx)
        res[m] = None

    return res
