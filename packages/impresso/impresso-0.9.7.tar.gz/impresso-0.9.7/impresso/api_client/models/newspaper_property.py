from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewspaperProperty")


@_attrs_define
class NewspaperProperty:
    """
    Attributes:
        name (str): The name of the property
        value (str): The value of the property
        label (str): The label of the property
        is_url (Union[Unset, bool]): Whether the value is a URL
    """

    name: str
    value: str
    label: str
    is_url: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        value = self.value

        label = self.label

        is_url = self.is_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
                "label": label,
            }
        )
        if is_url is not UNSET:
            field_dict["isUrl"] = is_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        value = d.pop("value")

        label = d.pop("label")

        is_url = d.pop("isUrl", UNSET)

        newspaper_property = cls(
            name=name,
            value=value,
            label=label,
            is_url=is_url,
        )

        newspaper_property.additional_properties = d
        return newspaper_property

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
