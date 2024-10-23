from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.entity_details_type import EntityDetailsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_specific_fields import LocationSpecificFields


T = TypeVar("T", bound="EntityDetails")


@_attrs_define
class EntityDetails:
    """An entity like location, person, etc

    Attributes:
        uid (str): Unique identifier of the entity
        name (str): Entity name
        type (EntityDetailsType):
        count_items (int): TODO
        count_mentions (int): Number of mentions of this entity in articles
        wikidata_id (Union[Unset, str]): ID of the entity in wikidata
        wikidata (Union[Unset, LocationSpecificFields]): Details of a wikidata entity
    """

    uid: str
    name: str
    type: EntityDetailsType
    count_items: int
    count_mentions: int
    wikidata_id: Union[Unset, str] = UNSET
    wikidata: Union[Unset, "LocationSpecificFields"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        uid = self.uid

        name = self.name

        type = self.type.value

        count_items = self.count_items

        count_mentions = self.count_mentions

        wikidata_id = self.wikidata_id

        wikidata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.wikidata, Unset):
            wikidata = self.wikidata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "uid": uid,
                "name": name,
                "type": type,
                "countItems": count_items,
                "countMentions": count_mentions,
            }
        )
        if wikidata_id is not UNSET:
            field_dict["wikidataId"] = wikidata_id
        if wikidata is not UNSET:
            field_dict["wikidata"] = wikidata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.location_specific_fields import LocationSpecificFields

        d = src_dict.copy()
        uid = d.pop("uid")

        name = d.pop("name")

        type = EntityDetailsType(d.pop("type"))

        count_items = d.pop("countItems")

        count_mentions = d.pop("countMentions")

        wikidata_id = d.pop("wikidataId", UNSET)

        _wikidata = d.pop("wikidata", UNSET)
        wikidata: Union[Unset, LocationSpecificFields]
        if isinstance(_wikidata, Unset):
            wikidata = UNSET
        else:
            wikidata = LocationSpecificFields.from_dict(_wikidata)

        entity_details = cls(
            uid=uid,
            name=name,
            type=type,
            count_items=count_items,
            count_mentions=count_mentions,
            wikidata_id=wikidata_id,
            wikidata=wikidata,
        )

        return entity_details
