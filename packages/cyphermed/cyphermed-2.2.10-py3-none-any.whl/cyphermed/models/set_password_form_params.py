from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="SetPasswordFormParams")


@_attrs_define
class SetPasswordFormParams:
    """
    Attributes:
        new_password (str): New password
        old_password (Union[Unset, str]): Old password
    """

    new_password: str
    old_password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new_password = self.new_password

        old_password = self.old_password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "new_password": new_password,
            }
        )
        if old_password is not UNSET:
            field_dict["old_password"] = old_password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_password = d.pop("new_password")

        old_password = d.pop("old_password", UNSET)

        set_password_form_params = cls(
            new_password=new_password,
            old_password=old_password,
        )

        set_password_form_params.additional_properties = d
        return set_password_form_params

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
