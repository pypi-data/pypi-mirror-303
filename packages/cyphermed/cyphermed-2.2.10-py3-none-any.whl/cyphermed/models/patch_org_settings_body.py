from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.patch_org_settings_body_custom_settings import (
        PatchOrgSettingsBodyCustomSettings,
    )


T = TypeVar("T", bound="PatchOrgSettingsBody")


@_attrs_define
class PatchOrgSettingsBody:
    """Settings admins can update on their org

    Attributes:
        name (Union[Unset, str]): Organization name
        description (Union[Unset, str]): Organization description
        device_owners_have_admin_access (Union[Unset, bool]): Device owners have admin access
        device_owners_can_tunnel (Union[Unset, bool]): Device owners can open tunnels
        device_creators_are_owners_by_default (Union[Unset, bool]): Device creators are owners by default
        project_delete_protection_on_by_default (Union[Unset, bool]): (Org admins only) Delete protection is on by
            default for new projects
        group_delete_protection_on_by_default (Union[Unset, bool]): Delete protection is on by default for new groups
        user_delete_protection_on_by_default (Union[Unset, bool]): Delete protection is on by default for new users
        device_delete_protection_on_by_default (Union[Unset, bool]): Delete protection is on by default for new devices
        mfa_required (Union[Unset, bool]): MFA is required for all users
        custom_settings (Union[Unset, PatchOrgSettingsBodyCustomSettings]): Dictionary of custom organization settings
        default_locale (Union[Unset, str]): Default locale for the organization
        default_from_address (Union[Unset, str]): Default from address for the organization
        reset_token_expire_hours (Union[Unset, int]): Number of hours reset tokens are valid (1-168)
        access_token_expire_hours (Union[Unset, int]): Number of hours access tokens are valid (1-24)
        refresh_token_expire_hours (Union[Unset, int]): Number of hours refresh tokens are valid (1-8760)
        session_expire_mins (Union[Unset, int]): Number of mins sessions are valid (3-15)
        pii_admin_only (Union[Unset, bool]): Only admins can view personally identifiable info
        is_delete_protected (Union[Unset, bool]): This must be set false before the org/project can be deleted
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    device_owners_have_admin_access: Union[Unset, bool] = UNSET
    device_owners_can_tunnel: Union[Unset, bool] = UNSET
    device_creators_are_owners_by_default: Union[Unset, bool] = UNSET
    project_delete_protection_on_by_default: Union[Unset, bool] = UNSET
    group_delete_protection_on_by_default: Union[Unset, bool] = UNSET
    user_delete_protection_on_by_default: Union[Unset, bool] = UNSET
    device_delete_protection_on_by_default: Union[Unset, bool] = UNSET
    mfa_required: Union[Unset, bool] = UNSET
    custom_settings: Union[Unset, "PatchOrgSettingsBodyCustomSettings"] = UNSET
    default_locale: Union[Unset, str] = UNSET
    default_from_address: Union[Unset, str] = UNSET
    reset_token_expire_hours: Union[Unset, int] = UNSET
    access_token_expire_hours: Union[Unset, int] = UNSET
    refresh_token_expire_hours: Union[Unset, int] = UNSET
    session_expire_mins: Union[Unset, int] = UNSET
    pii_admin_only: Union[Unset, bool] = UNSET
    is_delete_protected: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        device_owners_have_admin_access = self.device_owners_have_admin_access

        device_owners_can_tunnel = self.device_owners_can_tunnel

        device_creators_are_owners_by_default = self.device_creators_are_owners_by_default

        project_delete_protection_on_by_default = self.project_delete_protection_on_by_default

        group_delete_protection_on_by_default = self.group_delete_protection_on_by_default

        user_delete_protection_on_by_default = self.user_delete_protection_on_by_default

        device_delete_protection_on_by_default = self.device_delete_protection_on_by_default

        mfa_required = self.mfa_required

        custom_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_settings, Unset):
            custom_settings = self.custom_settings.to_dict()

        default_locale = self.default_locale

        default_from_address = self.default_from_address

        reset_token_expire_hours = self.reset_token_expire_hours

        access_token_expire_hours = self.access_token_expire_hours

        refresh_token_expire_hours = self.refresh_token_expire_hours

        session_expire_mins = self.session_expire_mins

        pii_admin_only = self.pii_admin_only

        is_delete_protected = self.is_delete_protected

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if device_owners_have_admin_access is not UNSET:
            field_dict["device_owners_have_admin_access"] = device_owners_have_admin_access
        if device_owners_can_tunnel is not UNSET:
            field_dict["device_owners_can_tunnel"] = device_owners_can_tunnel
        if device_creators_are_owners_by_default is not UNSET:
            field_dict["device_creators_are_owners_by_default"] = (
                device_creators_are_owners_by_default
            )
        if project_delete_protection_on_by_default is not UNSET:
            field_dict["project_delete_protection_on_by_default"] = (
                project_delete_protection_on_by_default
            )
        if group_delete_protection_on_by_default is not UNSET:
            field_dict["group_delete_protection_on_by_default"] = (
                group_delete_protection_on_by_default
            )
        if user_delete_protection_on_by_default is not UNSET:
            field_dict["user_delete_protection_on_by_default"] = (
                user_delete_protection_on_by_default
            )
        if device_delete_protection_on_by_default is not UNSET:
            field_dict["device_delete_protection_on_by_default"] = (
                device_delete_protection_on_by_default
            )
        if mfa_required is not UNSET:
            field_dict["mfa_required"] = mfa_required
        if custom_settings is not UNSET:
            field_dict["custom_settings"] = custom_settings
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale
        if default_from_address is not UNSET:
            field_dict["default_from_address"] = default_from_address
        if reset_token_expire_hours is not UNSET:
            field_dict["reset_token_expire_hours"] = reset_token_expire_hours
        if access_token_expire_hours is not UNSET:
            field_dict["access_token_expire_hours"] = access_token_expire_hours
        if refresh_token_expire_hours is not UNSET:
            field_dict["refresh_token_expire_hours"] = refresh_token_expire_hours
        if session_expire_mins is not UNSET:
            field_dict["session_expire_mins"] = session_expire_mins
        if pii_admin_only is not UNSET:
            field_dict["pii_admin_only"] = pii_admin_only
        if is_delete_protected is not UNSET:
            field_dict["is_delete_protected"] = is_delete_protected

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_org_settings_body_custom_settings import (
            PatchOrgSettingsBodyCustomSettings,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        device_owners_have_admin_access = d.pop("device_owners_have_admin_access", UNSET)

        device_owners_can_tunnel = d.pop("device_owners_can_tunnel", UNSET)

        device_creators_are_owners_by_default = d.pop(
            "device_creators_are_owners_by_default", UNSET
        )

        project_delete_protection_on_by_default = d.pop(
            "project_delete_protection_on_by_default", UNSET
        )

        group_delete_protection_on_by_default = d.pop(
            "group_delete_protection_on_by_default", UNSET
        )

        user_delete_protection_on_by_default = d.pop("user_delete_protection_on_by_default", UNSET)

        device_delete_protection_on_by_default = d.pop(
            "device_delete_protection_on_by_default", UNSET
        )

        mfa_required = d.pop("mfa_required", UNSET)

        _custom_settings = d.pop("custom_settings", UNSET)
        custom_settings: Union[Unset, PatchOrgSettingsBodyCustomSettings]
        if isinstance(_custom_settings, Unset):
            custom_settings = UNSET
        else:
            custom_settings = PatchOrgSettingsBodyCustomSettings.from_dict(_custom_settings)

        default_locale = d.pop("default_locale", UNSET)

        default_from_address = d.pop("default_from_address", UNSET)

        reset_token_expire_hours = d.pop("reset_token_expire_hours", UNSET)

        access_token_expire_hours = d.pop("access_token_expire_hours", UNSET)

        refresh_token_expire_hours = d.pop("refresh_token_expire_hours", UNSET)

        session_expire_mins = d.pop("session_expire_mins", UNSET)

        pii_admin_only = d.pop("pii_admin_only", UNSET)

        is_delete_protected = d.pop("is_delete_protected", UNSET)

        patch_org_settings_body = cls(
            name=name,
            description=description,
            device_owners_have_admin_access=device_owners_have_admin_access,
            device_owners_can_tunnel=device_owners_can_tunnel,
            device_creators_are_owners_by_default=device_creators_are_owners_by_default,
            project_delete_protection_on_by_default=project_delete_protection_on_by_default,
            group_delete_protection_on_by_default=group_delete_protection_on_by_default,
            user_delete_protection_on_by_default=user_delete_protection_on_by_default,
            device_delete_protection_on_by_default=device_delete_protection_on_by_default,
            mfa_required=mfa_required,
            custom_settings=custom_settings,
            default_locale=default_locale,
            default_from_address=default_from_address,
            reset_token_expire_hours=reset_token_expire_hours,
            access_token_expire_hours=access_token_expire_hours,
            refresh_token_expire_hours=refresh_token_expire_hours,
            session_expire_mins=session_expire_mins,
            pii_admin_only=pii_admin_only,
            is_delete_protected=is_delete_protected,
        )

        patch_org_settings_body.additional_properties = d
        return patch_org_settings_body

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
