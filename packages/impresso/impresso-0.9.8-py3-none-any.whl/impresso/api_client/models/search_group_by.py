from enum import Enum
from typing import Literal


class SearchGroupBy(str, Enum):
    ARTICLES = "articles"
    RAW = "raw"

    def __str__(self) -> str:
        return str(self.value)


SearchGroupByLiteral = Literal[
    "articles",
    "raw",
]
