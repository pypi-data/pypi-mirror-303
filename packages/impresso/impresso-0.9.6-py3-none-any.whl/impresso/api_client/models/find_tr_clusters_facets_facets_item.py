from enum import Enum
from typing import Literal


class FindTrClustersFacetsFacetsItem(str, Enum):
    DATERANGE = "daterange"
    NEWSPAPER = "newspaper"
    TEXTREUSECLUSTERDAYDELTA = "textReuseClusterDayDelta"
    TEXTREUSECLUSTERLEXICALOVERLAP = "textReuseClusterLexicalOverlap"
    TEXTREUSECLUSTERSIZE = "textReuseClusterSize"

    def __str__(self) -> str:
        return str(self.value)


FindTrClustersFacetsFacetsItemLiteral = Literal[
    "daterange",
    "newspaper",
    "textReuseClusterDayDelta",
    "textReuseClusterLexicalOverlap",
    "textReuseClusterSize",
]
