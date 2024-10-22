from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="RespondToChallengeFormParams")


@_attrs_define
class RespondToChallengeFormParams:
    """
    Attributes:
        client_id (str): Client ID
        challenge (str): Challenge
        username (Union[Unset, str]): Username
        email (Union[Unset, str]): Email
        phone_number (Union[Unset, str]): Phone number
        scope (Union[Unset, str]): (Staff Only) Scope
        mfa_choice (Union[Unset, str]): MFA choice: software or sms
        mfa_code (Union[Unset, str]): MFA code
        new_password (Union[Unset, str]): New password
    """

    client_id: str
    challenge: str
    username: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    mfa_choice: Union[Unset, str] = UNSET
    mfa_code: Union[Unset, str] = UNSET
    new_password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_id = self.client_id

        challenge = self.challenge

        username = self.username

        email = self.email

        phone_number = self.phone_number

        scope = self.scope

        mfa_choice = self.mfa_choice

        mfa_code = self.mfa_code

        new_password = self.new_password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_id": client_id,
                "challenge": challenge,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if scope is not UNSET:
            field_dict["scope"] = scope
        if mfa_choice is not UNSET:
            field_dict["mfa_choice"] = mfa_choice
        if mfa_code is not UNSET:
            field_dict["mfa_code"] = mfa_code
        if new_password is not UNSET:
            field_dict["new_password"] = new_password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_id = d.pop("client_id")

        challenge = d.pop("challenge")

        username = d.pop("username", UNSET)

        email = d.pop("email", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        scope = d.pop("scope", UNSET)

        mfa_choice = d.pop("mfa_choice", UNSET)

        mfa_code = d.pop("mfa_code", UNSET)

        new_password = d.pop("new_password", UNSET)

        respond_to_challenge_form_params = cls(
            client_id=client_id,
            challenge=challenge,
            username=username,
            email=email,
            phone_number=phone_number,
            scope=scope,
            mfa_choice=mfa_choice,
            mfa_code=mfa_code,
            new_password=new_password,
        )

        respond_to_challenge_form_params.additional_properties = d
        return respond_to_challenge_form_params

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
