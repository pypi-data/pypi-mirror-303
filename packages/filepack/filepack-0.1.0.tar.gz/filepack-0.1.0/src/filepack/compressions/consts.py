from typing import Final

GZIP_SUFFIX: Final[str] = "gz"
BZ2_SUFFIX: Final[str] = "bz2"
LZ4_SUFFIX: Final[str] = "lz4"
XZ_SUFFIX: Final[str] = "xz"

SUPPORTED_COMPRESSIONS_SUFFIXES: Final[list[str]] = [
    GZIP_SUFFIX,
    BZ2_SUFFIX,
    LZ4_SUFFIX,
    XZ_SUFFIX,
]
