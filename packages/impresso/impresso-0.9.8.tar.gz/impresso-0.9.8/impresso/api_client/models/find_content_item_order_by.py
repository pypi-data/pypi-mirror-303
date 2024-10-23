from enum import Enum
from typing import Literal


class FindContentItemOrderBy(str, Enum):
    DATE = "date"
    RELEVANCE = "relevance"
    VALUE_0 = "-date"
    VALUE_2 = "-relevance"

    def __str__(self) -> str:
        return str(self.value)


FindContentItemOrderByLiteral = Literal[
    "date",
    "relevance",
    "-date",
    "-relevance",
]
