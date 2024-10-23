from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_reuse_cluster import TextReuseCluster
    from ..models.text_reuse_cluster_details import TextReuseClusterDetails


T = TypeVar("T", bound="TextReuseClusterCompound")


@_attrs_define
class TextReuseClusterCompound:
    """Text reuse cluster with details and a sample

    Attributes:
        text_sample (str):
        cluster (Union[Unset, TextReuseCluster]): Represents a cluster of text reuse passages
        details (Union[Unset, TextReuseClusterDetails]): Extra details of the cluster
    """

    text_sample: str
    cluster: Union[Unset, "TextReuseCluster"] = UNSET
    details: Union[Unset, "TextReuseClusterDetails"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        text_sample = self.text_sample

        cluster: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cluster, Unset):
            cluster = self.cluster.to_dict()

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "textSample": text_sample,
            }
        )
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.text_reuse_cluster import TextReuseCluster
        from ..models.text_reuse_cluster_details import TextReuseClusterDetails

        d = src_dict.copy()
        text_sample = d.pop("textSample")

        _cluster = d.pop("cluster", UNSET)
        cluster: Union[Unset, TextReuseCluster]
        if isinstance(_cluster, Unset):
            cluster = UNSET
        else:
            cluster = TextReuseCluster.from_dict(_cluster)

        _details = d.pop("details", UNSET)
        details: Union[Unset, TextReuseClusterDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = TextReuseClusterDetails.from_dict(_details)

        text_reuse_cluster_compound = cls(
            text_sample=text_sample,
            cluster=cluster,
            details=details,
        )

        return text_reuse_cluster_compound
