from enum import Enum
from typing import Literal


class FindSearchFacetsRangeInclude(str, Enum):
    ALL = "all"
    EDGE = "edge"
    UPPER = "upper"

    def __str__(self) -> str:
        return str(self.value)


FindSearchFacetsRangeIncludeLiteral = Literal[
    "all",
    "edge",
    "upper",
]
