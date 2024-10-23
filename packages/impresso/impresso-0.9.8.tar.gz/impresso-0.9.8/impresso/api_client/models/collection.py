import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_user import BaseUser


T = TypeVar("T", bound="Collection")


@_attrs_define
class Collection:
    """Description of the collection object (Collection class)

    Attributes:
        uid (str):
        name (str):
        description (str):
        status (str):  Example: PRI.
        creation_date (datetime.datetime):
        last_modified_date (datetime.datetime):
        count_items (Union[int, str]):
        creator (BaseUser):
        labels (Union[Unset, List[str]]):
    """

    uid: str
    name: str
    description: str
    status: str
    creation_date: datetime.datetime
    last_modified_date: datetime.datetime
    count_items: Union[int, str]
    creator: "BaseUser"
    labels: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        uid = self.uid

        name = self.name

        description = self.description

        status = self.status

        creation_date = self.creation_date.isoformat()

        last_modified_date = self.last_modified_date.isoformat()

        count_items: Union[int, str]
        count_items = self.count_items

        creator = self.creator.to_dict()

        labels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "uid": uid,
                "name": name,
                "description": description,
                "status": status,
                "creationDate": creation_date,
                "lastModifiedDate": last_modified_date,
                "countItems": count_items,
                "creator": creator,
            }
        )
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_user import BaseUser

        d = src_dict.copy()
        uid = d.pop("uid")

        name = d.pop("name")

        description = d.pop("description")

        status = d.pop("status")

        creation_date = isoparse(d.pop("creationDate"))

        last_modified_date = isoparse(d.pop("lastModifiedDate"))

        def _parse_count_items(data: object) -> Union[int, str]:
            return cast(Union[int, str], data)

        count_items = _parse_count_items(d.pop("countItems"))

        creator = BaseUser.from_dict(d.pop("creator"))

        labels = cast(List[str], d.pop("labels", UNSET))

        collection = cls(
            uid=uid,
            name=name,
            description=description,
            status=status,
            creation_date=creation_date,
            last_modified_date=last_modified_date,
            count_items=count_items,
            creator=creator,
            labels=labels,
        )

        return collection
