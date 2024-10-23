from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TextReusePassageArticleDetails")


@_attrs_define
class TextReusePassageArticleDetails:
    """Details of the article the passage belongs to

    Attributes:
        id (str): ID of the article
    """

    id: str

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        text_reuse_passage_article_details = cls(
            id=id,
        )

        return text_reuse_passage_article_details
