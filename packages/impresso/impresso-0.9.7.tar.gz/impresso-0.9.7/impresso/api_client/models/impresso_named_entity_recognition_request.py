from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ImpressoNamedEntityRecognitionRequest")


@_attrs_define
class ImpressoNamedEntityRecognitionRequest:
    """Request body for the Impresso NER endpoint

    Attributes:
        text (str): Text to be processed for named entity recognition
    """

    text: str

    def to_dict(self) -> Dict[str, Any]:
        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        impresso_named_entity_recognition_request = cls(
            text=text,
        )

        return impresso_named_entity_recognition_request
