from enum import Enum
from typing import Literal


class FindNewspapersOrderBy(str, Enum):
    COUNTISSUES = "countIssues"
    ENDYEAR = "endYear"
    FIRSTISSUE = "firstIssue"
    LASTISSUE = "lastIssue"
    NAME = "name"
    STARTYEAR = "startYear"
    VALUE_0 = "-name"
    VALUE_11 = "-countIssues"
    VALUE_2 = "-startYear"
    VALUE_4 = "-endYear"
    VALUE_7 = "-firstIssue"
    VALUE_9 = "-lastIssue"

    def __str__(self) -> str:
        return str(self.value)


FindNewspapersOrderByLiteral = Literal[
    "countIssues",
    "endYear",
    "firstIssue",
    "lastIssue",
    "name",
    "startYear",
    "-name",
    "-countIssues",
    "-startYear",
    "-endYear",
    "-firstIssue",
    "-lastIssue",
]
