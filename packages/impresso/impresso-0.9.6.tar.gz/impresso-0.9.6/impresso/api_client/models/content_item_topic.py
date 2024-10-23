from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topic import Topic


T = TypeVar("T", bound="ContentItemTopic")


@_attrs_define
class ContentItemTopic:
    """TODO

    Attributes:
        relevance (float): TODO
        topic (Union[Unset, Topic]): A topic (TODO)
        topic_uid (Union[Unset, str]): TODO
    """

    relevance: float
    topic: Union[Unset, "Topic"] = UNSET
    topic_uid: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        relevance = self.relevance

        topic: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.topic, Unset):
            topic = self.topic.to_dict()

        topic_uid = self.topic_uid

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "relevance": relevance,
            }
        )
        if topic is not UNSET:
            field_dict["topic"] = topic
        if topic_uid is not UNSET:
            field_dict["topicUid"] = topic_uid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.topic import Topic

        d = src_dict.copy()
        relevance = d.pop("relevance")

        _topic = d.pop("topic", UNSET)
        topic: Union[Unset, Topic]
        if isinstance(_topic, Unset):
            topic = UNSET
        else:
            topic = Topic.from_dict(_topic)

        topic_uid = d.pop("topicUid", UNSET)

        content_item_topic = cls(
            relevance=relevance,
            topic=topic,
            topic_uid=topic_uid,
        )

        return content_item_topic
