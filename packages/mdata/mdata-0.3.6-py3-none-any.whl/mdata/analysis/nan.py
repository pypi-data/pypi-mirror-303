import numpy as np
import pandas as pd
from IPython.core.display_functions import display
from matplotlib import pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster


def nan_clustering(ts: pd.DataFrame, plot_dendrogram=False, print_output=False) -> frozenset[frozenset[str]]:
    nas = ts.isna()
    nas = ts.isna().loc[:, nas.sum(axis=0) > 0]
    corrs = nas.corr()
    Z = linkage(corrs, method='ward', optimal_ordering=True)

    if plot_dendrogram:
        dendrogram(Z, leaf_label_func=lambda i: corrs.index[i], leaf_rotation=90)
        plt.show()

    clust = fcluster(Z, t=1, criterion='distance')
    clustered_features = pd.DataFrame(clust, index=corrs.index, columns=['cluster_id'])
    feature_groups = set()
    for g, idx in clustered_features.groupby('cluster_id').groups.items():
        if print_output:
            total = nas[idx].all(axis=1).sum()
            singles = np.array([nas[i].sum() for i in idx])
            print('Confidences of {individual column na} => {all group columns nan}')
            display(pd.Series(total / singles, index=idx))
        feature_groups.add(frozenset(idx))

    return frozenset(feature_groups)




def plot_nan_pattern(df, cols):
    fig = make_subplots(len(cols), 1, shared_xaxes=True)
    for i, c in enumerate(cols):
        s = df.loc[df[c].isna(), 'time']
        fig.add_trace(go.Scattergl(x=s, y=[True] * len(s), name=c, mode='markers',
                                   marker=dict(size=10, line_width=4, symbol='line-ns-open')), row=i + 1, col=1)
    fig.update_yaxes(visible=False)
    fig.update_xaxes(range=[min(df['time']), max(df['time'])])
    fig.update_layout(title_text='NaN pattern of selected columns')
    fig.show()
