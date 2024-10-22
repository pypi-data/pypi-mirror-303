from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.org_access_permissions import OrgAccessPermissions
    from ..models.project_access_permissions import ProjectAccessPermissions


T = TypeVar("T", bound="CurrentSessionAccessInfo")


@_attrs_define
class CurrentSessionAccessInfo:
    """Current session access info

    Attributes:
        org_permissions (OrgAccessPermissions): Collection of permissions for org access
        project_permissions (Union[Unset, ProjectAccessPermissions]): Collection of permissions for project access
    """

    org_permissions: "OrgAccessPermissions"
    project_permissions: Union[Unset, "ProjectAccessPermissions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        org_permissions = self.org_permissions.to_dict()

        project_permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project_permissions, Unset):
            project_permissions = self.project_permissions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "org_permissions": org_permissions,
            }
        )
        if project_permissions is not UNSET:
            field_dict["project_permissions"] = project_permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.org_access_permissions import OrgAccessPermissions
        from ..models.project_access_permissions import ProjectAccessPermissions

        d = src_dict.copy()
        org_permissions = OrgAccessPermissions.from_dict(d.pop("org_permissions"))

        _project_permissions = d.pop("project_permissions", UNSET)
        project_permissions: Union[Unset, ProjectAccessPermissions]
        if isinstance(_project_permissions, Unset):
            project_permissions = UNSET
        else:
            project_permissions = ProjectAccessPermissions.from_dict(_project_permissions)

        current_session_access_info = cls(
            org_permissions=org_permissions,
            project_permissions=project_permissions,
        )

        current_session_access_info.additional_properties = d
        return current_session_access_info

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
