from enum import Enum
from typing import Literal


class FindContentItemResolve(str, Enum):
    COLLECTION = "collection"
    TAGS = "tags"

    def __str__(self) -> str:
        return str(self.value)


FindContentItemResolveLiteral = Literal[
    "collection",
    "tags",
]
