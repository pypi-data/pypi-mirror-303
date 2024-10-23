from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection import Collection
    from ..models.entity import Entity
    from ..models.newspaper import Newspaper
    from ..models.topic import Topic
    from ..models.year import Year


T = TypeVar("T", bound="SearchFacetBucket")


@_attrs_define
class SearchFacetBucket:
    """Facet bucket

    Attributes:
        count (int): Number of items in the bucket
        val (str): Value of the 'type' element
        uid (Union[Unset, str]): UID of the 'type' element. Same as 'val'
        item (Union['Collection', 'Entity', 'Newspaper', 'Topic', 'Year', Unset]): The item in the bucket. Particular
            objct schema depends on the facet type
    """

    count: int
    val: str
    uid: Union[Unset, str] = UNSET
    item: Union["Collection", "Entity", "Newspaper", "Topic", "Year", Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.collection import Collection
        from ..models.entity import Entity
        from ..models.newspaper import Newspaper
        from ..models.topic import Topic

        count = self.count

        val = self.val

        uid = self.uid

        item: Union[Dict[str, Any], Unset]
        if isinstance(self.item, Unset):
            item = UNSET
        elif isinstance(self.item, Newspaper):
            item = self.item.to_dict()
        elif isinstance(self.item, Collection):
            item = self.item.to_dict()
        elif isinstance(self.item, Entity):
            item = self.item.to_dict()
        elif isinstance(self.item, Topic):
            item = self.item.to_dict()
        else:
            item = self.item.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "count": count,
                "val": val,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if item is not UNSET:
            field_dict["item"] = item

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.collection import Collection
        from ..models.entity import Entity
        from ..models.newspaper import Newspaper
        from ..models.topic import Topic
        from ..models.year import Year

        d = src_dict.copy()
        count = d.pop("count")

        val = d.pop("val")

        uid = d.pop("uid", UNSET)

        def _parse_item(data: object) -> Union["Collection", "Entity", "Newspaper", "Topic", "Year", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                item_type_0 = Newspaper.from_dict(data)

                return item_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                item_type_1 = Collection.from_dict(data)

                return item_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                item_type_2 = Entity.from_dict(data)

                return item_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                item_type_3 = Topic.from_dict(data)

                return item_type_3
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            item_type_4 = Year.from_dict(data)

            return item_type_4

        item = _parse_item(d.pop("item", UNSET))

        search_facet_bucket = cls(
            count=count,
            val=val,
            uid=uid,
            item=item,
        )

        return search_facet_bucket
