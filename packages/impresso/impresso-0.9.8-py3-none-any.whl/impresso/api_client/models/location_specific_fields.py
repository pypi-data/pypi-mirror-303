from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.location_specific_fields_descriptions import LocationSpecificFieldsDescriptions
    from ..models.location_specific_fields_images_item import LocationSpecificFieldsImagesItem
    from ..models.location_specific_fields_labels import LocationSpecificFieldsLabels


T = TypeVar("T", bound="LocationSpecificFields")


@_attrs_define
class LocationSpecificFields:
    """Details of a wikidata entity

    Attributes:
        id (str):
        type (str):
        labels (LocationSpecificFieldsLabels): Labels of the entity. Key is the language code.
        descriptions (LocationSpecificFieldsDescriptions): Labels of the entity. Key is the language code.
        images (List['LocationSpecificFieldsImagesItem']):
    """

    id: str
    type: str
    labels: "LocationSpecificFieldsLabels"
    descriptions: "LocationSpecificFieldsDescriptions"
    images: List["LocationSpecificFieldsImagesItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type

        labels = self.labels.to_dict()

        descriptions = self.descriptions.to_dict()

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "labels": labels,
                "descriptions": descriptions,
                "images": images,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.location_specific_fields_descriptions import LocationSpecificFieldsDescriptions
        from ..models.location_specific_fields_images_item import LocationSpecificFieldsImagesItem
        from ..models.location_specific_fields_labels import LocationSpecificFieldsLabels

        d = src_dict.copy()
        id = d.pop("id")

        type = d.pop("type")

        labels = LocationSpecificFieldsLabels.from_dict(d.pop("labels"))

        descriptions = LocationSpecificFieldsDescriptions.from_dict(d.pop("descriptions"))

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = LocationSpecificFieldsImagesItem.from_dict(images_item_data)

            images.append(images_item)

        location_specific_fields = cls(
            id=id,
            type=type,
            labels=labels,
            descriptions=descriptions,
            images=images,
        )

        location_specific_fields.additional_properties = d
        return location_specific_fields

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
