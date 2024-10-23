from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.collection import Collection
    from ..models.find_collections_response_200_info import FindCollectionsResponse200Info


T = TypeVar("T", bound="FindCollectionsResponse200")


@_attrs_define
class FindCollectionsResponse200:
    """
    Attributes:
        limit (int): The number of items returned in this response
        offset (int): Starting index of the items subset returned in this response
        total (int): The total number of items matching the query
        info (FindCollectionsResponse200Info): Additional information about the response.
        data (List['Collection']):
    """

    limit: int
    offset: int
    total: int
    info: "FindCollectionsResponse200Info"
    data: List["Collection"]

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
        from ..models.collection import Collection
        from ..models.find_collections_response_200_info import FindCollectionsResponse200Info

        d = src_dict.copy()
        limit = d.pop("limit")

        offset = d.pop("offset")

        total = d.pop("total")

        info = FindCollectionsResponse200Info.from_dict(d.pop("info"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Collection.from_dict(data_item_data)

            data.append(data_item)

        find_collections_response_200 = cls(
            limit=limit,
            offset=offset,
            total=total,
            info=info,
            data=data,
        )

        return find_collections_response_200
