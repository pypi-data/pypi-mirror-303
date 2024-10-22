from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="SoftwareMfaAdded")


@_attrs_define
class SoftwareMfaAdded:
    """MFA software token success

    Attributes:
        recovery_code (str): Software MFA recovery code
        message (Union[Unset, str]):  Default: 'Software MFA successfully enabled'.
        session (Union[Unset, str]): Session to use for answering MFA_SETUP challenge
    """

    recovery_code: str
    message: Union[Unset, str] = "Software MFA successfully enabled"
    session: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        recovery_code = self.recovery_code

        message = self.message

        session = self.session

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recovery_code": recovery_code,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if session is not UNSET:
            field_dict["session"] = session

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        recovery_code = d.pop("recovery_code")

        message = d.pop("message", UNSET)

        session = d.pop("session", UNSET)

        software_mfa_added = cls(
            recovery_code=recovery_code,
            message=message,
            session=session,
        )

        software_mfa_added.additional_properties = d
        return software_mfa_added

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
