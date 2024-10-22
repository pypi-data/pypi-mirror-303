import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.org_schema_allowed_login_fields import OrgSchemaAllowedLoginFields
    from ..models.org_schema_custom_settings import OrgSchemaCustomSettings
    from ..models.org_schema_ui_config import OrgSchemaUiConfig


T = TypeVar("T", bound="OrgSchema")


@_attrs_define
class OrgSchema:
    """Organization model schema

    Attributes:
        name (str):
        created_date (datetime.datetime):
        id (str): ID of the account
        alias (Union[Unset, str]):
        description (Union[Unset, str]):  Default: ''.
        allowed_login_fields (Union[Unset, OrgSchemaAllowedLoginFields]):
        mfa_required (Union[Unset, bool]):  Default: False.
        custom_settings (Union[Unset, OrgSchemaCustomSettings]):
        device_owners_have_admin_access (Union[Unset, bool]):  Default: False.
        device_owners_can_tunnel (Union[Unset, bool]):  Default: False.
        device_creators_are_owners_by_default (Union[Unset, bool]):  Default: False.
        project_delete_protection_on_by_default (Union[Unset, bool]):  Default: False.
        group_delete_protection_on_by_default (Union[Unset, bool]):  Default: False.
        role_delete_protection_on_by_default (Union[Unset, bool]):  Default: False.
        user_delete_protection_on_by_default (Union[Unset, bool]):  Default: False.
        device_delete_protection_on_by_default (Union[Unset, bool]):  Default: False.
        is_delete_protected (Union[Unset, bool]):  Default: False.
        is_active (Union[Unset, bool]):  Default: True.
        last_updated_date (Union[Unset, datetime.datetime]):
        default_locale (Union[Unset, str]):  Default: 'en-US'.
        default_from_address (Union[Unset, str]):  Default: 'no-reply@cyphermed.cloud'.
        reset_token_expire_hours (Union[Unset, int]):  Default: 24.
        access_token_expire_hours (Union[Unset, int]):  Default: 1.
        refresh_token_expire_hours (Union[Unset, int]):  Default: 24.
        session_expire_mins (Union[Unset, int]):  Default: 5.
        pii_admin_only (Union[Unset, bool]):  Default: False.
        ui_config (Union[Unset, OrgSchemaUiConfig]):
        use_legacy_data_and_files_permissions (Union[Unset, bool]):  Default: False.
        groups_require_delete_permission_to_put_data_by_default (Union[Unset, bool]):  Default: False.
    """

    name: str
    created_date: datetime.datetime
    id: str
    alias: Union[Unset, str] = UNSET
    description: Union[Unset, str] = ""
    allowed_login_fields: Union[Unset, "OrgSchemaAllowedLoginFields"] = UNSET
    mfa_required: Union[Unset, bool] = False
    custom_settings: Union[Unset, "OrgSchemaCustomSettings"] = UNSET
    device_owners_have_admin_access: Union[Unset, bool] = False
    device_owners_can_tunnel: Union[Unset, bool] = False
    device_creators_are_owners_by_default: Union[Unset, bool] = False
    project_delete_protection_on_by_default: Union[Unset, bool] = False
    group_delete_protection_on_by_default: Union[Unset, bool] = False
    role_delete_protection_on_by_default: Union[Unset, bool] = False
    user_delete_protection_on_by_default: Union[Unset, bool] = False
    device_delete_protection_on_by_default: Union[Unset, bool] = False
    is_delete_protected: Union[Unset, bool] = False
    is_active: Union[Unset, bool] = True
    last_updated_date: Union[Unset, datetime.datetime] = UNSET
    default_locale: Union[Unset, str] = "en-US"
    default_from_address: Union[Unset, str] = "no-reply@cyphermed.cloud"
    reset_token_expire_hours: Union[Unset, int] = 24
    access_token_expire_hours: Union[Unset, int] = 1
    refresh_token_expire_hours: Union[Unset, int] = 24
    session_expire_mins: Union[Unset, int] = 5
    pii_admin_only: Union[Unset, bool] = False
    ui_config: Union[Unset, "OrgSchemaUiConfig"] = UNSET
    use_legacy_data_and_files_permissions: Union[Unset, bool] = False
    groups_require_delete_permission_to_put_data_by_default: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        created_date = self.created_date.isoformat()

        id = self.id

        alias = self.alias

        description = self.description

        allowed_login_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.allowed_login_fields, Unset):
            allowed_login_fields = self.allowed_login_fields.to_dict()

        mfa_required = self.mfa_required

        custom_settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_settings, Unset):
            custom_settings = self.custom_settings.to_dict()

        device_owners_have_admin_access = self.device_owners_have_admin_access

        device_owners_can_tunnel = self.device_owners_can_tunnel

        device_creators_are_owners_by_default = self.device_creators_are_owners_by_default

        project_delete_protection_on_by_default = self.project_delete_protection_on_by_default

        group_delete_protection_on_by_default = self.group_delete_protection_on_by_default

        role_delete_protection_on_by_default = self.role_delete_protection_on_by_default

        user_delete_protection_on_by_default = self.user_delete_protection_on_by_default

        device_delete_protection_on_by_default = self.device_delete_protection_on_by_default

        is_delete_protected = self.is_delete_protected

        is_active = self.is_active

        last_updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.isoformat()

        default_locale = self.default_locale

        default_from_address = self.default_from_address

        reset_token_expire_hours = self.reset_token_expire_hours

        access_token_expire_hours = self.access_token_expire_hours

        refresh_token_expire_hours = self.refresh_token_expire_hours

        session_expire_mins = self.session_expire_mins

        pii_admin_only = self.pii_admin_only

        ui_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ui_config, Unset):
            ui_config = self.ui_config.to_dict()

        use_legacy_data_and_files_permissions = self.use_legacy_data_and_files_permissions

        groups_require_delete_permission_to_put_data_by_default = (
            self.groups_require_delete_permission_to_put_data_by_default
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "created_date": created_date,
                "id": id,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias
        if description is not UNSET:
            field_dict["description"] = description
        if allowed_login_fields is not UNSET:
            field_dict["allowed_login_fields"] = allowed_login_fields
        if mfa_required is not UNSET:
            field_dict["mfa_required"] = mfa_required
        if custom_settings is not UNSET:
            field_dict["custom_settings"] = custom_settings
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
        if role_delete_protection_on_by_default is not UNSET:
            field_dict["role_delete_protection_on_by_default"] = (
                role_delete_protection_on_by_default
            )
        if user_delete_protection_on_by_default is not UNSET:
            field_dict["user_delete_protection_on_by_default"] = (
                user_delete_protection_on_by_default
            )
        if device_delete_protection_on_by_default is not UNSET:
            field_dict["device_delete_protection_on_by_default"] = (
                device_delete_protection_on_by_default
            )
        if is_delete_protected is not UNSET:
            field_dict["is_delete_protected"] = is_delete_protected
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if last_updated_date is not UNSET:
            field_dict["last_updated_date"] = last_updated_date
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
        if ui_config is not UNSET:
            field_dict["ui_config"] = ui_config
        if use_legacy_data_and_files_permissions is not UNSET:
            field_dict["use_legacy_data_and_files_permissions"] = (
                use_legacy_data_and_files_permissions
            )
        if groups_require_delete_permission_to_put_data_by_default is not UNSET:
            field_dict["groups_require_delete_permission_to_put_data_by_default"] = (
                groups_require_delete_permission_to_put_data_by_default
            )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.org_schema_allowed_login_fields import OrgSchemaAllowedLoginFields
        from ..models.org_schema_custom_settings import OrgSchemaCustomSettings
        from ..models.org_schema_ui_config import OrgSchemaUiConfig

        d = src_dict.copy()
        name = d.pop("name")

        created_date = isoparse(d.pop("created_date"))

        id = d.pop("id")

        alias = d.pop("alias", UNSET)

        description = d.pop("description", UNSET)

        _allowed_login_fields = d.pop("allowed_login_fields", UNSET)
        allowed_login_fields: Union[Unset, OrgSchemaAllowedLoginFields]
        if isinstance(_allowed_login_fields, Unset):
            allowed_login_fields = UNSET
        else:
            allowed_login_fields = OrgSchemaAllowedLoginFields.from_dict(_allowed_login_fields)

        mfa_required = d.pop("mfa_required", UNSET)

        _custom_settings = d.pop("custom_settings", UNSET)
        custom_settings: Union[Unset, OrgSchemaCustomSettings]
        if isinstance(_custom_settings, Unset):
            custom_settings = UNSET
        else:
            custom_settings = OrgSchemaCustomSettings.from_dict(_custom_settings)

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

        role_delete_protection_on_by_default = d.pop("role_delete_protection_on_by_default", UNSET)

        user_delete_protection_on_by_default = d.pop("user_delete_protection_on_by_default", UNSET)

        device_delete_protection_on_by_default = d.pop(
            "device_delete_protection_on_by_default", UNSET
        )

        is_delete_protected = d.pop("is_delete_protected", UNSET)

        is_active = d.pop("is_active", UNSET)

        _last_updated_date = d.pop("last_updated_date", UNSET)
        last_updated_date: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = isoparse(_last_updated_date)

        default_locale = d.pop("default_locale", UNSET)

        default_from_address = d.pop("default_from_address", UNSET)

        reset_token_expire_hours = d.pop("reset_token_expire_hours", UNSET)

        access_token_expire_hours = d.pop("access_token_expire_hours", UNSET)

        refresh_token_expire_hours = d.pop("refresh_token_expire_hours", UNSET)

        session_expire_mins = d.pop("session_expire_mins", UNSET)

        pii_admin_only = d.pop("pii_admin_only", UNSET)

        _ui_config = d.pop("ui_config", UNSET)
        ui_config: Union[Unset, OrgSchemaUiConfig]
        if isinstance(_ui_config, Unset):
            ui_config = UNSET
        else:
            ui_config = OrgSchemaUiConfig.from_dict(_ui_config)

        use_legacy_data_and_files_permissions = d.pop(
            "use_legacy_data_and_files_permissions", UNSET
        )

        groups_require_delete_permission_to_put_data_by_default = d.pop(
            "groups_require_delete_permission_to_put_data_by_default", UNSET
        )

        org_schema = cls(
            name=name,
            created_date=created_date,
            id=id,
            alias=alias,
            description=description,
            allowed_login_fields=allowed_login_fields,
            mfa_required=mfa_required,
            custom_settings=custom_settings,
            device_owners_have_admin_access=device_owners_have_admin_access,
            device_owners_can_tunnel=device_owners_can_tunnel,
            device_creators_are_owners_by_default=device_creators_are_owners_by_default,
            project_delete_protection_on_by_default=project_delete_protection_on_by_default,
            group_delete_protection_on_by_default=group_delete_protection_on_by_default,
            role_delete_protection_on_by_default=role_delete_protection_on_by_default,
            user_delete_protection_on_by_default=user_delete_protection_on_by_default,
            device_delete_protection_on_by_default=device_delete_protection_on_by_default,
            is_delete_protected=is_delete_protected,
            is_active=is_active,
            last_updated_date=last_updated_date,
            default_locale=default_locale,
            default_from_address=default_from_address,
            reset_token_expire_hours=reset_token_expire_hours,
            access_token_expire_hours=access_token_expire_hours,
            refresh_token_expire_hours=refresh_token_expire_hours,
            session_expire_mins=session_expire_mins,
            pii_admin_only=pii_admin_only,
            ui_config=ui_config,
            use_legacy_data_and_files_permissions=use_legacy_data_and_files_permissions,
            groups_require_delete_permission_to_put_data_by_default=groups_require_delete_permission_to_put_data_by_default,
        )

        org_schema.additional_properties = d
        return org_schema

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
