from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.find_tr_clusters_facets_response_200_info import FindTrClustersFacetsResponse200Info
    from ..models.search_facet import SearchFacet


T = TypeVar("T", bound="FindTrClustersFacetsResponse200")


@_attrs_define
class FindTrClustersFacetsResponse200:
    """
    Attributes:
        limit (int): The number of items returned in this response
        offset (int): Starting index of the items subset returned in this response
        total (int): The total number of items matching the query
        info (FindTrClustersFacetsResponse200Info): Additional information about the response.
        data (List['SearchFacet']):
    """

    limit: int
    offset: int
    total: int
    info: "FindTrClustersFacetsResponse200Info"
    data: List["SearchFacet"]

    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit

        offset = self.offset

        total = self.total

        info = self.info.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "limit": limit,
                "offset": offset,
                "total": total,
                "info": info,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.find_tr_clusters_facets_response_200_info import FindTrClustersFacetsResponse200Info
        from ..models.search_facet import SearchFacet

        d = src_dict.copy()
        limit = d.pop("limit")

        offset = d.pop("offset")

        total = d.pop("total")

        info = FindTrClustersFacetsResponse200Info.from_dict(d.pop("info"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = SearchFacet.from_dict(data_item_data)

            data.append(data_item)

        find_tr_clusters_facets_response_200 = cls(
            limit=limit,
            offset=offset,
            total=total,
            info=info,
            data=data,
        )

        return find_tr_clusters_facets_response_200
