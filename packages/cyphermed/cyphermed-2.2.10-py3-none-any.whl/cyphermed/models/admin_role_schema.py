import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.admin_role_schema_custom_attributes import (
        AdminRoleSchemaCustomAttributes,
    )
    from ..models.admin_role_schema_restricted_custom_attributes import (
        AdminRoleSchemaRestrictedCustomAttributes,
    )
    from ..models.org_access_permissions import OrgAccessPermissions
    from ..models.project_access_permissions import ProjectAccessPermissions


T = TypeVar("T", bound="AdminRoleSchema")


@_attrs_define
class AdminRoleSchema:
    """Which Role fields to include in response bodies for admins

    Attributes:
        id (str): ID of the role
        name (str): Name of the role
        description (str): Description of the role
        is_delete_protected (bool): This must be set false before the role can be deleted
        is_org_admin (bool): Whether this user is an org admin
        tags (List[str]): Tags for this role
        created_date (datetime.datetime): UTC datetime the account was created
        restricted_custom_attributes (AdminRoleSchemaRestrictedCustomAttributes): Custom attributes only admins can
            update
        is_active (bool): If false, all role operations are disabled
        created_by (Union[Unset, str]): ID of the user who created this account
        last_updated_by (Union[Unset, str]): ID of the user who last updated this account
        last_updated_date (Union[Unset, datetime.datetime]): UTC datetime the account was last updated
        project_id (Union[Unset, str]): ID of the project this group belongs to, if any
        is_project_admin (Union[Unset, bool]): Whether this user is a project admin, only visible in project scope
        is_group_admin (Union[Unset, bool]): Whether this user is a group admin, only visible when filtered by group
        custom_attributes (Union[Unset, AdminRoleSchemaCustomAttributes]): Custom attributes for this user
        project_ids (Union[Unset, List[str]]): Projects they belong to, individual roles only
        group_ids (Union[Unset, List[str]]): Groups they belong to, individual roles only
        project_permissions (Union[Unset, ProjectAccessPermissions]): Collection of permissions for project access
        org_permissions (Union[Unset, OrgAccessPermissions]): Collection of permissions for org access
    """

    id: str
    name: str
    description: str
    is_delete_protected: bool
    is_org_admin: bool
    tags: List[str]
    created_date: datetime.datetime
    restricted_custom_attributes: "AdminRoleSchemaRestrictedCustomAttributes"
    is_active: bool
    created_by: Union[Unset, str] = UNSET
    last_updated_by: Union[Unset, str] = UNSET
    last_updated_date: Union[Unset, datetime.datetime] = UNSET
    project_id: Union[Unset, str] = UNSET
    is_project_admin: Union[Unset, bool] = UNSET
    is_group_admin: Union[Unset, bool] = UNSET
    custom_attributes: Union[Unset, "AdminRoleSchemaCustomAttributes"] = UNSET
    project_ids: Union[Unset, List[str]] = UNSET
    group_ids: Union[Unset, List[str]] = UNSET
    project_permissions: Union[Unset, "ProjectAccessPermissions"] = UNSET
    org_permissions: Union[Unset, "OrgAccessPermissions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        is_delete_protected = self.is_delete_protected

        is_org_admin = self.is_org_admin

        tags = self.tags

        created_date = self.created_date.isoformat()

        restricted_custom_attributes = self.restricted_custom_attributes.to_dict()

        is_active = self.is_active

        created_by = self.created_by

        last_updated_by = self.last_updated_by

        last_updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.isoformat()

        project_id = self.project_id

        is_project_admin = self.is_project_admin

        is_group_admin = self.is_group_admin

        custom_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_attributes, Unset):
            custom_attributes = self.custom_attributes.to_dict()

        project_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.project_ids, Unset):
            project_ids = self.project_ids

        group_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        project_permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project_permissions, Unset):
            project_permissions = self.project_permissions.to_dict()

        org_permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.org_permissions, Unset):
            org_permissions = self.org_permissions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "is_delete_protected": is_delete_protected,
                "is_org_admin": is_org_admin,
                "tags": tags,
                "created_date": created_date,
                "restricted_custom_attributes": restricted_custom_attributes,
                "is_active": is_active,
            }
        )
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if last_updated_by is not UNSET:
            field_dict["last_updated_by"] = last_updated_by
        if last_updated_date is not UNSET:
            field_dict["last_updated_date"] = last_updated_date
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if is_project_admin is not UNSET:
            field_dict["is_project_admin"] = is_project_admin
        if is_group_admin is not UNSET:
            field_dict["is_group_admin"] = is_group_admin
        if custom_attributes is not UNSET:
            field_dict["custom_attributes"] = custom_attributes
        if project_ids is not UNSET:
            field_dict["project_ids"] = project_ids
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if project_permissions is not UNSET:
            field_dict["project_permissions"] = project_permissions
        if org_permissions is not UNSET:
            field_dict["org_permissions"] = org_permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.admin_role_schema_custom_attributes import (
            AdminRoleSchemaCustomAttributes,
        )
        from ..models.admin_role_schema_restricted_custom_attributes import (
            AdminRoleSchemaRestrictedCustomAttributes,
        )
        from ..models.org_access_permissions import OrgAccessPermissions
        from ..models.project_access_permissions import ProjectAccessPermissions

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        is_delete_protected = d.pop("is_delete_protected")

        is_org_admin = d.pop("is_org_admin")

        tags = cast(List[str], d.pop("tags"))

        created_date = isoparse(d.pop("created_date"))

        restricted_custom_attributes = AdminRoleSchemaRestrictedCustomAttributes.from_dict(
            d.pop("restricted_custom_attributes")
        )

        is_active = d.pop("is_active")

        created_by = d.pop("created_by", UNSET)

        last_updated_by = d.pop("last_updated_by", UNSET)

        _last_updated_date = d.pop("last_updated_date", UNSET)
        last_updated_date: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = isoparse(_last_updated_date)

        project_id = d.pop("project_id", UNSET)

        is_project_admin = d.pop("is_project_admin", UNSET)

        is_group_admin = d.pop("is_group_admin", UNSET)

        _custom_attributes = d.pop("custom_attributes", UNSET)
        custom_attributes: Union[Unset, AdminRoleSchemaCustomAttributes]
        if isinstance(_custom_attributes, Unset):
            custom_attributes = UNSET
        else:
            custom_attributes = AdminRoleSchemaCustomAttributes.from_dict(_custom_attributes)

        project_ids = cast(List[str], d.pop("project_ids", UNSET))

        group_ids = cast(List[str], d.pop("group_ids", UNSET))

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

        admin_role_schema = cls(
            id=id,
            name=name,
            description=description,
            is_delete_protected=is_delete_protected,
            is_org_admin=is_org_admin,
            tags=tags,
            created_date=created_date,
            restricted_custom_attributes=restricted_custom_attributes,
            is_active=is_active,
            created_by=created_by,
            last_updated_by=last_updated_by,
            last_updated_date=last_updated_date,
            project_id=project_id,
            is_project_admin=is_project_admin,
            is_group_admin=is_group_admin,
            custom_attributes=custom_attributes,
            project_ids=project_ids,
            group_ids=group_ids,
            project_permissions=project_permissions,
            org_permissions=org_permissions,
        )

        admin_role_schema.additional_properties = d
        return admin_role_schema

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
