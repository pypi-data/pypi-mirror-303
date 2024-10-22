from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="LoginFormParams")


@_attrs_define
class LoginFormParams:
    """
    Attributes:
        grant_type (str): Grant type
        client_id (Union[Unset, str]): Client ID
        username (Union[Unset, str]): Username
        email (Union[Unset, str]): Email
        phone_number (Union[Unset, str]): Phone number
        refresh_token (Union[Unset, str]): Refresh token
        scope (Union[Unset, str]): Scope
        password (Union[Unset, str]): Password
        mfa_code (Union[Unset, str]): Software MFA code
    """

    grant_type: str
    client_id: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    refresh_token: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    mfa_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        grant_type = self.grant_type

        client_id = self.client_id

        username = self.username

        email = self.email

        phone_number = self.phone_number

        refresh_token = self.refresh_token

        scope = self.scope

        password = self.password

        mfa_code = self.mfa_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_type": grant_type,
            }
        )
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if username is not UNSET:
            field_dict["username"] = username
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if scope is not UNSET:
            field_dict["scope"] = scope
        if password is not UNSET:
            field_dict["password"] = password
        if mfa_code is not UNSET:
            field_dict["mfa_code"] = mfa_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        grant_type = d.pop("grant_type")

        client_id = d.pop("client_id", UNSET)

        username = d.pop("username", UNSET)

        email = d.pop("email", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        refresh_token = d.pop("refresh_token", UNSET)

        scope = d.pop("scope", UNSET)

        password = d.pop("password", UNSET)

        mfa_code = d.pop("mfa_code", UNSET)

        login_form_params = cls(
            grant_type=grant_type,
            client_id=client_id,
            username=username,
            email=email,
            phone_number=phone_number,
            refresh_token=refresh_token,
            scope=scope,
            password=password,
            mfa_code=mfa_code,
        )

        login_form_params.additional_properties = d
        return login_form_params

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
