from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.org_access_permissions import OrgAccessPermissions
    from ..models.patch_device_body_custom_attributes import (
        PatchDeviceBodyCustomAttributes,
    )
    from ..models.patch_device_body_iot_scopes import PatchDeviceBodyIotScopes
    from ..models.patch_device_body_restricted_custom_attributes import (
        PatchDeviceBodyRestrictedCustomAttributes,
    )
    from ..models.project_access_permissions import ProjectAccessPermissions


T = TypeVar("T", bound="PatchDeviceBody")


@_attrs_define
class PatchDeviceBody:
    """Update a device

    Attributes:
        owner_id (Union[Unset, str]): ID of the device owner
        name (Union[Unset, str]): Name of the device
        manufacturer (Union[Unset, str]): Device manufacturer
        product (Union[Unset, str]): Product name
        site (Union[Unset, str]): Location of this device
        serial_number (Union[Unset, str]): Device serial number
        mac_address (Union[Unset, str]): MAC address of this device
        is_active (Union[Unset, bool]): (Admin only) Whether this device is active
        is_delete_protected (Union[Unset, bool]): Whether this device is delete protected
        locale (Union[Unset, str]): Locale of the device
        zoneinfo (Union[Unset, str]): Timezone of the device
        picture (Union[Unset, str]): URL of the device's picture
        tags (Union[Unset, List[str]]): List of tags on this account
        project_permissions (Union[Unset, ProjectAccessPermissions]): Collection of permissions for project access
        org_permissions (Union[Unset, OrgAccessPermissions]): Collection of permissions for org access
        custom_attributes (Union[Unset, PatchDeviceBodyCustomAttributes]): Custom attributes for this user
        restricted_custom_attributes (Union[Unset, PatchDeviceBodyRestrictedCustomAttributes]): Custom attributes only
            admins can update
        iot_scopes (Union[Unset, PatchDeviceBodyIotScopes]): PubSub permissions per IoT scope for this device
    """

    owner_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    product: Union[Unset, str] = UNSET
    site: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    mac_address: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_delete_protected: Union[Unset, bool] = UNSET
    locale: Union[Unset, str] = UNSET
    zoneinfo: Union[Unset, str] = UNSET
    picture: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    project_permissions: Union[Unset, "ProjectAccessPermissions"] = UNSET
    org_permissions: Union[Unset, "OrgAccessPermissions"] = UNSET
    custom_attributes: Union[Unset, "PatchDeviceBodyCustomAttributes"] = UNSET
    restricted_custom_attributes: Union[Unset, "PatchDeviceBodyRestrictedCustomAttributes"] = UNSET
    iot_scopes: Union[Unset, "PatchDeviceBodyIotScopes"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        owner_id = self.owner_id

        name = self.name

        manufacturer = self.manufacturer

        product = self.product

        site = self.site

        serial_number = self.serial_number

        mac_address = self.mac_address

        is_active = self.is_active

        is_delete_protected = self.is_delete_protected

        locale = self.locale

        zoneinfo = self.zoneinfo

        picture = self.picture

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        project_permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project_permissions, Unset):
            project_permissions = self.project_permissions.to_dict()

        org_permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.org_permissions, Unset):
            org_permissions = self.org_permissions.to_dict()

        custom_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_attributes, Unset):
            custom_attributes = self.custom_attributes.to_dict()

        restricted_custom_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.restricted_custom_attributes, Unset):
            restricted_custom_attributes = self.restricted_custom_attributes.to_dict()

        iot_scopes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.iot_scopes, Unset):
            iot_scopes = self.iot_scopes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if name is not UNSET:
            field_dict["name"] = name
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
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_delete_protected is not UNSET:
            field_dict["is_delete_protected"] = is_delete_protected
        if locale is not UNSET:
            field_dict["locale"] = locale
        if zoneinfo is not UNSET:
            field_dict["zoneinfo"] = zoneinfo
        if picture is not UNSET:
            field_dict["picture"] = picture
        if tags is not UNSET:
            field_dict["tags"] = tags
        if project_permissions is not UNSET:
            field_dict["project_permissions"] = project_permissions
        if org_permissions is not UNSET:
            field_dict["org_permissions"] = org_permissions
        if custom_attributes is not UNSET:
            field_dict["custom_attributes"] = custom_attributes
        if restricted_custom_attributes is not UNSET:
            field_dict["restricted_custom_attributes"] = restricted_custom_attributes
        if iot_scopes is not UNSET:
            field_dict["iot_scopes"] = iot_scopes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.org_access_permissions import OrgAccessPermissions
        from ..models.patch_device_body_custom_attributes import (
            PatchDeviceBodyCustomAttributes,
        )
        from ..models.patch_device_body_iot_scopes import PatchDeviceBodyIotScopes
        from ..models.patch_device_body_restricted_custom_attributes import (
            PatchDeviceBodyRestrictedCustomAttributes,
        )
        from ..models.project_access_permissions import ProjectAccessPermissions

        d = src_dict.copy()
        owner_id = d.pop("owner_id", UNSET)

        name = d.pop("name", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        product = d.pop("product", UNSET)

        site = d.pop("site", UNSET)

        serial_number = d.pop("serial_number", UNSET)

        mac_address = d.pop("mac_address", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_delete_protected = d.pop("is_delete_protected", UNSET)

        locale = d.pop("locale", UNSET)

        zoneinfo = d.pop("zoneinfo", UNSET)

        picture = d.pop("picture", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

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

        _custom_attributes = d.pop("custom_attributes", UNSET)
        custom_attributes: Union[Unset, PatchDeviceBodyCustomAttributes]
        if isinstance(_custom_attributes, Unset):
            custom_attributes = UNSET
        else:
            custom_attributes = PatchDeviceBodyCustomAttributes.from_dict(_custom_attributes)

        _restricted_custom_attributes = d.pop("restricted_custom_attributes", UNSET)
        restricted_custom_attributes: Union[Unset, PatchDeviceBodyRestrictedCustomAttributes]
        if isinstance(_restricted_custom_attributes, Unset):
            restricted_custom_attributes = UNSET
        else:
            restricted_custom_attributes = PatchDeviceBodyRestrictedCustomAttributes.from_dict(
                _restricted_custom_attributes
            )

        _iot_scopes = d.pop("iot_scopes", UNSET)
        iot_scopes: Union[Unset, PatchDeviceBodyIotScopes]
        if isinstance(_iot_scopes, Unset):
            iot_scopes = UNSET
        else:
            iot_scopes = PatchDeviceBodyIotScopes.from_dict(_iot_scopes)

        patch_device_body = cls(
            owner_id=owner_id,
            name=name,
            manufacturer=manufacturer,
            product=product,
            site=site,
            serial_number=serial_number,
            mac_address=mac_address,
            is_active=is_active,
            is_delete_protected=is_delete_protected,
            locale=locale,
            zoneinfo=zoneinfo,
            picture=picture,
            tags=tags,
            project_permissions=project_permissions,
            org_permissions=org_permissions,
            custom_attributes=custom_attributes,
            restricted_custom_attributes=restricted_custom_attributes,
            iot_scopes=iot_scopes,
        )

        patch_device_body.additional_properties = d
        return patch_device_body

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
