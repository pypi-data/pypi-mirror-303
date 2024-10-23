from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Entity")


@_attrs_define
class Entity:
    """An entity like location, person, etc

    Attributes:
        uid (str): Unique identifier of the entity
        relevance (int): Relevance of the entity in the document
    """

    uid: str
    relevance: int

    def to_dict(self) -> Dict[str, Any]:
        uid = self.uid

        relevance = self.relevance

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "uid": uid,
                "relevance": relevance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uid = d.pop("uid")

        relevance = d.pop("relevance")

        entity = cls(
            uid=uid,
            relevance=relevance,
        )

        return entity
