from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="EnableSoftwareMfaFormParams")


@_attrs_define
class EnableSoftwareMfaFormParams:
    """
    Attributes:
        client_id (str): Client ID
        mfa_code (str): MFA code generated using the secret code
        username (Union[Unset, str]): Username
        email (Union[Unset, str]): Email
        phone_number (Union[Unset, str]): Phone number
        set_preferred (Union[Unset, bool]): Set as preferred MFA device
    """

    client_id: str
    mfa_code: str
    username: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    set_preferred: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_id = self.client_id

        mfa_code = self.mfa_code

        username = self.username

        email = self.email

        phone_number = self.phone_number

        set_preferred = self.set_preferred

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_id": client_id,
                "mfa_code": mfa_code,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if set_preferred is not UNSET:
            field_dict["set_preferred"] = set_preferred

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_id = d.pop("client_id")

        mfa_code = d.pop("mfa_code")

        username = d.pop("username", UNSET)

        email = d.pop("email", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        set_preferred = d.pop("set_preferred", UNSET)

        enable_software_mfa_form_params = cls(
            client_id=client_id,
            mfa_code=mfa_code,
            username=username,
            email=email,
            phone_number=phone_number,
            set_preferred=set_preferred,
        )

        enable_software_mfa_form_params.additional_properties = d
        return enable_software_mfa_form_params

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
