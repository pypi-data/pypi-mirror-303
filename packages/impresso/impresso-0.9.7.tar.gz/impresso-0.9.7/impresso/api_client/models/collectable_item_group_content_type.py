from enum import Enum
from typing import Literal


class CollectableItemGroupContentType(str, Enum):
    A = "A"
    E = "E"
    I = "I"
    P = "P"

    def __str__(self) -> str:
        return str(self.value)


CollectableItemGroupContentTypeLiteral = Literal[
    "A",
    "E",
    "I",
    "P",
]
