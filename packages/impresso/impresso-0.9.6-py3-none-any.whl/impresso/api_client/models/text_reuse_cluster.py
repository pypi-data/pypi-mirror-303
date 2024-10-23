from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.text_reuse_cluster_time_coverage import TextReuseClusterTimeCoverage


T = TypeVar("T", bound="TextReuseCluster")


@_attrs_define
class TextReuseCluster:
    """Represents a cluster of text reuse passages

    Attributes:
        id (str): ID of the text reuse passage Example: abc123.
        lexical_overlap (Union[Unset, float]): Percentage of overlap between passages in the cluster
        cluster_size (Union[Unset, float]): Number of passages in cluster
        connected_clusters_count (Union[Unset, float]): Number of connected clusters
        time_coverage (Union[Unset, TextReuseClusterTimeCoverage]): Time window covered by documents in the cluster
    """

    id: str
    lexical_overlap: Union[Unset, float] = UNSET
    cluster_size: Union[Unset, float] = UNSET
    connected_clusters_count: Union[Unset, float] = UNSET
    time_coverage: Union[Unset, "TextReuseClusterTimeCoverage"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        lexical_overlap = self.lexical_overlap

        cluster_size = self.cluster_size

        connected_clusters_count = self.connected_clusters_count

        time_coverage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_coverage, Unset):
            time_coverage = self.time_coverage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )
        if lexical_overlap is not UNSET:
            field_dict["lexicalOverlap"] = lexical_overlap
        if cluster_size is not UNSET:
            field_dict["clusterSize"] = cluster_size
        if connected_clusters_count is not UNSET:
            field_dict["connectedClustersCount"] = connected_clusters_count
        if time_coverage is not UNSET:
            field_dict["timeCoverage"] = time_coverage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.text_reuse_cluster_time_coverage import TextReuseClusterTimeCoverage

        d = src_dict.copy()
        id = d.pop("id")

        lexical_overlap = d.pop("lexicalOverlap", UNSET)

        cluster_size = d.pop("clusterSize", UNSET)

        connected_clusters_count = d.pop("connectedClustersCount", UNSET)

        _time_coverage = d.pop("timeCoverage", UNSET)
        time_coverage: Union[Unset, TextReuseClusterTimeCoverage]
        if isinstance(_time_coverage, Unset):
            time_coverage = UNSET
        else:
            time_coverage = TextReuseClusterTimeCoverage.from_dict(_time_coverage)

        text_reuse_cluster = cls(
            id=id,
            lexical_overlap=lexical_overlap,
            cluster_size=cluster_size,
            connected_clusters_count=connected_clusters_count,
            time_coverage=time_coverage,
        )

        return text_reuse_cluster
