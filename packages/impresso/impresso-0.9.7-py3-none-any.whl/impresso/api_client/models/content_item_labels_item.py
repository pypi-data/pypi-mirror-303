from enum import Enum
from typing import Literal


class ContentItemLabelsItem(str, Enum):
    ARTICLE = "article"

    def __str__(self) -> str:
        return str(self.value)


ContentItemLabelsItemLiteral = Literal["article",]
