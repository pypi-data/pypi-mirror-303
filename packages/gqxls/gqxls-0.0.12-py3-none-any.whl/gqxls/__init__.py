from . import (
    convert,
    path,
    information,
    network,
)

from .convert import (
    ConvertImage,
    ConvertPdf
)

from .path import (
    paths,
    is_empty,
    type_name,
    path_exists,
    type_same,
    file_maker,
    get_film,
    get_detail_film
)

from .information import (
    gain
)

from .network import (
    download
)

__all__ = [
    "__version__",
    "convert",
    "path",
    "information",
    "network",
    "ConvertImage",
    "ConvertPdf",
    "is_empty",
    "type_name",
    "path_exists",
    "type_same",
    "file_maker",
    "get_film",
    "get_detail_film",
    "paths",
    "gain",
    "download"
]

__name__="gqxls",
__version__ = '0.0.12'
__description__ = 'Consolidation package for daily use'
__author__ = 'S Liao'