from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.text_reuse_cluster_details_resolution import TextReuseClusterDetailsResolution
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_reuse_cluster_details_facets_item import TextReuseClusterDetailsFacetsItem


T = TypeVar("T", bound="TextReuseClusterDetails")


@_attrs_define
class TextReuseClusterDetails:
    """Extra details of the cluster

    Attributes:
        facets (List['TextReuseClusterDetailsFacetsItem']):
        resolution (Union[Unset, TextReuseClusterDetailsResolution]): Resolution for the 'date' facet
    """

    facets: List["TextReuseClusterDetailsFacetsItem"]
    resolution: Union[Unset, TextReuseClusterDetailsResolution] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        facets = []
        for facets_item_data in self.facets:
            facets_item = facets_item_data.to_dict()
            facets.append(facets_item)

        resolution: Union[Unset, str] = UNSET
        if not isinstance(self.resolution, Unset):
            resolution = self.resolution.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "facets": facets,
            }
        )
        if resolution is not UNSET:
            field_dict["resolution"] = resolution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.text_reuse_cluster_details_facets_item import TextReuseClusterDetailsFacetsItem

        d = src_dict.copy()
        facets = []
        _facets = d.pop("facets")
        for facets_item_data in _facets:
            facets_item = TextReuseClusterDetailsFacetsItem.from_dict(facets_item_data)

            facets.append(facets_item)

        _resolution = d.pop("resolution", UNSET)
        resolution: Union[Unset, TextReuseClusterDetailsResolution]
        if isinstance(_resolution, Unset):
            resolution = UNSET
        else:
            resolution = TextReuseClusterDetailsResolution(_resolution)

        text_reuse_cluster_details = cls(
            facets=facets,
            resolution=resolution,
        )

        return text_reuse_cluster_details
