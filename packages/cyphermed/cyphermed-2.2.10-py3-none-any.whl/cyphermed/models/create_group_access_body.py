from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.create_group_access_body_data_paths import (
        CreateGroupAccessBodyDataPaths,
    )
    from ..models.create_group_access_body_file_paths import (
        CreateGroupAccessBodyFilePaths,
    )
    from ..models.crud_permissions import CRUDPermissions


T = TypeVar("T", bound="CreateGroupAccessBody")


@_attrs_define
class CreateGroupAccessBody:
    """Which GroupAccess fields to include in POST request bodies

    Attributes:
        is_delete_protected (Union[Unset, bool]): This must be set false before the access can be deleted
        tags (Union[Unset, List[str]]): List of tags on this access object
        user_permissions (Union[Unset, CRUDPermissions]): Collection of CRUD permissions
        device_permissions (Union[Unset, CRUDPermissions]): Collection of CRUD permissions
        can_read (Union[Unset, bool]): If true, the grantee can read the target resource
        can_update (Union[Unset, bool]): If true, the grantee can update the target resource
        role_permissions (Union[Unset, CRUDPermissions]): Collection of CRUD permissions
        is_admin (Union[Unset, bool]): If true, the grantee has admin access to the group
        data_paths (Union[Unset, CreateGroupAccessBodyDataPaths]): Dictionary of accessible data paths and their CRUD
            permissions
        file_paths (Union[Unset, CreateGroupAccessBodyFilePaths]): Dictionary of accessible file paths and their CRUD
            permissions
    """

    is_delete_protected: Union[Unset, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    user_permissions: Union[Unset, "CRUDPermissions"] = UNSET
    device_permissions: Union[Unset, "CRUDPermissions"] = UNSET
    can_read: Union[Unset, bool] = UNSET
    can_update: Union[Unset, bool] = UNSET
    role_permissions: Union[Unset, "CRUDPermissions"] = UNSET
    is_admin: Union[Unset, bool] = UNSET
    data_paths: Union[Unset, "CreateGroupAccessBodyDataPaths"] = UNSET
    file_paths: Union[Unset, "CreateGroupAccessBodyFilePaths"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_delete_protected = self.is_delete_protected

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        user_permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_permissions, Unset):
            user_permissions = self.user_permissions.to_dict()

        device_permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.device_permissions, Unset):
            device_permissions = self.device_permissions.to_dict()

        can_read = self.can_read

        can_update = self.can_update

        role_permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.role_permissions, Unset):
            role_permissions = self.role_permissions.to_dict()

        is_admin = self.is_admin

        data_paths: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_paths, Unset):
            data_paths = self.data_paths.to_dict()

        file_paths: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file_paths, Unset):
            file_paths = self.file_paths.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_delete_protected is not UNSET:
            field_dict["is_delete_protected"] = is_delete_protected
        if tags is not UNSET:
            field_dict["tags"] = tags
        if user_permissions is not UNSET:
            field_dict["user_permissions"] = user_permissions
        if device_permissions is not UNSET:
            field_dict["device_permissions"] = device_permissions
        if can_read is not UNSET:
            field_dict["can_read"] = can_read
        if can_update is not UNSET:
            field_dict["can_update"] = can_update
        if role_permissions is not UNSET:
            field_dict["role_permissions"] = role_permissions
        if is_admin is not UNSET:
            field_dict["is_admin"] = is_admin
        if data_paths is not UNSET:
            field_dict["data_paths"] = data_paths
        if file_paths is not UNSET:
            field_dict["file_paths"] = file_paths

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_group_access_body_data_paths import (
            CreateGroupAccessBodyDataPaths,
        )
        from ..models.create_group_access_body_file_paths import (
            CreateGroupAccessBodyFilePaths,
        )
        from ..models.crud_permissions import CRUDPermissions

        d = src_dict.copy()
        is_delete_protected = d.pop("is_delete_protected", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

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

        can_read = d.pop("can_read", UNSET)

        can_update = d.pop("can_update", UNSET)

        _role_permissions = d.pop("role_permissions", UNSET)
        role_permissions: Union[Unset, CRUDPermissions]
        if isinstance(_role_permissions, Unset):
            role_permissions = UNSET
        else:
            role_permissions = CRUDPermissions.from_dict(_role_permissions)

        is_admin = d.pop("is_admin", UNSET)

        _data_paths = d.pop("data_paths", UNSET)
        data_paths: Union[Unset, CreateGroupAccessBodyDataPaths]
        if isinstance(_data_paths, Unset):
            data_paths = UNSET
        else:
            data_paths = CreateGroupAccessBodyDataPaths.from_dict(_data_paths)

        _file_paths = d.pop("file_paths", UNSET)
        file_paths: Union[Unset, CreateGroupAccessBodyFilePaths]
        if isinstance(_file_paths, Unset):
            file_paths = UNSET
        else:
            file_paths = CreateGroupAccessBodyFilePaths.from_dict(_file_paths)

        create_group_access_body = cls(
            is_delete_protected=is_delete_protected,
            tags=tags,
            user_permissions=user_permissions,
            device_permissions=device_permissions,
            can_read=can_read,
            can_update=can_update,
            role_permissions=role_permissions,
            is_admin=is_admin,
            data_paths=data_paths,
            file_paths=file_paths,
        )

        create_group_access_body.additional_properties = d
        return create_group_access_body

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
