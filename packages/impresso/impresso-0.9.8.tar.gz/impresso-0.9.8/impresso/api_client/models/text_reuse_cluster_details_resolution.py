from enum import Enum
from typing import Literal


class TextReuseClusterDetailsResolution(str, Enum):
    DAY = "day"
    MONTH = "month"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)


TextReuseClusterDetailsResolutionLiteral = Literal[
    "day",
    "month",
    "year",
]
