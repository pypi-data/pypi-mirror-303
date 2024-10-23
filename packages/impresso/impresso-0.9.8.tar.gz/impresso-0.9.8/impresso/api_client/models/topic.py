from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topic_related_topics_item import TopicRelatedTopicsItem
    from ..models.topic_word import TopicWord


T = TypeVar("T", bound="Topic")


@_attrs_define
class Topic:
    """A topic (TODO)

    Attributes:
        uid (str): The unique identifier of the topic
        language (str): The language code of the topic
        community (Union[Unset, str]): TODO
        pagerank (Union[Unset, float]): TODO
        degree (Union[Unset, float]): TODO
        x (Union[Unset, float]): TODO
        y (Union[Unset, float]): TODO
        related_topics (Union[Unset, List['TopicRelatedTopicsItem']]):
        count_items (Union[Unset, float]): TODO
        excerpt (Union[Unset, List['TopicWord']]): TODO
        words (Union[Unset, List['TopicWord']]): TODO
        model (Union[Unset, str]): ID of the model used to generate the topic
    """

    uid: str
    language: str
    community: Union[Unset, str] = UNSET
    pagerank: Union[Unset, float] = UNSET
    degree: Union[Unset, float] = UNSET
    x: Union[Unset, float] = UNSET
    y: Union[Unset, float] = UNSET
    related_topics: Union[Unset, List["TopicRelatedTopicsItem"]] = UNSET
    count_items: Union[Unset, float] = UNSET
    excerpt: Union[Unset, List["TopicWord"]] = UNSET
    words: Union[Unset, List["TopicWord"]] = UNSET
    model: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        uid = self.uid

        language = self.language

        community = self.community

        pagerank = self.pagerank

        degree = self.degree

        x = self.x

        y = self.y

        related_topics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.related_topics, Unset):
            related_topics = []
            for related_topics_item_data in self.related_topics:
                related_topics_item = related_topics_item_data.to_dict()
                related_topics.append(related_topics_item)

        count_items = self.count_items

        excerpt: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.excerpt, Unset):
            excerpt = []
            for excerpt_item_data in self.excerpt:
                excerpt_item = excerpt_item_data.to_dict()
                excerpt.append(excerpt_item)

        words: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.words, Unset):
            words = []
            for words_item_data in self.words:
                words_item = words_item_data.to_dict()
                words.append(words_item)

        model = self.model

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "uid": uid,
                "language": language,
            }
        )
        if community is not UNSET:
            field_dict["community"] = community
        if pagerank is not UNSET:
            field_dict["pagerank"] = pagerank
        if degree is not UNSET:
            field_dict["degree"] = degree
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if related_topics is not UNSET:
            field_dict["relatedTopics"] = related_topics
        if count_items is not UNSET:
            field_dict["countItems"] = count_items
        if excerpt is not UNSET:
            field_dict["excerpt"] = excerpt
        if words is not UNSET:
            field_dict["words"] = words
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.topic_related_topics_item import TopicRelatedTopicsItem
        from ..models.topic_word import TopicWord

        d = src_dict.copy()
        uid = d.pop("uid")

        language = d.pop("language")

        community = d.pop("community", UNSET)

        pagerank = d.pop("pagerank", UNSET)

        degree = d.pop("degree", UNSET)

        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        related_topics = []
        _related_topics = d.pop("relatedTopics", UNSET)
        for related_topics_item_data in _related_topics or []:
            related_topics_item = TopicRelatedTopicsItem.from_dict(related_topics_item_data)

            related_topics.append(related_topics_item)

        count_items = d.pop("countItems", UNSET)

        excerpt = []
        _excerpt = d.pop("excerpt", UNSET)
        for excerpt_item_data in _excerpt or []:
            excerpt_item = TopicWord.from_dict(excerpt_item_data)

            excerpt.append(excerpt_item)

        words = []
        _words = d.pop("words", UNSET)
        for words_item_data in _words or []:
            words_item = TopicWord.from_dict(words_item_data)

            words.append(words_item)

        model = d.pop("model", UNSET)

        topic = cls(
            uid=uid,
            language=language,
            community=community,
            pagerank=pagerank,
            degree=degree,
            x=x,
            y=y,
            related_topics=related_topics,
            count_items=count_items,
            excerpt=excerpt,
            words=words,
            model=model,
        )

        return topic
