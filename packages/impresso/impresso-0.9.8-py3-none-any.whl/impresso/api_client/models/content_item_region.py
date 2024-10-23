from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentItemRegion")


@_attrs_define
class ContentItemRegion:
    """TODO

    Attributes:
        page_uid (str):
        coords (List[float]):
        is_empty (bool): TODO
        iiif_fragment (Union[Unset, str]): IIIF fragment URL
        g (Union[Unset, List[str]]): TODO
    """

    page_uid: str
    coords: List[float]
    is_empty: bool
    iiif_fragment: Union[Unset, str] = UNSET
    g: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        page_uid = self.page_uid

        coords = self.coords

        is_empty = self.is_empty

        iiif_fragment = self.iiif_fragment

        g: Union[Unset, List[str]] = UNSET
        if not isinstance(self.g, Unset):
            g = self.g

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "pageUid": page_uid,
                "coords": coords,
                "isEmpty": is_empty,
            }
        )
        if iiif_fragment is not UNSET:
            field_dict["iiifFragment"] = iiif_fragment
        if g is not UNSET:
            field_dict["g"] = g

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        page_uid = d.pop("pageUid")

        coords = cast(List[float], d.pop("coords"))

        is_empty = d.pop("isEmpty")

        iiif_fragment = d.pop("iiifFragment", UNSET)

        g = cast(List[str], d.pop("g", UNSET))

        content_item_region = cls(
            page_uid=page_uid,
            coords=coords,
            is_empty=is_empty,
            iiif_fragment=iiif_fragment,
            g=g,
        )

        return content_item_region
