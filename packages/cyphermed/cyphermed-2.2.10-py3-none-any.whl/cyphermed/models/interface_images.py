from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="InterfaceImages")


@_attrs_define
class InterfaceImages:
    """Logos for the user interface

    Attributes:
        logo_default (Union[Unset, str]): URL of the default logo
        logo_small (Union[Unset, str]): URL of the small logo
        login_background (Union[Unset, str]): URL of the login background image
        favicon (Union[Unset, str]): URL of the favicon
    """

    logo_default: Union[Unset, str] = UNSET
    logo_small: Union[Unset, str] = UNSET
    login_background: Union[Unset, str] = UNSET
    favicon: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        logo_default = self.logo_default

        logo_small = self.logo_small

        login_background = self.login_background

        favicon = self.favicon

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logo_default is not UNSET:
            field_dict["logo_default"] = logo_default
        if logo_small is not UNSET:
            field_dict["logo_small"] = logo_small
        if login_background is not UNSET:
            field_dict["login_background"] = login_background
        if favicon is not UNSET:
            field_dict["favicon"] = favicon

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        logo_default = d.pop("logo_default", UNSET)

        logo_small = d.pop("logo_small", UNSET)

        login_background = d.pop("login_background", UNSET)

        favicon = d.pop("favicon", UNSET)

        interface_images = cls(
            logo_default=logo_default,
            logo_small=logo_small,
            login_background=login_background,
            favicon=favicon,
        )

        interface_images.additional_properties = d
        return interface_images

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
