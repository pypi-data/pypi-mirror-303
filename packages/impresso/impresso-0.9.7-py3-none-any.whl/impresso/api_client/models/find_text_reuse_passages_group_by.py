from enum import Enum
from typing import Literal


class FindTextReusePassagesGroupBy(str, Enum):
    TEXTREUSECLUSTERID = "textReuseClusterId"

    def __str__(self) -> str:
        return str(self.value)


FindTextReusePassagesGroupByLiteral = Literal["textReuseClusterId",]
