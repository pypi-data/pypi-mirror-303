from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentItemMentionsItem")


@_attrs_define
class ContentItemMentionsItem:
    """
    Attributes:
        person (Union[Unset, List[List[int]]]):
        location (Union[Unset, List[List[int]]]):
    """

    person: Union[Unset, List[List[int]]] = UNSET
    location: Union[Unset, List[List[int]]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        person: Union[Unset, List[List[int]]] = UNSET
        if not isinstance(self.person, Unset):
            person = []
            for person_item_data in self.person:
                person_item = person_item_data

                person.append(person_item)

        location: Union[Unset, List[List[int]]] = UNSET
        if not isinstance(self.location, Unset):
            location = []
            for location_item_data in self.location:
                location_item = location_item_data

                location.append(location_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if person is not UNSET:
            field_dict["person"] = person
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        person = []
        _person = d.pop("person", UNSET)
        for person_item_data in _person or []:
            person_item = cast(List[int], person_item_data)

            person.append(person_item)

        location = []
        _location = d.pop("location", UNSET)
        for location_item_data in _location or []:
            location_item = cast(List[int], location_item_data)

            location.append(location_item)

        content_item_mentions_item = cls(
            person=person,
            location=location,
        )

        return content_item_mentions_item
