import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.account_group_access_schema_data_paths import (
        AccountGroupAccessSchemaDataPaths,
    )
    from ..models.account_group_access_schema_file_paths import (
        AccountGroupAccessSchemaFilePaths,
    )
    from ..models.crud_permissions import CRUDPermissions


T = TypeVar("T", bound="AccountGroupAccessSchema")


@_attrs_define
class AccountGroupAccessSchema:
    """Group access schema plus some info about the group

    Attributes:
        is_delete_protected (bool): This must be set false before the access can be deleted
        created_date (datetime.datetime): Date and time the access was created
        can_read (bool): If true, the account can read this access
        can_update (bool): If true, the account can update this access
        user_permissions (CRUDPermissions): Collection of CRUD permissions
        device_permissions (CRUDPermissions): Collection of CRUD permissions
        tags (List[str]): List of tags on this access object
        group_id (str): ID of the group that has access
        grantee_id (str): ID of the account that has access
        is_admin (bool): If true, the account has admin access
        role_permissions (CRUDPermissions): Collection of CRUD permissions
        is_active (bool): If false, all group access operations are disabled
        data_paths (AccountGroupAccessSchemaDataPaths): Dictionary of accessible data paths
        file_paths (AccountGroupAccessSchemaFilePaths): Dictionary of accessible file paths
        group_name (str):
        group_description (str):
        group_tags (List[str]):
        last_updated_date (Union[Unset, datetime.datetime]): Date and time the access was last updated
        created_by (Union[Unset, str]): ID of the account that created this access
        last_updated_by (Union[Unset, str]): ID of the account that last updated this access
    """

    is_delete_protected: bool
    created_date: datetime.datetime
    can_read: bool
    can_update: bool
    user_permissions: "CRUDPermissions"
    device_permissions: "CRUDPermissions"
    tags: List[str]
    group_id: str
    grantee_id: str
    is_admin: bool
    role_permissions: "CRUDPermissions"
    is_active: bool
    data_paths: "AccountGroupAccessSchemaDataPaths"
    file_paths: "AccountGroupAccessSchemaFilePaths"
    group_name: str
    group_description: str
    group_tags: List[str]
    last_updated_date: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    last_updated_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_delete_protected = self.is_delete_protected

        created_date = self.created_date.isoformat()

        can_read = self.can_read

        can_update = self.can_update

        user_permissions = self.user_permissions.to_dict()

        device_permissions = self.device_permissions.to_dict()

        tags = self.tags

        group_id = self.group_id

        grantee_id = self.grantee_id

        is_admin = self.is_admin

        role_permissions = self.role_permissions.to_dict()

        is_active = self.is_active

        data_paths = self.data_paths.to_dict()

        file_paths = self.file_paths.to_dict()

        group_name = self.group_name

        group_description = self.group_description

        group_tags = self.group_tags

        last_updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.isoformat()

        created_by = self.created_by

        last_updated_by = self.last_updated_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_delete_protected": is_delete_protected,
                "created_date": created_date,
                "can_read": can_read,
                "can_update": can_update,
                "user_permissions": user_permissions,
                "device_permissions": device_permissions,
                "tags": tags,
                "group_id": group_id,
                "grantee_id": grantee_id,
                "is_admin": is_admin,
                "role_permissions": role_permissions,
                "is_active": is_active,
                "data_paths": data_paths,
                "file_paths": file_paths,
                "group_name": group_name,
                "group_description": group_description,
                "group_tags": group_tags,
            }
        )
        if last_updated_date is not UNSET:
            field_dict["last_updated_date"] = last_updated_date
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if last_updated_by is not UNSET:
            field_dict["last_updated_by"] = last_updated_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account_group_access_schema_data_paths import (
            AccountGroupAccessSchemaDataPaths,
        )
        from ..models.account_group_access_schema_file_paths import (
            AccountGroupAccessSchemaFilePaths,
        )
        from ..models.crud_permissions import CRUDPermissions

        d = src_dict.copy()
        is_delete_protected = d.pop("is_delete_protected")

        created_date = isoparse(d.pop("created_date"))

        can_read = d.pop("can_read")

        can_update = d.pop("can_update")

        user_permissions = CRUDPermissions.from_dict(d.pop("user_permissions"))

        device_permissions = CRUDPermissions.from_dict(d.pop("device_permissions"))

        tags = cast(List[str], d.pop("tags"))

        group_id = d.pop("group_id")

        grantee_id = d.pop("grantee_id")

        is_admin = d.pop("is_admin")

        role_permissions = CRUDPermissions.from_dict(d.pop("role_permissions"))

        is_active = d.pop("is_active")

        data_paths = AccountGroupAccessSchemaDataPaths.from_dict(d.pop("data_paths"))

        file_paths = AccountGroupAccessSchemaFilePaths.from_dict(d.pop("file_paths"))

        group_name = d.pop("group_name")

        group_description = d.pop("group_description")

        group_tags = cast(List[str], d.pop("group_tags"))

        _last_updated_date = d.pop("last_updated_date", UNSET)
        last_updated_date: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = isoparse(_last_updated_date)

        created_by = d.pop("created_by", UNSET)

        last_updated_by = d.pop("last_updated_by", UNSET)

        account_group_access_schema = cls(
            is_delete_protected=is_delete_protected,
            created_date=created_date,
            can_read=can_read,
            can_update=can_update,
            user_permissions=user_permissions,
            device_permissions=device_permissions,
            tags=tags,
            group_id=group_id,
            grantee_id=grantee_id,
            is_admin=is_admin,
            role_permissions=role_permissions,
            is_active=is_active,
            data_paths=data_paths,
            file_paths=file_paths,
            group_name=group_name,
            group_description=group_description,
            group_tags=group_tags,
            last_updated_date=last_updated_date,
            created_by=created_by,
            last_updated_by=last_updated_by,
        )

        account_group_access_schema.additional_properties = d
        return account_group_access_schema

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
