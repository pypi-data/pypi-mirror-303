import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.admin_user_schema_custom_attributes import (
        AdminUserSchemaCustomAttributes,
    )
    from ..models.admin_user_schema_restricted_custom_attributes import (
        AdminUserSchemaRestrictedCustomAttributes,
    )
    from ..models.org_access_permissions import OrgAccessPermissions
    from ..models.project_access_permissions import ProjectAccessPermissions


T = TypeVar("T", bound="AdminUserSchema")


@_attrs_define
class AdminUserSchema:
    """Which User fields to include in response bodies

    Attributes:
        locale (str):
        zoneinfo (str):
        username (str):
        email (str):
        new_password_required (bool): State of user not having permanent password
        has_temporary_password (bool): Whether this user has a temporary password
        id (str): ID of the account
        created_date (datetime.datetime): UTC datetime the account was created
        tags (List[str]): Tags for this user
        custom_attributes (AdminUserSchemaCustomAttributes): Custom attributes for this user
        restricted_custom_attributes (AdminUserSchemaRestrictedCustomAttributes): Custom attributes only admins can
            update
        mfa_enabled (bool): Whether MFA is enabled for this user
        sms_mfa_enabled (bool): Whether SMS MFA is enabled for this user
        software_mfa_enabled (bool): Whether software MFA is enabled for this user
        is_active (bool): Whether this user is active
        is_delete_protected (Union[Unset, bool]):  Default: False.
        picture (Union[Unset, str]):
        picture_base64 (Union[Unset, str]):
        picture_content_type (Union[Unset, str]):
        password_last_changed (Union[Unset, datetime.datetime]): UTC datetime the user last changed password
        phone_number (Union[Unset, str]):
        phone_number_verified (Union[Unset, bool]):  Default: False.
        nickname (Union[Unset, str]):
        first_name (Union[Unset, str]):
        middle_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        is_org_admin (Union[Unset, bool]):  Default: False.
        created_by (Union[Unset, str]): ID of the user who created this account
        last_updated_by (Union[Unset, str]): ID of the user who last updated this account
        last_updated_date (Union[Unset, datetime.datetime]): UTC datetime the account was last updated
        last_seen (Union[Unset, datetime.datetime]): UTC datetime the user was last seen
        preferred_mfa (Union[Unset, str]): Preferred MFA method for this user
        is_project_admin (Union[Unset, bool]): Whether this user is a project admin, only visible when filtered by
            project
        is_group_admin (Union[Unset, bool]): Whether this user is a group admin, only visible when filtered by group
        project_permissions (Union[Unset, ProjectAccessPermissions]): Collection of permissions for project access
        org_permissions (Union[Unset, OrgAccessPermissions]): Collection of permissions for org access
        project_ids (Union[Unset, List[str]]): Projects they belong to, individual users only
        group_ids (Union[Unset, List[str]]): Groups they belong to, individual users only
        role_ids (Union[Unset, List[str]]): Roles they belong to, individual users only
    """

    locale: str
    zoneinfo: str
    username: str
    email: str
    new_password_required: bool
    has_temporary_password: bool
    id: str
    created_date: datetime.datetime
    tags: List[str]
    custom_attributes: "AdminUserSchemaCustomAttributes"
    restricted_custom_attributes: "AdminUserSchemaRestrictedCustomAttributes"
    mfa_enabled: bool
    sms_mfa_enabled: bool
    software_mfa_enabled: bool
    is_active: bool
    is_delete_protected: Union[Unset, bool] = False
    picture: Union[Unset, str] = UNSET
    picture_base64: Union[Unset, str] = UNSET
    picture_content_type: Union[Unset, str] = UNSET
    password_last_changed: Union[Unset, datetime.datetime] = UNSET
    phone_number: Union[Unset, str] = UNSET
    phone_number_verified: Union[Unset, bool] = False
    nickname: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    is_org_admin: Union[Unset, bool] = False
    created_by: Union[Unset, str] = UNSET
    last_updated_by: Union[Unset, str] = UNSET
    last_updated_date: Union[Unset, datetime.datetime] = UNSET
    last_seen: Union[Unset, datetime.datetime] = UNSET
    preferred_mfa: Union[Unset, str] = UNSET
    is_project_admin: Union[Unset, bool] = UNSET
    is_group_admin: Union[Unset, bool] = UNSET
    project_permissions: Union[Unset, "ProjectAccessPermissions"] = UNSET
    org_permissions: Union[Unset, "OrgAccessPermissions"] = UNSET
    project_ids: Union[Unset, List[str]] = UNSET
    group_ids: Union[Unset, List[str]] = UNSET
    role_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        locale = self.locale

        zoneinfo = self.zoneinfo

        username = self.username

        email = self.email

        new_password_required = self.new_password_required

        has_temporary_password = self.has_temporary_password

        id = self.id

        created_date = self.created_date.isoformat()

        tags = self.tags

        custom_attributes = self.custom_attributes.to_dict()

        restricted_custom_attributes = self.restricted_custom_attributes.to_dict()

        mfa_enabled = self.mfa_enabled

        sms_mfa_enabled = self.sms_mfa_enabled

        software_mfa_enabled = self.software_mfa_enabled

        is_active = self.is_active

        is_delete_protected = self.is_delete_protected

        picture = self.picture

        picture_base64 = self.picture_base64

        picture_content_type = self.picture_content_type

        password_last_changed: Union[Unset, str] = UNSET
        if not isinstance(self.password_last_changed, Unset):
            password_last_changed = self.password_last_changed.isoformat()

        phone_number = self.phone_number

        phone_number_verified = self.phone_number_verified

        nickname = self.nickname

        first_name = self.first_name

        middle_name = self.middle_name

        last_name = self.last_name

        is_org_admin = self.is_org_admin

        created_by = self.created_by

        last_updated_by = self.last_updated_by

        last_updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.isoformat()

        last_seen: Union[Unset, str] = UNSET
        if not isinstance(self.last_seen, Unset):
            last_seen = self.last_seen.isoformat()

        preferred_mfa = self.preferred_mfa

        is_project_admin = self.is_project_admin

        is_group_admin = self.is_group_admin

        project_permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project_permissions, Unset):
            project_permissions = self.project_permissions.to_dict()

        org_permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.org_permissions, Unset):
            org_permissions = self.org_permissions.to_dict()

        project_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.project_ids, Unset):
            project_ids = self.project_ids

        group_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        role_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.role_ids, Unset):
            role_ids = self.role_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locale": locale,
                "zoneinfo": zoneinfo,
                "username": username,
                "email": email,
                "new_password_required": new_password_required,
                "has_temporary_password": has_temporary_password,
                "id": id,
                "created_date": created_date,
                "tags": tags,
                "custom_attributes": custom_attributes,
                "restricted_custom_attributes": restricted_custom_attributes,
                "mfa_enabled": mfa_enabled,
                "sms_mfa_enabled": sms_mfa_enabled,
                "software_mfa_enabled": software_mfa_enabled,
                "is_active": is_active,
            }
        )
        if is_delete_protected is not UNSET:
            field_dict["is_delete_protected"] = is_delete_protected
        if picture is not UNSET:
            field_dict["picture"] = picture
        if picture_base64 is not UNSET:
            field_dict["picture_base64"] = picture_base64
        if picture_content_type is not UNSET:
            field_dict["picture_content_type"] = picture_content_type
        if password_last_changed is not UNSET:
            field_dict["password_last_changed"] = password_last_changed
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if phone_number_verified is not UNSET:
            field_dict["phone_number_verified"] = phone_number_verified
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if is_org_admin is not UNSET:
            field_dict["is_org_admin"] = is_org_admin
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if last_updated_by is not UNSET:
            field_dict["last_updated_by"] = last_updated_by
        if last_updated_date is not UNSET:
            field_dict["last_updated_date"] = last_updated_date
        if last_seen is not UNSET:
            field_dict["last_seen"] = last_seen
        if preferred_mfa is not UNSET:
            field_dict["preferred_mfa"] = preferred_mfa
        if is_project_admin is not UNSET:
            field_dict["is_project_admin"] = is_project_admin
        if is_group_admin is not UNSET:
            field_dict["is_group_admin"] = is_group_admin
        if project_permissions is not UNSET:
            field_dict["project_permissions"] = project_permissions
        if org_permissions is not UNSET:
            field_dict["org_permissions"] = org_permissions
        if project_ids is not UNSET:
            field_dict["project_ids"] = project_ids
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if role_ids is not UNSET:
            field_dict["role_ids"] = role_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.admin_user_schema_custom_attributes import (
            AdminUserSchemaCustomAttributes,
        )
        from ..models.admin_user_schema_restricted_custom_attributes import (
            AdminUserSchemaRestrictedCustomAttributes,
        )
        from ..models.org_access_permissions import OrgAccessPermissions
        from ..models.project_access_permissions import ProjectAccessPermissions

        d = src_dict.copy()
        locale = d.pop("locale")

        zoneinfo = d.pop("zoneinfo")

        username = d.pop("username")

        email = d.pop("email")

        new_password_required = d.pop("new_password_required")

        has_temporary_password = d.pop("has_temporary_password")

        id = d.pop("id")

        created_date = isoparse(d.pop("created_date"))

        tags = cast(List[str], d.pop("tags"))

        custom_attributes = AdminUserSchemaCustomAttributes.from_dict(d.pop("custom_attributes"))

        restricted_custom_attributes = AdminUserSchemaRestrictedCustomAttributes.from_dict(
            d.pop("restricted_custom_attributes")
        )

        mfa_enabled = d.pop("mfa_enabled")

        sms_mfa_enabled = d.pop("sms_mfa_enabled")

        software_mfa_enabled = d.pop("software_mfa_enabled")

        is_active = d.pop("is_active")

        is_delete_protected = d.pop("is_delete_protected", UNSET)

        picture = d.pop("picture", UNSET)

        picture_base64 = d.pop("picture_base64", UNSET)

        picture_content_type = d.pop("picture_content_type", UNSET)

        _password_last_changed = d.pop("password_last_changed", UNSET)
        password_last_changed: Union[Unset, datetime.datetime]
        if isinstance(_password_last_changed, Unset):
            password_last_changed = UNSET
        else:
            password_last_changed = isoparse(_password_last_changed)

        phone_number = d.pop("phone_number", UNSET)

        phone_number_verified = d.pop("phone_number_verified", UNSET)

        nickname = d.pop("nickname", UNSET)

        first_name = d.pop("first_name", UNSET)

        middle_name = d.pop("middle_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        is_org_admin = d.pop("is_org_admin", UNSET)

        created_by = d.pop("created_by", UNSET)

        last_updated_by = d.pop("last_updated_by", UNSET)

        _last_updated_date = d.pop("last_updated_date", UNSET)
        last_updated_date: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = isoparse(_last_updated_date)

        _last_seen = d.pop("last_seen", UNSET)
        last_seen: Union[Unset, datetime.datetime]
        if isinstance(_last_seen, Unset):
            last_seen = UNSET
        else:
            last_seen = isoparse(_last_seen)

        preferred_mfa = d.pop("preferred_mfa", UNSET)

        is_project_admin = d.pop("is_project_admin", UNSET)

        is_group_admin = d.pop("is_group_admin", UNSET)

        _project_permissions = d.pop("project_permissions", UNSET)
        project_permissions: Union[Unset, ProjectAccessPermissions]
        if isinstance(_project_permissions, Unset):
            project_permissions = UNSET
        else:
            project_permissions = ProjectAccessPermissions.from_dict(_project_permissions)

        _org_permissions = d.pop("org_permissions", UNSET)
        org_permissions: Union[Unset, OrgAccessPermissions]
        if isinstance(_org_permissions, Unset):
            org_permissions = UNSET
        else:
            org_permissions = OrgAccessPermissions.from_dict(_org_permissions)

        project_ids = cast(List[str], d.pop("project_ids", UNSET))

        group_ids = cast(List[str], d.pop("group_ids", UNSET))

        role_ids = cast(List[str], d.pop("role_ids", UNSET))

        admin_user_schema = cls(
            locale=locale,
            zoneinfo=zoneinfo,
            username=username,
            email=email,
            new_password_required=new_password_required,
            has_temporary_password=has_temporary_password,
            id=id,
            created_date=created_date,
            tags=tags,
            custom_attributes=custom_attributes,
            restricted_custom_attributes=restricted_custom_attributes,
            mfa_enabled=mfa_enabled,
            sms_mfa_enabled=sms_mfa_enabled,
            software_mfa_enabled=software_mfa_enabled,
            is_active=is_active,
            is_delete_protected=is_delete_protected,
            picture=picture,
            picture_base64=picture_base64,
            picture_content_type=picture_content_type,
            password_last_changed=password_last_changed,
            phone_number=phone_number,
            phone_number_verified=phone_number_verified,
            nickname=nickname,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            is_org_admin=is_org_admin,
            created_by=created_by,
            last_updated_by=last_updated_by,
            last_updated_date=last_updated_date,
            last_seen=last_seen,
            preferred_mfa=preferred_mfa,
            is_project_admin=is_project_admin,
            is_group_admin=is_group_admin,
            project_permissions=project_permissions,
            org_permissions=org_permissions,
            project_ids=project_ids,
            group_ids=group_ids,
            role_ids=role_ids,
        )

        admin_user_schema.additional_properties = d
        return admin_user_schema

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
