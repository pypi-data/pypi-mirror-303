from enum import Enum
from typing import Literal


class GetTrPassagesFacetRangeInclude(str, Enum):
    ALL = "all"
    EDGE = "edge"
    UPPER = "upper"

    def __str__(self) -> str:
        return str(self.value)


GetTrPassagesFacetRangeIncludeLiteral = Literal[
    "all",
    "edge",
    "upper",
]
