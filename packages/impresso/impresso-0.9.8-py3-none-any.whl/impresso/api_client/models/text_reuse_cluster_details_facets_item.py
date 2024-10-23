from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_reuse_cluster_details_facets_item_buckets_item import (
        TextReuseClusterDetailsFacetsItemBucketsItem,
    )


T = TypeVar("T", bound="TextReuseClusterDetailsFacetsItem")


@_attrs_define
class TextReuseClusterDetailsFacetsItem:
    """
    Attributes:
        type (Union[Unset, str]): Facet type
        num_buckets (Union[Unset, int]): Number of buckets
        buckets (Union[Unset, List['TextReuseClusterDetailsFacetsItemBucketsItem']]):
    """

    type: Union[Unset, str] = UNSET
    num_buckets: Union[Unset, int] = UNSET
    buckets: Union[Unset, List["TextReuseClusterDetailsFacetsItemBucketsItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        num_buckets = self.num_buckets

        buckets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.buckets, Unset):
            buckets = []
            for buckets_item_data in self.buckets:
                buckets_item = buckets_item_data.to_dict()
                buckets.append(buckets_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if num_buckets is not UNSET:
            field_dict["numBuckets"] = num_buckets
        if buckets is not UNSET:
            field_dict["buckets"] = buckets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.text_reuse_cluster_details_facets_item_buckets_item import (
            TextReuseClusterDetailsFacetsItemBucketsItem,
        )

        d = src_dict.copy()
        type = d.pop("type", UNSET)

        num_buckets = d.pop("numBuckets", UNSET)

        buckets = []
        _buckets = d.pop("buckets", UNSET)
        for buckets_item_data in _buckets or []:
            buckets_item = TextReuseClusterDetailsFacetsItemBucketsItem.from_dict(buckets_item_data)

            buckets.append(buckets_item)

        text_reuse_cluster_details_facets_item = cls(
            type=type,
            num_buckets=num_buckets,
            buckets=buckets,
        )

        return text_reuse_cluster_details_facets_item
