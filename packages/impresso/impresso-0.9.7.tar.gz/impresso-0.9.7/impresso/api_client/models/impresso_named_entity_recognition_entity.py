from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.impresso_named_entity_recognition_entity_type import ImpressoNamedEntityRecognitionEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impresso_named_entity_recognition_entity_confidence import (
        ImpressoNamedEntityRecognitionEntityConfidence,
    )
    from ..models.impresso_named_entity_recognition_entity_offset import ImpressoNamedEntityRecognitionEntityOffset
    from ..models.impresso_named_entity_recognition_entity_wikidata import ImpressoNamedEntityRecognitionEntityWikidata


T = TypeVar("T", bound="ImpressoNamedEntityRecognitionEntity")


@_attrs_define
class ImpressoNamedEntityRecognitionEntity:
    """Impresso NER entity

    Attributes:
        id (str): ID of the entity
        type (ImpressoNamedEntityRecognitionEntityType): Type of the entity
        surface_form (str): Surface form of the entity
        offset (ImpressoNamedEntityRecognitionEntityOffset):
        confidence (ImpressoNamedEntityRecognitionEntityConfidence):
        is_type_nested (Union[Unset, bool]): Whether the entity type is nested
        wikidata (Union[Unset, ImpressoNamedEntityRecognitionEntityWikidata]):
        function (Union[Unset, str]): Function of the entity
        name (Union[Unset, str]): Name of the entity
    """

    id: str
    type: ImpressoNamedEntityRecognitionEntityType
    surface_form: str
    offset: "ImpressoNamedEntityRecognitionEntityOffset"
    confidence: "ImpressoNamedEntityRecognitionEntityConfidence"
    is_type_nested: Union[Unset, bool] = UNSET
    wikidata: Union[Unset, "ImpressoNamedEntityRecognitionEntityWikidata"] = UNSET
    function: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type = self.type.value

        surface_form = self.surface_form

        offset = self.offset.to_dict()

        confidence = self.confidence.to_dict()

        is_type_nested = self.is_type_nested

        wikidata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.wikidata, Unset):
            wikidata = self.wikidata.to_dict()

        function = self.function

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "type": type,
                "surfaceForm": surface_form,
                "offset": offset,
                "confidence": confidence,
            }
        )
        if is_type_nested is not UNSET:
            field_dict["isTypeNested"] = is_type_nested
        if wikidata is not UNSET:
            field_dict["wikidata"] = wikidata
        if function is not UNSET:
            field_dict["function"] = function
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.impresso_named_entity_recognition_entity_confidence import (
            ImpressoNamedEntityRecognitionEntityConfidence,
        )
        from ..models.impresso_named_entity_recognition_entity_offset import ImpressoNamedEntityRecognitionEntityOffset
        from ..models.impresso_named_entity_recognition_entity_wikidata import (
            ImpressoNamedEntityRecognitionEntityWikidata,
        )

        d = src_dict.copy()
        id = d.pop("id")

        type = ImpressoNamedEntityRecognitionEntityType(d.pop("type"))

        surface_form = d.pop("surfaceForm")

        offset = ImpressoNamedEntityRecognitionEntityOffset.from_dict(d.pop("offset"))

        confidence = ImpressoNamedEntityRecognitionEntityConfidence.from_dict(d.pop("confidence"))

        is_type_nested = d.pop("isTypeNested", UNSET)

        _wikidata = d.pop("wikidata", UNSET)
        wikidata: Union[Unset, ImpressoNamedEntityRecognitionEntityWikidata]
        if isinstance(_wikidata, Unset):
            wikidata = UNSET
        else:
            wikidata = ImpressoNamedEntityRecognitionEntityWikidata.from_dict(_wikidata)

        function = d.pop("function", UNSET)

        name = d.pop("name", UNSET)

        impresso_named_entity_recognition_entity = cls(
            id=id,
            type=type,
            surface_form=surface_form,
            offset=offset,
            confidence=confidence,
            is_type_nested=is_type_nested,
            wikidata=wikidata,
            function=function,
            name=name,
        )

        return impresso_named_entity_recognition_entity
