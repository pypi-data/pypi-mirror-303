from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="SmsMfaAdded")


@_attrs_define
class SmsMfaAdded:
    """MFA SMS token success

    Attributes:
        message (Union[Unset, str]):  Default: 'SMS MFA successfully enabled'.
        recovery_code (Union[Unset, str]): SMS MFA recovery code
    """

    message: Union[Unset, str] = "SMS MFA successfully enabled"
    recovery_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message

        recovery_code = self.recovery_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if recovery_code is not UNSET:
            field_dict["recovery_code"] = recovery_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message", UNSET)

        recovery_code = d.pop("recovery_code", UNSET)

        sms_mfa_added = cls(
            message=message,
            recovery_code=recovery_code,
        )

        sms_mfa_added.additional_properties = d
        return sms_mfa_added

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
