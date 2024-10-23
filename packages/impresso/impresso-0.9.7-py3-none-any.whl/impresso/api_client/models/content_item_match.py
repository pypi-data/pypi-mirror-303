from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentItemMatch")


@_attrs_define
class ContentItemMatch:
    """TODO

    Attributes:
        fragment (str): TODO
        coords (Union[Unset, List[float]]): TODO
        page_uid (Union[Unset, str]): TODO
        iiif (Union[Unset, str]): TODO
    """

    fragment: str
    coords: Union[Unset, List[float]] = UNSET
    page_uid: Union[Unset, str] = UNSET
    iiif: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        fragment = self.fragment

        coords: Union[Unset, List[float]] = UNSET
        if not isinstance(self.coords, Unset):
            coords = self.coords

        page_uid = self.page_uid

        iiif = self.iiif

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "fragment": fragment,
            }
        )
        if coords is not UNSET:
            field_dict["coords"] = coords
        if page_uid is not UNSET:
            field_dict["pageUid"] = page_uid
        if iiif is not UNSET:
            field_dict["iiif"] = iiif

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fragment = d.pop("fragment")

        coords = cast(List[float], d.pop("coords", UNSET))

        page_uid = d.pop("pageUid", UNSET)

        iiif = d.pop("iiif", UNSET)

        content_item_match = cls(
            fragment=fragment,
            coords=coords,
            page_uid=page_uid,
            iiif=iiif,
        )

        return content_item_match
