from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="EnableSmsMfaFormParams")


@_attrs_define
class EnableSmsMfaFormParams:
    """
    Attributes:
        phone_number (str): Phone number
        client_id (Union[Unset, str]): Client ID
        username (Union[Unset, str]): Username
        email (Union[Unset, str]): Email
        set_preferred (Union[Unset, bool]): Set as preferred MFA device
        recovery_code (Union[Unset, str]): MFA recovery code
    """

    phone_number: str
    client_id: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    set_preferred: Union[Unset, bool] = UNSET
    recovery_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        phone_number = self.phone_number

        client_id = self.client_id

        username = self.username

        email = self.email

        set_preferred = self.set_preferred

        recovery_code = self.recovery_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phone_number": phone_number,
            }
        )
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if username is not UNSET:
            field_dict["username"] = username
        if email is not UNSET:
            field_dict["email"] = email
        if set_preferred is not UNSET:
            field_dict["set_preferred"] = set_preferred
        if recovery_code is not UNSET:
            field_dict["recovery_code"] = recovery_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        phone_number = d.pop("phone_number")

        client_id = d.pop("client_id", UNSET)

        username = d.pop("username", UNSET)

        email = d.pop("email", UNSET)

        set_preferred = d.pop("set_preferred", UNSET)

        recovery_code = d.pop("recovery_code", UNSET)

        enable_sms_mfa_form_params = cls(
            phone_number=phone_number,
            client_id=client_id,
            username=username,
            email=email,
            set_preferred=set_preferred,
            recovery_code=recovery_code,
        )

        enable_sms_mfa_form_params.additional_properties = d
        return enable_sms_mfa_form_params

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
