from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchFacetRangeBucket")


@_attrs_define
class SearchFacetRangeBucket:
    """Facet bucket

    Attributes:
        count (int): Number of items in the bucket
        val (int): Value of the 'type' element
        lower (Union[Unset, int]): Lower bound of the range
        upper (Union[Unset, int]): Lower bound of the range
    """

    count: int
    val: int
    lower: Union[Unset, int] = UNSET
    upper: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        val = self.val

        lower = self.lower

        upper = self.upper

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "count": count,
                "val": val,
            }
        )
        if lower is not UNSET:
            field_dict["lower"] = lower
        if upper is not UNSET:
            field_dict["upper"] = upper

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count")

        val = d.pop("val")

        lower = d.pop("lower", UNSET)

        upper = d.pop("upper", UNSET)

        search_facet_range_bucket = cls(
            count=count,
            val=val,
            lower=lower,
            upper=upper,
        )

        return search_facet_range_bucket
