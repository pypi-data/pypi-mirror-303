from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.page_regions_item import PageRegionsItem


T = TypeVar("T", bound="Page")


@_attrs_define
class Page:
    """A page of an article

    Attributes:
        uid (str): The unique identifier of the page
        num (int): The number of the page
        issue_uid (str): Reference to the article
        newspaper_uid (str): Unique ID of the newspaper
        iiif (str): The IIF image file name of the page
        iiif_thumbnail (str): The IIF image thumbnail file name of the page
        access_rights (str): The access rights code
        labels (List[str]): Page labels
        has_coords (bool): Whether the page has coordinates
        has_errors (bool): Whether the page has errors
        regions (List['PageRegionsItem']): Regions of the page
        obfuscated (Union[Unset, bool]): Whether the page image has been obfuscated because the user is not authorised
            to access it
        iiif_fragment (Union[Unset, str]): The IIIF fragment of the page, image file name
    """

    uid: str
    num: int
    issue_uid: str
    newspaper_uid: str
    iiif: str
    iiif_thumbnail: str
    access_rights: str
    labels: List[str]
    has_coords: bool
    has_errors: bool
    regions: List["PageRegionsItem"]
    obfuscated: Union[Unset, bool] = UNSET
    iiif_fragment: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        uid = self.uid

        num = self.num

        issue_uid = self.issue_uid

        newspaper_uid = self.newspaper_uid

        iiif = self.iiif

        iiif_thumbnail = self.iiif_thumbnail

        access_rights = self.access_rights

        labels = self.labels

        has_coords = self.has_coords

        has_errors = self.has_errors

        regions = []
        for regions_item_data in self.regions:
            regions_item = regions_item_data.to_dict()
            regions.append(regions_item)

        obfuscated = self.obfuscated

        iiif_fragment = self.iiif_fragment

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "uid": uid,
                "num": num,
                "issueUid": issue_uid,
                "newspaperUid": newspaper_uid,
                "iiif": iiif,
                "iiifThumbnail": iiif_thumbnail,
                "accessRights": access_rights,
                "labels": labels,
                "hasCoords": has_coords,
                "hasErrors": has_errors,
                "regions": regions,
            }
        )
        if obfuscated is not UNSET:
            field_dict["obfuscated"] = obfuscated
        if iiif_fragment is not UNSET:
            field_dict["iiifFragment"] = iiif_fragment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.page_regions_item import PageRegionsItem

        d = src_dict.copy()
        uid = d.pop("uid")

        num = d.pop("num")

        issue_uid = d.pop("issueUid")

        newspaper_uid = d.pop("newspaperUid")

        iiif = d.pop("iiif")

        iiif_thumbnail = d.pop("iiifThumbnail")

        access_rights = d.pop("accessRights")

        labels = cast(List[str], d.pop("labels"))

        has_coords = d.pop("hasCoords")

        has_errors = d.pop("hasErrors")

        regions = []
        _regions = d.pop("regions")
        for regions_item_data in _regions:
            regions_item = PageRegionsItem.from_dict(regions_item_data)

            regions.append(regions_item)

        obfuscated = d.pop("obfuscated", UNSET)

        iiif_fragment = d.pop("iiifFragment", UNSET)

        page = cls(
            uid=uid,
            num=num,
            issue_uid=issue_uid,
            newspaper_uid=newspaper_uid,
            iiif=iiif,
            iiif_thumbnail=iiif_thumbnail,
            access_rights=access_rights,
            labels=labels,
            has_coords=has_coords,
            has_errors=has_errors,
            regions=regions,
            obfuscated=obfuscated,
            iiif_fragment=iiif_fragment,
        )

        return page
