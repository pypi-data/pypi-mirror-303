from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopicRelatedTopicsItem")


@_attrs_define
class TopicRelatedTopicsItem:
    """
    Attributes:
        uid (str): The unique identifier of the related topic
        w (float): TODO
        avg (Union[Unset, float]): TODO
    """

    uid: str
    w: float
    avg: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        uid = self.uid

        w = self.w

        avg = self.avg

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "uid": uid,
                "w": w,
            }
        )
        if avg is not UNSET:
            field_dict["avg"] = avg

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uid = d.pop("uid")

        w = d.pop("w")

        avg = d.pop("avg", UNSET)

        topic_related_topics_item = cls(
            uid=uid,
            w=w,
            avg=avg,
        )

        return topic_related_topics_item
