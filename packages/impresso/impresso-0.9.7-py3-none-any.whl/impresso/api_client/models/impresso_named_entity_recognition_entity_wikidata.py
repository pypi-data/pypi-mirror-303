from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImpressoNamedEntityRecognitionEntityWikidata")


@_attrs_define
class ImpressoNamedEntityRecognitionEntityWikidata:
    """
    Attributes:
        id (str): Wikidata ID of the entity
        wikipedia_page_name (Union[Unset, str]): Wikipedia page name of the entity
    """

    id: str
    wikipedia_page_name: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        wikipedia_page_name = self.wikipedia_page_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )
        if wikipedia_page_name is not UNSET:
            field_dict["wikipediaPageName"] = wikipedia_page_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        wikipedia_page_name = d.pop("wikipediaPageName", UNSET)

        impresso_named_entity_recognition_entity_wikidata = cls(
            id=id,
            wikipedia_page_name=wikipedia_page_name,
        )

        return impresso_named_entity_recognition_entity_wikidata
