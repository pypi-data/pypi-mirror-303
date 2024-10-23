import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.content_item_access_right import ContentItemAccessRight
from ..models.content_item_labels_item import ContentItemLabelsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection import Collection
    from ..models.content_item_match import ContentItemMatch
    from ..models.content_item_mentions_item import ContentItemMentionsItem
    from ..models.content_item_region import ContentItemRegion
    from ..models.content_item_topic import ContentItemTopic
    from ..models.entity import Entity
    from ..models.newspaper import Newspaper
    from ..models.newspaper_issue import NewspaperIssue
    from ..models.page import Page


T = TypeVar("T", bound="ContentItem")


@_attrs_define
class ContentItem:
    """A journal/magazine content item (article, advertisement, etc.)

    Attributes:
        uid (str): The unique identifier of the content item
        type (str): The type of the content item. NOTE: may be empty.
        title (str): The title of the content item
        size (int): The size of the content item in characters
        nb_pages (int): The number of pages in this content item
        pages (List['Page']):
        is_cc (bool): TODO
        excerpt (str): The excerpt of the content item
        labels (List[ContentItemLabelsItem]): TODO
        access_right (ContentItemAccessRight):
        year (int): The year of the content item
        locations (Union[Unset, List['Entity']]):
        persons (Union[Unset, List['Entity']]):
        language (Union[Unset, str]): The language code of the content item
        issue (Union[Unset, NewspaperIssue]):
        matches (Union[Unset, List['ContentItemMatch']]):
        regions (Union[Unset, List['ContentItemRegion']]):
        region_breaks (Union[Unset, List[int]]):
        content_line_breaks (Union[Unset, List[int]]):
        is_front (Union[Unset, bool]): TODO
        date (Union[None, Unset, datetime.datetime]):
        country (Union[Unset, str]): The country code of the content item
        tags (Union[Unset, List[str]]):
        collections (Union[List['Collection'], List[str], Unset]):
        newspaper (Union[Unset, Newspaper]): A newspaper
        data_provider (Union[None, Unset, str]):
        topics (Union[Unset, List['ContentItemTopic']]):
        content (Union[Unset, str]): The content of the content item
        mentions (Union[Unset, List['ContentItemMentionsItem']]):
        v (Union[Unset, str]): TODO
    """

    uid: str
    type: str
    title: str
    size: int
    nb_pages: int
    pages: List["Page"]
    is_cc: bool
    excerpt: str
    labels: List[ContentItemLabelsItem]
    access_right: ContentItemAccessRight
    year: int
    locations: Union[Unset, List["Entity"]] = UNSET
    persons: Union[Unset, List["Entity"]] = UNSET
    language: Union[Unset, str] = UNSET
    issue: Union[Unset, "NewspaperIssue"] = UNSET
    matches: Union[Unset, List["ContentItemMatch"]] = UNSET
    regions: Union[Unset, List["ContentItemRegion"]] = UNSET
    region_breaks: Union[Unset, List[int]] = UNSET
    content_line_breaks: Union[Unset, List[int]] = UNSET
    is_front: Union[Unset, bool] = UNSET
    date: Union[None, Unset, datetime.datetime] = UNSET
    country: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    collections: Union[List["Collection"], List[str], Unset] = UNSET
    newspaper: Union[Unset, "Newspaper"] = UNSET
    data_provider: Union[None, Unset, str] = UNSET
    topics: Union[Unset, List["ContentItemTopic"]] = UNSET
    content: Union[Unset, str] = UNSET
    mentions: Union[Unset, List["ContentItemMentionsItem"]] = UNSET
    v: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        uid = self.uid

        type = self.type

        title = self.title

        size = self.size

        nb_pages = self.nb_pages

        pages = []
        for pages_item_data in self.pages:
            pages_item = pages_item_data.to_dict()
            pages.append(pages_item)

        is_cc = self.is_cc

        excerpt = self.excerpt

        labels = []
        for labels_item_data in self.labels:
            labels_item = labels_item_data.value
            labels.append(labels_item)

        access_right = self.access_right.value

        year = self.year

        locations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)

        persons: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.persons, Unset):
            persons = []
            for persons_item_data in self.persons:
                persons_item = persons_item_data.to_dict()
                persons.append(persons_item)

        language = self.language

        issue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.issue, Unset):
            issue = self.issue.to_dict()

        matches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.matches, Unset):
            matches = []
            for matches_item_data in self.matches:
                matches_item = matches_item_data.to_dict()
                matches.append(matches_item)

        regions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.regions, Unset):
            regions = []
            for regions_item_data in self.regions:
                regions_item = regions_item_data.to_dict()
                regions.append(regions_item)

        region_breaks: Union[Unset, List[int]] = UNSET
        if not isinstance(self.region_breaks, Unset):
            region_breaks = self.region_breaks

        content_line_breaks: Union[Unset, List[int]] = UNSET
        if not isinstance(self.content_line_breaks, Unset):
            content_line_breaks = self.content_line_breaks

        is_front = self.is_front

        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        country = self.country

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        collections: Union[List[Dict[str, Any]], List[str], Unset]
        if isinstance(self.collections, Unset):
            collections = UNSET
        elif isinstance(self.collections, list):
            collections = self.collections

        else:
            collections = []
            for collections_type_1_item_data in self.collections:
                collections_type_1_item = collections_type_1_item_data.to_dict()
                collections.append(collections_type_1_item)

        newspaper: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.newspaper, Unset):
            newspaper = self.newspaper.to_dict()

        data_provider: Union[None, Unset, str]
        if isinstance(self.data_provider, Unset):
            data_provider = UNSET
        else:
            data_provider = self.data_provider

        topics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.topics, Unset):
            topics = []
            for topics_item_data in self.topics:
                topics_item = topics_item_data.to_dict()
                topics.append(topics_item)

        content = self.content

        mentions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.mentions, Unset):
            mentions = []
            for mentions_item_data in self.mentions:
                mentions_item = mentions_item_data.to_dict()
                mentions.append(mentions_item)

        v = self.v

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "uid": uid,
                "type": type,
                "title": title,
                "size": size,
                "nbPages": nb_pages,
                "pages": pages,
                "isCC": is_cc,
                "excerpt": excerpt,
                "labels": labels,
                "accessRight": access_right,
                "year": year,
            }
        )
        if locations is not UNSET:
            field_dict["locations"] = locations
        if persons is not UNSET:
            field_dict["persons"] = persons
        if language is not UNSET:
            field_dict["language"] = language
        if issue is not UNSET:
            field_dict["issue"] = issue
        if matches is not UNSET:
            field_dict["matches"] = matches
        if regions is not UNSET:
            field_dict["regions"] = regions
        if region_breaks is not UNSET:
            field_dict["regionBreaks"] = region_breaks
        if content_line_breaks is not UNSET:
            field_dict["contentLineBreaks"] = content_line_breaks
        if is_front is not UNSET:
            field_dict["isFront"] = is_front
        if date is not UNSET:
            field_dict["date"] = date
        if country is not UNSET:
            field_dict["country"] = country
        if tags is not UNSET:
            field_dict["tags"] = tags
        if collections is not UNSET:
            field_dict["collections"] = collections
        if newspaper is not UNSET:
            field_dict["newspaper"] = newspaper
        if data_provider is not UNSET:
            field_dict["dataProvider"] = data_provider
        if topics is not UNSET:
            field_dict["topics"] = topics
        if content is not UNSET:
            field_dict["content"] = content
        if mentions is not UNSET:
            field_dict["mentions"] = mentions
        if v is not UNSET:
            field_dict["v"] = v

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.collection import Collection
        from ..models.content_item_match import ContentItemMatch
        from ..models.content_item_mentions_item import ContentItemMentionsItem
        from ..models.content_item_region import ContentItemRegion
        from ..models.content_item_topic import ContentItemTopic
        from ..models.entity import Entity
        from ..models.newspaper import Newspaper
        from ..models.newspaper_issue import NewspaperIssue
        from ..models.page import Page

        d = src_dict.copy()
        uid = d.pop("uid")

        type = d.pop("type")

        title = d.pop("title")

        size = d.pop("size")

        nb_pages = d.pop("nbPages")

        pages = []
        _pages = d.pop("pages")
        for pages_item_data in _pages:
            pages_item = Page.from_dict(pages_item_data)

            pages.append(pages_item)

        is_cc = d.pop("isCC")

        excerpt = d.pop("excerpt")

        labels = []
        _labels = d.pop("labels")
        for labels_item_data in _labels:
            labels_item = ContentItemLabelsItem(labels_item_data)

            labels.append(labels_item)

        access_right = ContentItemAccessRight(d.pop("accessRight"))

        year = d.pop("year")

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = Entity.from_dict(locations_item_data)

            locations.append(locations_item)

        persons = []
        _persons = d.pop("persons", UNSET)
        for persons_item_data in _persons or []:
            persons_item = Entity.from_dict(persons_item_data)

            persons.append(persons_item)

        language = d.pop("language", UNSET)

        _issue = d.pop("issue", UNSET)
        issue: Union[Unset, NewspaperIssue]
        if isinstance(_issue, Unset):
            issue = UNSET
        else:
            issue = NewspaperIssue.from_dict(_issue)

        matches = []
        _matches = d.pop("matches", UNSET)
        for matches_item_data in _matches or []:
            matches_item = ContentItemMatch.from_dict(matches_item_data)

            matches.append(matches_item)

        regions = []
        _regions = d.pop("regions", UNSET)
        for regions_item_data in _regions or []:
            regions_item = ContentItemRegion.from_dict(regions_item_data)

            regions.append(regions_item)

        region_breaks = cast(List[int], d.pop("regionBreaks", UNSET))

        content_line_breaks = cast(List[int], d.pop("contentLineBreaks", UNSET))

        is_front = d.pop("isFront", UNSET)

        def _parse_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0_type_0 = isoparse(data)

                return date_type_0_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date = _parse_date(d.pop("date", UNSET))

        country = d.pop("country", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        def _parse_collections(data: object) -> Union[List["Collection"], List[str], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collections_type_0 = cast(List[str], data)

                return collections_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            collections_type_1 = []
            _collections_type_1 = data
            for collections_type_1_item_data in _collections_type_1:
                collections_type_1_item = Collection.from_dict(collections_type_1_item_data)

                collections_type_1.append(collections_type_1_item)

            return collections_type_1

        collections = _parse_collections(d.pop("collections", UNSET))

        _newspaper = d.pop("newspaper", UNSET)
        newspaper: Union[Unset, Newspaper]
        if isinstance(_newspaper, Unset):
            newspaper = UNSET
        else:
            newspaper = Newspaper.from_dict(_newspaper)

        def _parse_data_provider(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        data_provider = _parse_data_provider(d.pop("dataProvider", UNSET))

        topics = []
        _topics = d.pop("topics", UNSET)
        for topics_item_data in _topics or []:
            topics_item = ContentItemTopic.from_dict(topics_item_data)

            topics.append(topics_item)

        content = d.pop("content", UNSET)

        mentions = []
        _mentions = d.pop("mentions", UNSET)
        for mentions_item_data in _mentions or []:
            mentions_item = ContentItemMentionsItem.from_dict(mentions_item_data)

            mentions.append(mentions_item)

        v = d.pop("v", UNSET)

        content_item = cls(
            uid=uid,
            type=type,
            title=title,
            size=size,
            nb_pages=nb_pages,
            pages=pages,
            is_cc=is_cc,
            excerpt=excerpt,
            labels=labels,
            access_right=access_right,
            year=year,
            locations=locations,
            persons=persons,
            language=language,
            issue=issue,
            matches=matches,
            regions=regions,
            region_breaks=region_breaks,
            content_line_breaks=content_line_breaks,
            is_front=is_front,
            date=date,
            country=country,
            tags=tags,
            collections=collections,
            newspaper=newspaper,
            data_provider=data_provider,
            topics=topics,
            content=content,
            mentions=mentions,
            v=v,
        )

        return content_item
