from enum import Enum
from typing import Literal


class GetTrClustersFacetGroupBy(str, Enum):
    DATERANGE = "daterange"
    NEWSPAPER = "newspaper"
    TEXTREUSECLUSTERDAYDELTA = "textReuseClusterDayDelta"
    TEXTREUSECLUSTERLEXICALOVERLAP = "textReuseClusterLexicalOverlap"
    TEXTREUSECLUSTERSIZE = "textReuseClusterSize"

    def __str__(self) -> str:
        return str(self.value)


GetTrClustersFacetGroupByLiteral = Literal[
    "daterange",
    "newspaper",
    "textReuseClusterDayDelta",
    "textReuseClusterLexicalOverlap",
    "textReuseClusterSize",
]
