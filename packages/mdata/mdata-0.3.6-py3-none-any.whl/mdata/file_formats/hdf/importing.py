import pandas as pd

from mdata.core import ObservationConcepts, MD, ObservationKinds
from mdata.core.header import Meta
from mdata.core.raw import RawMetadataFeatureSpec


class InvalidHeaderException(Exception): pass


# noinspection PyTypeChecker
def read_machine_data_h5(filename) -> MD:
    # ext = io_utils.ensure_ext(filename, '.h5', override_ext=False)
    from mdata.core.factory import get_factory

    with pd.HDFStore(filename, mode='r') as store:
        measurements, events = [], []
        rel_groups = next(store.walk('/'))[1]

        extensions = set()
        use_metadata = False
        if store.get_node('meta/extensions') is not None:
            extensions = set(store.get('meta/extensions'))
            use_metadata = 'metadata' in extensions

        metadata = {}
        if use_metadata and store.get_node('meta/metadata') is not None:
            metadata_df: pd.DataFrame = store.get('meta/metadata')
            for key, row in metadata_df.iterrows():
                value = row['value']
                metadata[str(key)] = value

        if use_metadata and store.get_node('meta/specs') is not None:
            spec_extra_metadata: pd.DataFrame = store.get('meta/specs')

            def get_meta(t, label) -> list[RawMetadataFeatureSpec]:
                results = spec_extra_metadata.loc[
                    (spec_extra_metadata[ObservationConcepts.Kind] == t) & (
                            spec_extra_metadata[ObservationConcepts.Type] == label), ['feature',
                                                                                  'long_name',
                                                                                  'data_type']]
                specs = []
                for f, idx in results.groupby('feature').groups.items():
                    g = results.loc[idx][['long_name', 'data_type']]
                    if len(g) != 1:
                        raise InvalidHeaderException(f'Duplicate feature metadata for {f}.')
                    ln, dt = g.iloc[0]
                    specs.append(RawMetadataFeatureSpec({f: {'long_name': ln, 'data_type': dt}}))
                return specs

        meta = Meta.of(extensions, metadata)

        factory = get_factory(meta.extensions)

        def make_series_cont(path, o_type, label):
            key = '/'.join([path, label])
            df: pd.DataFrame = store.get(key)
            specs = get_meta(o_type, label) if use_metadata else ()
            ts_spec = factory.make_ts_spec_from_data(spec_id=(o_type, label), df=df, extra_metadata=specs)
            return factory.make_ts_container(ts_spec, df)

        series_containers = []

        def add_series_containers(base_key, o_type):
            if base_key in rel_groups:
                (path, groups, leaves) = next(store.walk(f'/{base_key}'))
                for label in leaves:
                    series_containers.append(make_series_cont(path, o_type, label))

        add_series_containers('events', ObservationKinds.E)
        add_series_containers('measurements', ObservationKinds.M)

        index_frame: pd.DataFrame = store.get('index') if store.get_node('index') is not None else pd.DataFrame([], columns=ObservationConcepts.base_columns())

        return factory.make(meta, events, measurements, index_frame=index_frame)
