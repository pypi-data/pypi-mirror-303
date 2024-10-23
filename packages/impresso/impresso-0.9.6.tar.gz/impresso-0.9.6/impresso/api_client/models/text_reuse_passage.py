import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_reuse_passage_article_details import TextReusePassageArticleDetails
    from ..models.text_reuse_passage_cluster_details import TextReusePassageClusterDetails
    from ..models.text_reuse_passage_connected_clusters_item import TextReusePassageConnectedClustersItem
    from ..models.text_reuse_passage_issue import TextReusePassageIssue


T = TypeVar("T", bound="TextReusePassage")


@_attrs_define
class TextReusePassage:
    """Represents a passage of text that was identified as a part of a text reuse cluster

    Attributes:
        id (str): ID of the text reuse passage Example: abc123.
        article (TextReusePassageArticleDetails): Details of the article the passage belongs to
        text_reuse_cluster (TextReusePassageClusterDetails): Details of the cluster the passage belongs to
        offset_start (Union[None, int]):
        offset_end (Union[None, int]):
        content (str): Textual content of the passage
        title (str): Title of the content item (article) where this passage was found
        page_numbers (List[int]): Numbers of the pages where the passage was found
        collections (List[str]): Collection IDs the passage belongs to
        connected_clusters (Union[Unset, List['TextReusePassageConnectedClustersItem']]):
        is_front (Union[Unset, bool]): TBD
        size (Union[Unset, int]): Size of the passage
        newspaper (Union[Unset, Any]):
        issue (Union[Unset, TextReusePassageIssue]): Issue details
        date (Union[Unset, datetime.datetime]): Date of the item (article) where this passage was found
        page_regions (Union[Unset, List[str]]): Bounding box of the passage in the page
    """

    id: str
    article: "TextReusePassageArticleDetails"
    text_reuse_cluster: "TextReusePassageClusterDetails"
    offset_start: Union[None, int]
    offset_end: Union[None, int]
    content: str
    title: str
    page_numbers: List[int]
    collections: List[str]
    connected_clusters: Union[Unset, List["TextReusePassageConnectedClustersItem"]] = UNSET
    is_front: Union[Unset, bool] = UNSET
    size: Union[Unset, int] = UNSET
    newspaper: Union[Unset, Any] = UNSET
    issue: Union[Unset, "TextReusePassageIssue"] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    page_regions: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        article = self.article.to_dict()

        text_reuse_cluster = self.text_reuse_cluster.to_dict()

        offset_start: Union[None, int]
        offset_start = self.offset_start

        offset_end: Union[None, int]
        offset_end = self.offset_end

        content = self.content

        title = self.title

        page_numbers = self.page_numbers

        collections = self.collections

        connected_clusters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.connected_clusters, Unset):
            connected_clusters = []
            for connected_clusters_item_data in self.connected_clusters:
                connected_clusters_item = connected_clusters_item_data.to_dict()
                connected_clusters.append(connected_clusters_item)

        is_front = self.is_front

        size = self.size

        newspaper = self.newspaper

        issue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.issue, Unset):
            issue = self.issue.to_dict()

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        page_regions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.page_regions, Unset):
            page_regions = self.page_regions

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "article": article,
                "textReuseCluster": text_reuse_cluster,
                "offsetStart": offset_start,
                "offsetEnd": offset_end,
                "content": content,
                "title": title,
                "pageNumbers": page_numbers,
                "collections": collections,
            }
        )
        if connected_clusters is not UNSET:
            field_dict["connectedClusters"] = connected_clusters
        if is_front is not UNSET:
            field_dict["isFront"] = is_front
        if size is not UNSET:
            field_dict["size"] = size
        if newspaper is not UNSET:
            field_dict["newspaper"] = newspaper
        if issue is not UNSET:
            field_dict["issue"] = issue
        if date is not UNSET:
            field_dict["date"] = date
        if page_regions is not UNSET:
            field_dict["pageRegions"] = page_regions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.text_reuse_passage_article_details import TextReusePassageArticleDetails
        from ..models.text_reuse_passage_cluster_details import TextReusePassageClusterDetails
        from ..models.text_reuse_passage_connected_clusters_item import TextReusePassageConnectedClustersItem
        from ..models.text_reuse_passage_issue import TextReusePassageIssue

        d = src_dict.copy()
        id = d.pop("id")

        article = TextReusePassageArticleDetails.from_dict(d.pop("article"))

        text_reuse_cluster = TextReusePassageClusterDetails.from_dict(d.pop("textReuseCluster"))

        def _parse_offset_start(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        offset_start = _parse_offset_start(d.pop("offsetStart"))

        def _parse_offset_end(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        offset_end = _parse_offset_end(d.pop("offsetEnd"))

        content = d.pop("content")

        title = d.pop("title")

        page_numbers = cast(List[int], d.pop("pageNumbers"))

        collections = cast(List[str], d.pop("collections"))

        connected_clusters = []
        _connected_clusters = d.pop("connectedClusters", UNSET)
        for connected_clusters_item_data in _connected_clusters or []:
            connected_clusters_item = TextReusePassageConnectedClustersItem.from_dict(connected_clusters_item_data)

            connected_clusters.append(connected_clusters_item)

        is_front = d.pop("isFront", UNSET)

        size = d.pop("size", UNSET)

        newspaper = d.pop("newspaper", UNSET)

        _issue = d.pop("issue", UNSET)
        issue: Union[Unset, TextReusePassageIssue]
        if isinstance(_issue, Unset):
            issue = UNSET
        else:
            issue = TextReusePassageIssue.from_dict(_issue)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        page_regions = cast(List[str], d.pop("pageRegions", UNSET))

        text_reuse_passage = cls(
            id=id,
            article=article,
            text_reuse_cluster=text_reuse_cluster,
            offset_start=offset_start,
            offset_end=offset_end,
            content=content,
            title=title,
            page_numbers=page_numbers,
            collections=collections,
            connected_clusters=connected_clusters,
            is_front=is_front,
            size=size,
            newspaper=newspaper,
            issue=issue,
            date=date,
            page_regions=page_regions,
        )

        return text_reuse_passage
