from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopicWord")


@_attrs_define
class TopicWord:
    """TODO

    Attributes:
        w (str): Word
        p (float): TODO
        h (Union[Unset, List[str]]): TODO
    """

    w: str
    p: float
    h: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        w = self.w

        p = self.p

        h: Union[Unset, List[str]] = UNSET
        if not isinstance(self.h, Unset):
            h = self.h

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "w": w,
                "p": p,
            }
        )
        if h is not UNSET:
            field_dict["h"] = h

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        w = d.pop("w")

        p = d.pop("p")

        h = cast(List[str], d.pop("h", UNSET))

        topic_word = cls(
            w=w,
            p=p,
            h=h,
        )

        return topic_word
