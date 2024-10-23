import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextReuseClusterTimeCoverage")


@_attrs_define
class TextReuseClusterTimeCoverage:
    """Time window covered by documents in the cluster

    Attributes:
        from_ (Union[Unset, datetime.date]):
        to (Union[Unset, datetime.date]):
    """

    from_: Union[Unset, datetime.date] = UNSET
    to: Union[Unset, datetime.date] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from_: Union[Unset, str] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: Union[Unset, str] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, datetime.date]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_).date()

        _to = d.pop("to", UNSET)
        to: Union[Unset, datetime.date]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to).date()

        text_reuse_cluster_time_coverage = cls(
            from_=from_,
            to=to,
        )

        return text_reuse_cluster_time_coverage
