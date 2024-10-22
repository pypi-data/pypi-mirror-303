from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.crud_permissions import CRUDPermissions


T = TypeVar("T", bound="ProjectAccessPermissions")


@_attrs_define
class ProjectAccessPermissions:
    """Collection of permissions for project access

    Attributes:
        can_update (Union[Unset, bool]):  Default: False.
        can_read (Union[Unset, bool]):  Default: False.
        user_permissions (Union[Unset, CRUDPermissions]): Collection of CRUD permissions
        device_permissions (Union[Unset, CRUDPermissions]): Collection of CRUD permissions
        role_permissions (Union[Unset, CRUDPermissions]): Collection of CRUD permissions
        is_admin (Union[Unset, bool]):  Default: False.
        group_permissions (Union[Unset, CRUDPermissions]): Collection of CRUD permissions
    """

    can_update: Union[Unset, bool] = False
    can_read: Union[Unset, bool] = False
    user_permissions: Union[Unset, "CRUDPermissions"] = UNSET
    device_permissions: Union[Unset, "CRUDPermissions"] = UNSET
    role_permissions: Union[Unset, "CRUDPermissions"] = UNSET
    is_admin: Union[Unset, bool] = False
    group_permissions: Union[Unset, "CRUDPermissions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        can_update = self.can_update

        can_read = self.can_read

        user_permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_permissions, Unset):
            user_permissions = self.user_permissions.to_dict()

        device_permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.device_permissions, Unset):
            device_permissions = self.device_permissions.to_dict()

        role_permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.role_permissions, Unset):
            role_permissions = self.role_permissions.to_dict()

        is_admin = self.is_admin

        group_permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.group_permissions, Unset):
            group_permissions = self.group_permissions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_update is not UNSET:
            field_dict["can_update"] = can_update
        if can_read is not UNSET:
            field_dict["can_read"] = can_read
        if user_permissions is not UNSET:
            field_dict["user_permissions"] = user_permissions
        if device_permissions is not UNSET:
            field_dict["device_permissions"] = device_permissions
        if role_permissions is not UNSET:
            field_dict["role_permissions"] = role_permissions
        if is_admin is not UNSET:
            field_dict["is_admin"] = is_admin
        if group_permissions is not UNSET:
            field_dict["group_permissions"] = group_permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.crud_permissions import CRUDPermissions

        d = src_dict.copy()
        can_update = d.pop("can_update", UNSET)

        can_read = d.pop("can_read", UNSET)

        _user_permissions = d.pop("user_permissions", UNSET)
        user_permissions: Union[Unset, CRUDPermissions]
        if isinstance(_user_permissions, Unset):
            user_permissions = UNSET
        else:
            user_permissions = CRUDPermissions.from_dict(_user_permissions)

        _device_permissions = d.pop("device_permissions", UNSET)
        device_permissions: Union[Unset, CRUDPermissions]
        if isinstance(_device_permissions, Unset):
            device_permissions = UNSET
        else:
            device_permissions = CRUDPermissions.from_dict(_device_permissions)

        _role_permissions = d.pop("role_permissions", UNSET)
        role_permissions: Union[Unset, CRUDPermissions]
        if isinstance(_role_permissions, Unset):
            role_permissions = UNSET
        else:
            role_permissions = CRUDPermissions.from_dict(_role_permissions)

        is_admin = d.pop("is_admin", UNSET)

        _group_permissions = d.pop("group_permissions", UNSET)
        group_permissions: Union[Unset, CRUDPermissions]
        if isinstance(_group_permissions, Unset):
            group_permissions = UNSET
        else:
            group_permissions = CRUDPermissions.from_dict(_group_permissions)

        project_access_permissions = cls(
            can_update=can_update,
            can_read=can_read,
            user_permissions=user_permissions,
            device_permissions=device_permissions,
            role_permissions=role_permissions,
            is_admin=is_admin,
            group_permissions=group_permissions,
        )

        project_access_permissions.additional_properties = d
        return project_access_permissions

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
