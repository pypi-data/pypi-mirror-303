from typing import Literal
# noinspection PyUnresolvedReferences
from .shared import HeaderFormatLiterals, HeaderFileFormats
from ..core.util import StringEnumeration


class ExportFormats(StringEnumeration):
    CSV = 'csv'
    HDF = 'h5'

class ExportFormatsV2(StringEnumeration):
    FOLDER = 'folder'
    ZIP = 'zip'

ExportFormatLiterals = Literal['csv', 'h5']
ExportFormatLiteralsV2 = Literal['folder', 'zip']
