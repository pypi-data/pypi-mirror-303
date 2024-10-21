This is the 'official' machine data/measurement and event data (MAED) format package.

It supports csv importing, exporting and format compliance checking.
Machine data files can be parsed into a python object that provides typed views on the contained measurement and event timeseries.

Some (slightly out of date) examples:

`validation.py` in `files/input/extension_testing` 
```python
from mdata.core import as_v2
from mdata.io import write_machine_data_v2, read_machine_data_zip, write_machine_data_zip
from mdata.io.util import HeaderFileFormats, mk_canon_filenames_v2

md = read_machine_data_zip('md.zip', header_format=HeaderFileFormats.CSV)
write_machine_data_zip('md_test.zip', md, header_format=HeaderFileFormats.CSV)
write_machine_data_v2(mk_canon_filenames_v2('test/', header_format=HeaderFileFormats.CSV), md, header_format=HeaderFileFormats.CSV)

as_v2(md)

print(md.event_specs)
print(md.measurement_specs)
print(md.segment_specs)
print(md.segment_data_specs)
print()
print(md.observation_index)
print(md.segments.df)
```
