import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewspaperIssue")


@_attrs_define
class NewspaperIssue:
    """
    Attributes:
        uid (str): The unique identifier of the issue
        cover (str): TODO
        labels (List[str]): The labels of the issue
        fresh (bool): TODO
        access_rights (str): TODO: list available options
        date (Union[Unset, datetime.datetime]): The date of the issue
        year (Union[Unset, str]): The year of the issue
    """

    uid: str
    cover: str
    labels: List[str]
    fresh: bool
    access_rights: str
    date: Union[Unset, datetime.datetime] = UNSET
    year: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        uid = self.uid

        cover = self.cover

        labels = self.labels

        fresh = self.fresh

        access_rights = self.access_rights

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        year = self.year

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "uid": uid,
                "cover": cover,
                "labels": labels,
                "fresh": fresh,
                "accessRights": access_rights,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uid = d.pop("uid")

        cover = d.pop("cover")

        labels = cast(List[str], d.pop("labels"))

        fresh = d.pop("fresh")

        access_rights = d.pop("accessRights")

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        year = d.pop("year", UNSET)

        newspaper_issue = cls(
            uid=uid,
            cover=cover,
            labels=labels,
            fresh=fresh,
            access_rights=access_rights,
            date=date,
            year=year,
        )

        return newspaper_issue
