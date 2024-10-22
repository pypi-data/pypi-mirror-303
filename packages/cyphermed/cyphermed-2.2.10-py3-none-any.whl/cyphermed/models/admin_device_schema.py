import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.admin_device_schema_custom_attributes import (
        AdminDeviceSchemaCustomAttributes,
    )
    from ..models.admin_device_schema_iot_scopes import AdminDeviceSchemaIotScopes
    from ..models.admin_device_schema_restricted_custom_attributes import (
        AdminDeviceSchemaRestrictedCustomAttributes,
    )
    from ..models.org_access_permissions import OrgAccessPermissions
    from ..models.project_access_permissions import ProjectAccessPermissions
    from ..models.tunnel import Tunnel


T = TypeVar("T", bound="AdminDeviceSchema")


@_attrs_define
class AdminDeviceSchema:
    """Which Device fields to include in response bodies

    Attributes:
        name (str):
        locale (str):
        zoneinfo (str):
        id (str): ID of the account
        created_date (datetime.datetime): UTC datetime the account was created
        tags (List[str]): Tags for this device
        open_tunnels (List['Tunnel']): List of open tunnels to this device
        custom_attributes (AdminDeviceSchemaCustomAttributes): Custom attributes for this device
        restricted_custom_attributes (AdminDeviceSchemaRestrictedCustomAttributes): Custom attributes only admins can
            update
        iot_scopes (AdminDeviceSchemaIotScopes): PubSub permissions per IoT scope for this device
        is_active (bool): Is this account active?
        is_delete_protected (Union[Unset, bool]):  Default: False.
        manufacturer (Union[Unset, str]):
        product (Union[Unset, str]):
        site (Union[Unset, str]):
        serial_number (Union[Unset, str]):
        mac_address (Union[Unset, str]):
        is_org_admin (Union[Unset, bool]):  Default: False.
        picture (Union[Unset, str]):
        picture_base64 (Union[Unset, str]):
        picture_content_type (Union[Unset, str]):
        project_id (Union[Unset, str]): ID of the project this group belongs to, if any
        is_project_admin (Union[Unset, bool]): Whether this user is a project admin, only visible in project scope
        is_group_admin (Union[Unset, bool]): Whether this user is a group admin, only visible when filtered by group
        created_by (Union[Unset, str]): ID of the user who created this account
        last_updated_by (Union[Unset, str]): ID of the user who last updated this account
        last_updated_date (Union[Unset, datetime.datetime]): UTC datetime the account was last updated
        api_key_last_changed (Union[Unset, datetime.datetime]): UTC datetime the API key was last changed
        mqtt_credentials_last_changed (Union[Unset, datetime.datetime]): UTC datetime the MQTT credentials were last
            changed
        last_seen (Union[Unset, datetime.datetime]): UTC datetime the device was last seen
        owner_id (Union[Unset, str]): ID of the device owner
        project_ids (Union[Unset, List[str]]): Projects they belong to, individual devices only
        group_ids (Union[Unset, List[str]]): Groups they belong to, individual devices only
        role_ids (Union[Unset, List[str]]): Roles they belong to, individual devices only
        project_permissions (Union[Unset, ProjectAccessPermissions]): Collection of permissions for project access
        org_permissions (Union[Unset, OrgAccessPermissions]): Collection of permissions for org access
    """

    name: str
    locale: str
    zoneinfo: str
    id: str
    created_date: datetime.datetime
    tags: List[str]
    open_tunnels: List["Tunnel"]
    custom_attributes: "AdminDeviceSchemaCustomAttributes"
    restricted_custom_attributes: "AdminDeviceSchemaRestrictedCustomAttributes"
    iot_scopes: "AdminDeviceSchemaIotScopes"
    is_active: bool
    is_delete_protected: Union[Unset, bool] = False
    manufacturer: Union[Unset, str] = UNSET
    product: Union[Unset, str] = UNSET
    site: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    mac_address: Union[Unset, str] = UNSET
    is_org_admin: Union[Unset, bool] = False
    picture: Union[Unset, str] = UNSET
    picture_base64: Union[Unset, str] = UNSET
    picture_content_type: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    is_project_admin: Union[Unset, bool] = UNSET
    is_group_admin: Union[Unset, bool] = UNSET
    created_by: Union[Unset, str] = UNSET
    last_updated_by: Union[Unset, str] = UNSET
    last_updated_date: Union[Unset, datetime.datetime] = UNSET
    api_key_last_changed: Union[Unset, datetime.datetime] = UNSET
    mqtt_credentials_last_changed: Union[Unset, datetime.datetime] = UNSET
    last_seen: Union[Unset, datetime.datetime] = UNSET
    owner_id: Union[Unset, str] = UNSET
    project_ids: Union[Unset, List[str]] = UNSET
    group_ids: Union[Unset, List[str]] = UNSET
    role_ids: Union[Unset, List[str]] = UNSET
    project_permissions: Union[Unset, "ProjectAccessPermissions"] = UNSET
    org_permissions: Union[Unset, "OrgAccessPermissions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        locale = self.locale

        zoneinfo = self.zoneinfo

        id = self.id

        created_date = self.created_date.isoformat()

        tags = self.tags

        open_tunnels = []
        for open_tunnels_item_data in self.open_tunnels:
            open_tunnels_item = open_tunnels_item_data.to_dict()
            open_tunnels.append(open_tunnels_item)

        custom_attributes = self.custom_attributes.to_dict()

        restricted_custom_attributes = self.restricted_custom_attributes.to_dict()

        iot_scopes = self.iot_scopes.to_dict()

        is_active = self.is_active

        is_delete_protected = self.is_delete_protected

        manufacturer = self.manufacturer

        product = self.product

        site = self.site

        serial_number = self.serial_number

        mac_address = self.mac_address

        is_org_admin = self.is_org_admin

        picture = self.picture

        picture_base64 = self.picture_base64

        picture_content_type = self.picture_content_type

        project_id = self.project_id

        is_project_admin = self.is_project_admin

        is_group_admin = self.is_group_admin

        created_by = self.created_by

        last_updated_by = self.last_updated_by

        last_updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.isoformat()

        api_key_last_changed: Union[Unset, str] = UNSET
        if not isinstance(self.api_key_last_changed, Unset):
            api_key_last_changed = self.api_key_last_changed.isoformat()

        mqtt_credentials_last_changed: Union[Unset, str] = UNSET
        if not isinstance(self.mqtt_credentials_last_changed, Unset):
            mqtt_credentials_last_changed = self.mqtt_credentials_last_changed.isoformat()

        last_seen: Union[Unset, str] = UNSET
        if not isinstance(self.last_seen, Unset):
            last_seen = self.last_seen.isoformat()

        owner_id = self.owner_id

        project_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.project_ids, Unset):
            project_ids = self.project_ids

        group_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        role_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.role_ids, Unset):
            role_ids = self.role_ids

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
                "name": name,
                "locale": locale,
                "zoneinfo": zoneinfo,
                "id": id,
                "created_date": created_date,
                "tags": tags,
                "open_tunnels": open_tunnels,
                "custom_attributes": custom_attributes,
                "restricted_custom_attributes": restricted_custom_attributes,
                "iot_scopes": iot_scopes,
                "is_active": is_active,
            }
        )
        if is_delete_protected is not UNSET:
            field_dict["is_delete_protected"] = is_delete_protected
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if product is not UNSET:
            field_dict["product"] = product
        if site is not UNSET:
            field_dict["site"] = site
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number
        if mac_address is not UNSET:
            field_dict["mac_address"] = mac_address
        if is_org_admin is not UNSET:
            field_dict["is_org_admin"] = is_org_admin
        if picture is not UNSET:
            field_dict["picture"] = picture
        if picture_base64 is not UNSET:
            field_dict["picture_base64"] = picture_base64
        if picture_content_type is not UNSET:
            field_dict["picture_content_type"] = picture_content_type
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if is_project_admin is not UNSET:
            field_dict["is_project_admin"] = is_project_admin
        if is_group_admin is not UNSET:
            field_dict["is_group_admin"] = is_group_admin
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if last_updated_by is not UNSET:
            field_dict["last_updated_by"] = last_updated_by
        if last_updated_date is not UNSET:
            field_dict["last_updated_date"] = last_updated_date
        if api_key_last_changed is not UNSET:
            field_dict["api_key_last_changed"] = api_key_last_changed
        if mqtt_credentials_last_changed is not UNSET:
            field_dict["mqtt_credentials_last_changed"] = mqtt_credentials_last_changed
        if last_seen is not UNSET:
            field_dict["last_seen"] = last_seen
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if project_ids is not UNSET:
            field_dict["project_ids"] = project_ids
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if role_ids is not UNSET:
            field_dict["role_ids"] = role_ids
        if project_permissions is not UNSET:
            field_dict["project_permissions"] = project_permissions
        if org_permissions is not UNSET:
            field_dict["org_permissions"] = org_permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.admin_device_schema_custom_attributes import (
            AdminDeviceSchemaCustomAttributes,
        )
        from ..models.admin_device_schema_iot_scopes import AdminDeviceSchemaIotScopes
        from ..models.admin_device_schema_restricted_custom_attributes import (
            AdminDeviceSchemaRestrictedCustomAttributes,
        )
        from ..models.org_access_permissions import OrgAccessPermissions
        from ..models.project_access_permissions import ProjectAccessPermissions
        from ..models.tunnel import Tunnel

        d = src_dict.copy()
        name = d.pop("name")

        locale = d.pop("locale")

        zoneinfo = d.pop("zoneinfo")

        id = d.pop("id")

        created_date = isoparse(d.pop("created_date"))

        tags = cast(List[str], d.pop("tags"))

        open_tunnels = []
        _open_tunnels = d.pop("open_tunnels")
        for open_tunnels_item_data in _open_tunnels:
            open_tunnels_item = Tunnel.from_dict(open_tunnels_item_data)

            open_tunnels.append(open_tunnels_item)

        custom_attributes = AdminDeviceSchemaCustomAttributes.from_dict(d.pop("custom_attributes"))

        restricted_custom_attributes = AdminDeviceSchemaRestrictedCustomAttributes.from_dict(
            d.pop("restricted_custom_attributes")
        )

        iot_scopes = AdminDeviceSchemaIotScopes.from_dict(d.pop("iot_scopes"))

        is_active = d.pop("is_active")

        is_delete_protected = d.pop("is_delete_protected", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        product = d.pop("product", UNSET)

        site = d.pop("site", UNSET)

        serial_number = d.pop("serial_number", UNSET)

        mac_address = d.pop("mac_address", UNSET)

        is_org_admin = d.pop("is_org_admin", UNSET)

        picture = d.pop("picture", UNSET)

        picture_base64 = d.pop("picture_base64", UNSET)

        picture_content_type = d.pop("picture_content_type", UNSET)

        project_id = d.pop("project_id", UNSET)

        is_project_admin = d.pop("is_project_admin", UNSET)

        is_group_admin = d.pop("is_group_admin", UNSET)

        created_by = d.pop("created_by", UNSET)

        last_updated_by = d.pop("last_updated_by", UNSET)

        _last_updated_date = d.pop("last_updated_date", UNSET)
        last_updated_date: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = isoparse(_last_updated_date)

        _api_key_last_changed = d.pop("api_key_last_changed", UNSET)
        api_key_last_changed: Union[Unset, datetime.datetime]
        if isinstance(_api_key_last_changed, Unset):
            api_key_last_changed = UNSET
        else:
            api_key_last_changed = isoparse(_api_key_last_changed)

        _mqtt_credentials_last_changed = d.pop("mqtt_credentials_last_changed", UNSET)
        mqtt_credentials_last_changed: Union[Unset, datetime.datetime]
        if isinstance(_mqtt_credentials_last_changed, Unset):
            mqtt_credentials_last_changed = UNSET
        else:
            mqtt_credentials_last_changed = isoparse(_mqtt_credentials_last_changed)

        _last_seen = d.pop("last_seen", UNSET)
        last_seen: Union[Unset, datetime.datetime]
        if isinstance(_last_seen, Unset):
            last_seen = UNSET
        else:
            last_seen = isoparse(_last_seen)

        owner_id = d.pop("owner_id", UNSET)

        project_ids = cast(List[str], d.pop("project_ids", UNSET))

        group_ids = cast(List[str], d.pop("group_ids", UNSET))

        role_ids = cast(List[str], d.pop("role_ids", UNSET))

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

        admin_device_schema = cls(
            name=name,
            locale=locale,
            zoneinfo=zoneinfo,
            id=id,
            created_date=created_date,
            tags=tags,
            open_tunnels=open_tunnels,
            custom_attributes=custom_attributes,
            restricted_custom_attributes=restricted_custom_attributes,
            iot_scopes=iot_scopes,
            is_active=is_active,
            is_delete_protected=is_delete_protected,
            manufacturer=manufacturer,
            product=product,
            site=site,
            serial_number=serial_number,
            mac_address=mac_address,
            is_org_admin=is_org_admin,
            picture=picture,
            picture_base64=picture_base64,
            picture_content_type=picture_content_type,
            project_id=project_id,
            is_project_admin=is_project_admin,
            is_group_admin=is_group_admin,
            created_by=created_by,
            last_updated_by=last_updated_by,
            last_updated_date=last_updated_date,
            api_key_last_changed=api_key_last_changed,
            mqtt_credentials_last_changed=mqtt_credentials_last_changed,
            last_seen=last_seen,
            owner_id=owner_id,
            project_ids=project_ids,
            group_ids=group_ids,
            role_ids=role_ids,
            project_permissions=project_permissions,
            org_permissions=org_permissions,
        )

        admin_device_schema.additional_properties = d
        return admin_device_schema

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
