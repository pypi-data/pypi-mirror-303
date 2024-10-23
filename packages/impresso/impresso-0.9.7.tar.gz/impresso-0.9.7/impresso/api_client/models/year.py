from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.year_weights import YearWeights


T = TypeVar("T", bound="Year")


@_attrs_define
class Year:
    """A year (TODO)

    Attributes:
        uid (Union[Unset, int]): Numeric representation of the year
        values (Union[Unset, YearWeights]): Total items counts within a year
        refs (Union[Unset, YearWeights]): Total items counts within a year
    """

    uid: Union[Unset, int] = UNSET
    values: Union[Unset, "YearWeights"] = UNSET
    refs: Union[Unset, "YearWeights"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        uid = self.uid

        values: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

        refs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.refs, Unset):
            refs = self.refs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if uid is not UNSET:
            field_dict["uid"] = uid
        if values is not UNSET:
            field_dict["values"] = values
        if refs is not UNSET:
            field_dict["refs"] = refs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.year_weights import YearWeights

        d = src_dict.copy()
        uid = d.pop("uid", UNSET)

        _values = d.pop("values", UNSET)
        values: Union[Unset, YearWeights]
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = YearWeights.from_dict(_values)

        _refs = d.pop("refs", UNSET)
        refs: Union[Unset, YearWeights]
        if isinstance(_refs, Unset):
            refs = UNSET
        else:
            refs = YearWeights.from_dict(_refs)

        year = cls(
            uid=uid,
            values=values,
            refs=refs,
        )

        return year
