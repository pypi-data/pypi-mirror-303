from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewCollection")


@_attrs_define
class NewCollection:
    """Create new collection request

    Attributes:
        name (str):
        description (Union[Unset, str]):
        status (Union[Unset, str]):  Example: PRI.
    """

    name: str
    description: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description", UNSET)

        status = d.pop("status", UNSET)

        new_collection = cls(
            name=name,
            description=description,
            status=status,
        )

        return new_collection
