from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.crud_permissions import CRUDPermissions


T = TypeVar("T", bound="PatchRoleAccessBody")


@_attrs_define
class PatchRoleAccessBody:
    """Which RoleAccess fields to include in request bodies

    Attributes:
        is_delete_protected (Union[Unset, bool]): This must be set false before the access can be deleted
        tags (Union[Unset, List[str]]): List of tags on this access object
        user_permissions (Union[Unset, CRUDPermissions]): Collection of CRUD permissions
        device_permissions (Union[Unset, CRUDPermissions]): Collection of CRUD permissions
        can_read (Union[Unset, bool]): If true, the grantee can read the target resource
        can_update (Union[Unset, bool]): If true, the grantee can update the target resource
        is_active (Union[Unset, bool]): If false, all role access operations are disabled
    """

    is_delete_protected: Union[Unset, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    user_permissions: Union[Unset, "CRUDPermissions"] = UNSET
    device_permissions: Union[Unset, "CRUDPermissions"] = UNSET
    can_read: Union[Unset, bool] = UNSET
    can_update: Union[Unset, bool] = UNSET
    is_active: Union[Unset, bool] = UNSET
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

        is_active = self.is_active

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
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        is_active = d.pop("is_active", UNSET)

        patch_role_access_body = cls(
            is_delete_protected=is_delete_protected,
            tags=tags,
            user_permissions=user_permissions,
            device_permissions=device_permissions,
            can_read=can_read,
            can_update=can_update,
            is_active=is_active,
        )

        patch_role_access_body.additional_properties = d
        return patch_role_access_body

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
