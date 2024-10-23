from enum import Enum
from typing import Literal


class GetSearchFacetRangeInclude(str, Enum):
    ALL = "all"
    EDGE = "edge"
    UPPER = "upper"

    def __str__(self) -> str:
        return str(self.value)


GetSearchFacetRangeIncludeLiteral = Literal[
    "all",
    "edge",
    "upper",
]
