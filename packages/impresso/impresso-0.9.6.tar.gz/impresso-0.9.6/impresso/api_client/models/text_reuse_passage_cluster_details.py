from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextReusePassageClusterDetails")


@_attrs_define
class TextReusePassageClusterDetails:
    """Details of the cluster the passage belongs to

    Attributes:
        id (str): ID of the cluster
        cluster_size (Union[Unset, int]): The size of the cluster
        time_difference_day (Union[Unset, int]): The time difference in days between the two articles
        lexical_overlap (Union[Unset, float]): The lexical overlap between the two articles
    """

    id: str
    cluster_size: Union[Unset, int] = UNSET
    time_difference_day: Union[Unset, int] = UNSET
    lexical_overlap: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        cluster_size = self.cluster_size

        time_difference_day = self.time_difference_day

        lexical_overlap = self.lexical_overlap

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )
        if cluster_size is not UNSET:
            field_dict["clusterSize"] = cluster_size
        if time_difference_day is not UNSET:
            field_dict["timeDifferenceDay"] = time_difference_day
        if lexical_overlap is not UNSET:
            field_dict["lexicalOverlap"] = lexical_overlap

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        cluster_size = d.pop("clusterSize", UNSET)

        time_difference_day = d.pop("timeDifferenceDay", UNSET)

        lexical_overlap = d.pop("lexicalOverlap", UNSET)

        text_reuse_passage_cluster_details = cls(
            id=id,
            cluster_size=cluster_size,
            time_difference_day=time_difference_day,
            lexical_overlap=lexical_overlap,
        )

        return text_reuse_passage_cluster_details
