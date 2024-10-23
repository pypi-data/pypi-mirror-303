from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.text_reuse_cluster_compound import TextReuseClusterCompound


T = TypeVar("T", bound="FindTextReuseClustersResponse")


@_attrs_define
class FindTextReuseClustersResponse:
    """Response for GET /text-reuse-clusters

    Attributes:
        clusters (List['TextReuseClusterCompound']):
        info (Any):
    """

    clusters: List["TextReuseClusterCompound"]
    info: Any

    def to_dict(self) -> Dict[str, Any]:
        clusters = []
        for clusters_item_data in self.clusters:
            clusters_item = clusters_item_data.to_dict()
            clusters.append(clusters_item)

        info = self.info

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "clusters": clusters,
                "info": info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.text_reuse_cluster_compound import TextReuseClusterCompound

        d = src_dict.copy()
        clusters = []
        _clusters = d.pop("clusters")
        for clusters_item_data in _clusters:
            clusters_item = TextReuseClusterCompound.from_dict(clusters_item_data)

            clusters.append(clusters_item)

        info = d.pop("info")

        find_text_reuse_clusters_response = cls(
            clusters=clusters,
            info=info,
        )

        return find_text_reuse_clusters_response
