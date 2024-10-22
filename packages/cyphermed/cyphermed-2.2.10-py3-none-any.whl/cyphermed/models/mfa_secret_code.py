from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="MfaSecretCode")


@_attrs_define
class MfaSecretCode:
    """MFA secret code

    Attributes:
        secret_code (str): MFA secret code
        session (Union[Unset, str]): Session to use for adding software MFA
    """

    secret_code: str
    session: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        secret_code = self.secret_code

        session = self.session

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secret_code": secret_code,
            }
        )
        if session is not UNSET:
            field_dict["session"] = session

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        secret_code = d.pop("secret_code")

        session = d.pop("session", UNSET)

        mfa_secret_code = cls(
            secret_code=secret_code,
            session=session,
        )

        mfa_secret_code.additional_properties = d
        return mfa_secret_code

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
