from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_facet_bucket import SearchFacetBucket
    from ..models.search_facet_range_bucket import SearchFacetRangeBucket


T = TypeVar("T", bound="SearchFacet")


@_attrs_define
class SearchFacet:
    """An object containing search results for a facet

    Attributes:
        type (str): The type of facet
        num_buckets (int): The number of buckets in the facet
        buckets (Union[List['SearchFacetBucket'], List['SearchFacetRangeBucket']]):
        min_ (Union[Unset, Any]): TODO
        max_ (Union[Unset, Any]): TODO
        gap (Union[Unset, Any]): TODO
    """

    type: str
    num_buckets: int
    buckets: Union[List["SearchFacetBucket"], List["SearchFacetRangeBucket"]]
    min_: Union[Unset, Any] = UNSET
    max_: Union[Unset, Any] = UNSET
    gap: Union[Unset, Any] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        num_buckets = self.num_buckets

        buckets: List[Dict[str, Any]]
        if isinstance(self.buckets, list):
            buckets = []
            for buckets_type_0_item_data in self.buckets:
                buckets_type_0_item = buckets_type_0_item_data.to_dict()
                buckets.append(buckets_type_0_item)

        else:
            buckets = []
            for buckets_type_1_item_data in self.buckets:
                buckets_type_1_item = buckets_type_1_item_data.to_dict()
                buckets.append(buckets_type_1_item)

        min_ = self.min_

        max_ = self.max_

        gap = self.gap

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "numBuckets": num_buckets,
                "buckets": buckets,
            }
        )
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if gap is not UNSET:
            field_dict["gap"] = gap

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_facet_bucket import SearchFacetBucket
        from ..models.search_facet_range_bucket import SearchFacetRangeBucket

        d = src_dict.copy()
        type = d.pop("type")

        num_buckets = d.pop("numBuckets")

        def _parse_buckets(data: object) -> Union[List["SearchFacetBucket"], List["SearchFacetRangeBucket"]]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                buckets_type_0 = []
                _buckets_type_0 = data
                for buckets_type_0_item_data in _buckets_type_0:
                    buckets_type_0_item = SearchFacetBucket.from_dict(buckets_type_0_item_data)

                    buckets_type_0.append(buckets_type_0_item)

                return buckets_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            buckets_type_1 = []
            _buckets_type_1 = data
            for buckets_type_1_item_data in _buckets_type_1:
                buckets_type_1_item = SearchFacetRangeBucket.from_dict(buckets_type_1_item_data)

                buckets_type_1.append(buckets_type_1_item)

            return buckets_type_1

        buckets = _parse_buckets(d.pop("buckets"))

        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        gap = d.pop("gap", UNSET)

        search_facet = cls(
            type=type,
            num_buckets=num_buckets,
            buckets=buckets,
            min_=min_,
            max_=max_,
            gap=gap,
        )

        return search_facet
