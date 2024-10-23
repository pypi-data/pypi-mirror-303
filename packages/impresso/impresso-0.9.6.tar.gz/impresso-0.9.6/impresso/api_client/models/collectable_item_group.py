import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.collectable_item_group_content_type import CollectableItemGroupContentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection import Collection


T = TypeVar("T", bound="CollectableItemGroup")


@_attrs_define
class CollectableItemGroup:
    """Collectable item group object

    Attributes:
        item_id (Union[Unset, str]): The id of the collectable item group
        content_type (Union[Unset, CollectableItemGroupContentType]): Content type of the collectable item group:
            (A)rticle, (E)ntities, (P)ages, (I)ssues
        collection_ids (Union[Unset, List[str]]): Ids of the collections
        search_queries (Union[Unset, List[str]]): Search queries
        collections (Union[Unset, List['Collection']]): Collection objects
        latest_date_added (Union[Unset, datetime.datetime]): The latest date added to the collectable item group
    """

    item_id: Union[Unset, str] = UNSET
    content_type: Union[Unset, CollectableItemGroupContentType] = UNSET
    collection_ids: Union[Unset, List[str]] = UNSET
    search_queries: Union[Unset, List[str]] = UNSET
    collections: Union[Unset, List["Collection"]] = UNSET
    latest_date_added: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_id = self.item_id

        content_type: Union[Unset, str] = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.value

        collection_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.collection_ids, Unset):
            collection_ids = self.collection_ids

        search_queries: Union[Unset, List[str]] = UNSET
        if not isinstance(self.search_queries, Unset):
            search_queries = self.search_queries

        collections: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.collections, Unset):
            collections = []
            for collections_item_data in self.collections:
                collections_item = collections_item_data.to_dict()
                collections.append(collections_item)

        latest_date_added: Union[Unset, str] = UNSET
        if not isinstance(self.latest_date_added, Unset):
            latest_date_added = self.latest_date_added.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if collection_ids is not UNSET:
            field_dict["collectionIds"] = collection_ids
        if search_queries is not UNSET:
            field_dict["searchQueries"] = search_queries
        if collections is not UNSET:
            field_dict["collections"] = collections
        if latest_date_added is not UNSET:
            field_dict["latestDateAdded"] = latest_date_added

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.collection import Collection

        d = src_dict.copy()
        item_id = d.pop("itemId", UNSET)

        _content_type = d.pop("contentType", UNSET)
        content_type: Union[Unset, CollectableItemGroupContentType]
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = CollectableItemGroupContentType(_content_type)

        collection_ids = cast(List[str], d.pop("collectionIds", UNSET))

        search_queries = cast(List[str], d.pop("searchQueries", UNSET))

        collections = []
        _collections = d.pop("collections", UNSET)
        for collections_item_data in _collections or []:
            collections_item = Collection.from_dict(collections_item_data)

            collections.append(collections_item)

        _latest_date_added = d.pop("latestDateAdded", UNSET)
        latest_date_added: Union[Unset, datetime.datetime]
        if isinstance(_latest_date_added, Unset):
            latest_date_added = UNSET
        else:
            latest_date_added = isoparse(_latest_date_added)

        collectable_item_group = cls(
            item_id=item_id,
            content_type=content_type,
            collection_ids=collection_ids,
            search_queries=search_queries,
            collections=collections,
            latest_date_added=latest_date_added,
        )

        collectable_item_group.additional_properties = d
        return collectable_item_group

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
