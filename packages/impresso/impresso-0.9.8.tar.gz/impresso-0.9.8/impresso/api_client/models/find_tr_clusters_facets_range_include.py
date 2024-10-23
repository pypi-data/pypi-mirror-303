from enum import Enum
from typing import Literal


class FindTrClustersFacetsRangeInclude(str, Enum):
    ALL = "all"
    EDGE = "edge"
    UPPER = "upper"

    def __str__(self) -> str:
        return str(self.value)


FindTrClustersFacetsRangeIncludeLiteral = Literal[
    "all",
    "edge",
    "upper",
]
