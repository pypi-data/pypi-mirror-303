from enum import Enum
from typing import Literal


class GetTrClustersFacetRangeInclude(str, Enum):
    ALL = "all"
    EDGE = "edge"
    UPPER = "upper"

    def __str__(self) -> str:
        return str(self.value)


GetTrClustersFacetRangeIncludeLiteral = Literal[
    "all",
    "edge",
    "upper",
]
