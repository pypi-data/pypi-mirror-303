from enum import Enum
from typing import Literal


class FindTrClustersFacetsGroupBy(str, Enum):
    DATERANGE = "daterange"
    NEWSPAPER = "newspaper"
    TEXTREUSECLUSTERDAYDELTA = "textReuseClusterDayDelta"
    TEXTREUSECLUSTERLEXICALOVERLAP = "textReuseClusterLexicalOverlap"
    TEXTREUSECLUSTERSIZE = "textReuseClusterSize"

    def __str__(self) -> str:
        return str(self.value)


FindTrClustersFacetsGroupByLiteral = Literal[
    "daterange",
    "newspaper",
    "textReuseClusterDayDelta",
    "textReuseClusterLexicalOverlap",
    "textReuseClusterSize",
]
