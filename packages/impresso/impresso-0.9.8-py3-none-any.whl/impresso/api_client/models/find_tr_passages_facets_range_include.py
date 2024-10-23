from enum import Enum
from typing import Literal


class FindTrPassagesFacetsRangeInclude(str, Enum):
    ALL = "all"
    EDGE = "edge"
    UPPER = "upper"

    def __str__(self) -> str:
        return str(self.value)


FindTrPassagesFacetsRangeIncludeLiteral = Literal[
    "all",
    "edge",
    "upper",
]
