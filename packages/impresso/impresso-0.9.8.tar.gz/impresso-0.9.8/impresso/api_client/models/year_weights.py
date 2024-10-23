from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="YearWeights")


@_attrs_define
class YearWeights:
    """Total items counts within a year

    Attributes:
        c (Union[Unset, float]): Number of content items
        a (Union[Unset, float]): Number of articles
        p (Union[Unset, float]): Number of pages
        i (Union[Unset, float]): Number of issues
        m (Union[Unset, float]): Number of images (with or without vectors)
    """

    c: Union[Unset, float] = UNSET
    a: Union[Unset, float] = UNSET
    p: Union[Unset, float] = UNSET
    i: Union[Unset, float] = UNSET
    m: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        c = self.c

        a = self.a

        p = self.p

        i = self.i

        m = self.m

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if c is not UNSET:
            field_dict["c"] = c
        if a is not UNSET:
            field_dict["a"] = a
        if p is not UNSET:
            field_dict["p"] = p
        if i is not UNSET:
            field_dict["i"] = i
        if m is not UNSET:
            field_dict["m"] = m

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        c = d.pop("c", UNSET)

        a = d.pop("a", UNSET)

        p = d.pop("p", UNSET)

        i = d.pop("i", UNSET)

        m = d.pop("m", UNSET)

        year_weights = cls(
            c=c,
            a=a,
            p=p,
            i=i,
            m=m,
        )

        return year_weights
