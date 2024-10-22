from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.create_role_body_custom_attributes import (
        CreateRoleBodyCustomAttributes,
    )
    from ..models.create_role_body_restricted_custom_attributes import (
        CreateRoleBodyRestrictedCustomAttributes,
    )
    from ..models.org_access_permissions import OrgAccessPermissions
    from ..models.project_access_permissions import ProjectAccessPermissions


T = TypeVar("T", bound="CreateRoleBody")


@_attrs_define
class CreateRoleBody:
    """Which Role fields to include in request bodies

    Attributes:
        name (str): Name of the role
        description (Union[Unset, str]): Description of the role
        is_delete_protected (Union[Unset, bool]): This must be set false before the role can be deleted
        tags (Union[Unset, List[str]]): List of tags on this role
        org_permissions (Union[Unset, OrgAccessPermissions]): Collection of permissions for org access
        project_permissions (Union[Unset, ProjectAccessPermissions]): Collection of permissions for project access
        custom_attributes (Union[Unset, CreateRoleBodyCustomAttributes]): Custom attributes for this user
        restricted_custom_attributes (Union[Unset, CreateRoleBodyRestrictedCustomAttributes]): Custom attributes only
            admins can update
        project_id (Union[Unset, str]): ID of the project the role is linked with, if any
        create_own_access (Union[Unset, bool]): If true, full access to the role is automatically created for the
            requester Default: False.
    """

    name: str
    description: Union[Unset, str] = UNSET
    is_delete_protected: Union[Unset, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    org_permissions: Union[Unset, "OrgAccessPermissions"] = UNSET
    project_permissions: Union[Unset, "ProjectAccessPermissions"] = UNSET
    custom_attributes: Union[Unset, "CreateRoleBodyCustomAttributes"] = UNSET
    restricted_custom_attributes: Union[Unset, "CreateRoleBodyRestrictedCustomAttributes"] = UNSET
    project_id: Union[Unset, str] = UNSET
    create_own_access: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        is_delete_protected = self.is_delete_protected

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        org_permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.org_permissions, Unset):
            org_permissions = self.org_permissions.to_dict()

        project_permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project_permissions, Unset):
            project_permissions = self.project_permissions.to_dict()

        custom_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_attributes, Unset):
            custom_attributes = self.custom_attributes.to_dict()

        restricted_custom_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.restricted_custom_attributes, Unset):
            restricted_custom_attributes = self.restricted_custom_attributes.to_dict()

        project_id = self.project_id

        create_own_access = self.create_own_access

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_delete_protected is not UNSET:
            field_dict["is_delete_protected"] = is_delete_protected
        if tags is not UNSET:
            field_dict["tags"] = tags
        if org_permissions is not UNSET:
            field_dict["org_permissions"] = org_permissions
        if project_permissions is not UNSET:
            field_dict["project_permissions"] = project_permissions
        if custom_attributes is not UNSET:
            field_dict["custom_attributes"] = custom_attributes
        if restricted_custom_attributes is not UNSET:
            field_dict["restricted_custom_attributes"] = restricted_custom_attributes
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if create_own_access is not UNSET:
            field_dict["create_own_access"] = create_own_access

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_role_body_custom_attributes import (
            CreateRoleBodyCustomAttributes,
        )
        from ..models.create_role_body_restricted_custom_attributes import (
            CreateRoleBodyRestrictedCustomAttributes,
        )
        from ..models.org_access_permissions import OrgAccessPermissions
        from ..models.project_access_permissions import ProjectAccessPermissions

        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description", UNSET)

        is_delete_protected = d.pop("is_delete_protected", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        _org_permissions = d.pop("org_permissions", UNSET)
        org_permissions: Union[Unset, OrgAccessPermissions]
        if isinstance(_org_permissions, Unset):
            org_permissions = UNSET
        else:
            org_permissions = OrgAccessPermissions.from_dict(_org_permissions)

        _project_permissions = d.pop("project_permissions", UNSET)
        project_permissions: Union[Unset, ProjectAccessPermissions]
        if isinstance(_project_permissions, Unset):
            project_permissions = UNSET
        else:
            project_permissions = ProjectAccessPermissions.from_dict(_project_permissions)

        _custom_attributes = d.pop("custom_attributes", UNSET)
        custom_attributes: Union[Unset, CreateRoleBodyCustomAttributes]
        if isinstance(_custom_attributes, Unset):
            custom_attributes = UNSET
        else:
            custom_attributes = CreateRoleBodyCustomAttributes.from_dict(_custom_attributes)

        _restricted_custom_attributes = d.pop("restricted_custom_attributes", UNSET)
        restricted_custom_attributes: Union[Unset, CreateRoleBodyRestrictedCustomAttributes]
        if isinstance(_restricted_custom_attributes, Unset):
            restricted_custom_attributes = UNSET
        else:
            restricted_custom_attributes = CreateRoleBodyRestrictedCustomAttributes.from_dict(
                _restricted_custom_attributes
            )

        project_id = d.pop("project_id", UNSET)

        create_own_access = d.pop("create_own_access", UNSET)

        create_role_body = cls(
            name=name,
            description=description,
            is_delete_protected=is_delete_protected,
            tags=tags,
            org_permissions=org_permissions,
            project_permissions=project_permissions,
            custom_attributes=custom_attributes,
            restricted_custom_attributes=restricted_custom_attributes,
            project_id=project_id,
            create_own_access=create_own_access,
        )

        create_role_body.additional_properties = d
        return create_role_body

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
