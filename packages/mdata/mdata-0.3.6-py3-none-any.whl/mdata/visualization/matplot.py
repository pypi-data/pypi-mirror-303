import matplotlib.pyplot as plt
import seaborn as sns

from mdata.core import MD
from mdata.core.factory import as_base

def create_basic_stacked_subplots(md: MD, measurement_spec: str, objects: set[str] = None, features: list[str] = None, figsize=None):
    md = as_base(md)

    tsc = md.measurement_series[measurement_spec]
    os = objects
    fs = features
    if os is None:
        os = list(tsc.objects)
    else:
        assert os <= set(tsc.objects)
        os = [o for o in tsc.objects if o in os]
    if fs is None:
        fs = list(tsc.series_spec.features)
    else:
        assert set(fs) <= set(tsc.series_spec.features)
        fs = [f for f in fs if f in tsc.series_spec.features]

    fig, axs = plt.subplots(len(fs), 1, sharex='all', figsize=figsize)

    for i, f in enumerate(fs):
        for o in os:
            ts = tsc.view(o)
            sns.lineplot(data=ts.df, x='time', y=f, ax=axs[i])
        # axs[i].plot(tsc.df.time, tsc.df[f])
        # axs[i].set_title(f)
    fig.tight_layout()
    return fig
