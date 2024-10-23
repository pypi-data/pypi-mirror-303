from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindTextReusePassagesAddons")


@_attrs_define
class FindTextReusePassagesAddons:
    """
    Attributes:
        newspaper (Union[Unset, Any]):
    """

    newspaper: Union[Unset, Any] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        newspaper = self.newspaper

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if newspaper is not UNSET:
            field_dict["newspaper"] = newspaper

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        newspaper = d.pop("newspaper", UNSET)

        find_text_reuse_passages_addons = cls(
            newspaper=newspaper,
        )

        return find_text_reuse_passages_addons
