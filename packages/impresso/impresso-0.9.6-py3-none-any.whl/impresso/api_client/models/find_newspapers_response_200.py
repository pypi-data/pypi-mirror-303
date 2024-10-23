from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.find_newspapers_response_200_info import FindNewspapersResponse200Info
    from ..models.newspaper import Newspaper


T = TypeVar("T", bound="FindNewspapersResponse200")


@_attrs_define
class FindNewspapersResponse200:
    """
    Attributes:
        limit (int): The number of items returned in this response
        offset (int): Starting index of the items subset returned in this response
        total (int): The total number of items matching the query
        info (FindNewspapersResponse200Info): Additional information about the response.
        data (List['Newspaper']):
    """

    limit: int
    offset: int
    total: int
    info: "FindNewspapersResponse200Info"
    data: List["Newspaper"]

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
        from ..models.find_newspapers_response_200_info import FindNewspapersResponse200Info
        from ..models.newspaper import Newspaper

        d = src_dict.copy()
        limit = d.pop("limit")

        offset = d.pop("offset")

        total = d.pop("total")

        info = FindNewspapersResponse200Info.from_dict(d.pop("info"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Newspaper.from_dict(data_item_data)

            data.append(data_item)

        find_newspapers_response_200 = cls(
            limit=limit,
            offset=offset,
            total=total,
            info=info,
            data=data,
        )

        return find_newspapers_response_200
