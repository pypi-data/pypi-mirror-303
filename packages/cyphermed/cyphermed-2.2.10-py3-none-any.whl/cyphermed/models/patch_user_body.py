from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.org_access_permissions import OrgAccessPermissions
    from ..models.patch_user_body_custom_attributes import PatchUserBodyCustomAttributes
    from ..models.patch_user_body_restricted_custom_attributes import (
        PatchUserBodyRestrictedCustomAttributes,
    )
    from ..models.project_access_permissions import ProjectAccessPermissions


T = TypeVar("T", bound="PatchUserBody")


@_attrs_define
class PatchUserBody:
    """Patch user body

    Attributes:
        username (Union[Unset, str]): Username of the user
        email (Union[Unset, str]): Email of the user
        phone_number (Union[Unset, str]): Phone number of the user
        is_delete_protected (Union[Unset, bool]): Whether this user is delete protected
        is_active (Union[Unset, bool]): Whether this user is active
        tags (Union[Unset, List[str]]): Tags for this user
        locale (Union[Unset, str]): Locale of the user
        zoneinfo (Union[Unset, str]): Zoneinfo of the user
        picture (Union[Unset, str]): URL of the user's picture
        nickname (Union[Unset, str]): Nickname of the user
        first_name (Union[Unset, str]): First (or given) name of the user
        middle_name (Union[Unset, str]): Middle name of the user
        last_name (Union[Unset, str]): Last (or family) name of the user
        project_permissions (Union[Unset, ProjectAccessPermissions]): Collection of permissions for project access
        org_permissions (Union[Unset, OrgAccessPermissions]): Collection of permissions for org access
        custom_attributes (Union[Unset, PatchUserBodyCustomAttributes]): Custom attributes for this user
        restricted_custom_attributes (Union[Unset, PatchUserBodyRestrictedCustomAttributes]): Custom attributes only
            admins can update
    """

    username: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    is_delete_protected: Union[Unset, bool] = UNSET
    is_active: Union[Unset, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    locale: Union[Unset, str] = UNSET
    zoneinfo: Union[Unset, str] = UNSET
    picture: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    project_permissions: Union[Unset, "ProjectAccessPermissions"] = UNSET
    org_permissions: Union[Unset, "OrgAccessPermissions"] = UNSET
    custom_attributes: Union[Unset, "PatchUserBodyCustomAttributes"] = UNSET
    restricted_custom_attributes: Union[Unset, "PatchUserBodyRestrictedCustomAttributes"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username

        email = self.email

        phone_number = self.phone_number

        is_delete_protected = self.is_delete_protected

        is_active = self.is_active

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        locale = self.locale

        zoneinfo = self.zoneinfo

        picture = self.picture

        nickname = self.nickname

        first_name = self.first_name

        middle_name = self.middle_name

        last_name = self.last_name

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if is_delete_protected is not UNSET:
            field_dict["is_delete_protected"] = is_delete_protected
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if tags is not UNSET:
            field_dict["tags"] = tags
        if locale is not UNSET:
            field_dict["locale"] = locale
        if zoneinfo is not UNSET:
            field_dict["zoneinfo"] = zoneinfo
        if picture is not UNSET:
            field_dict["picture"] = picture
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if project_permissions is not UNSET:
            field_dict["project_permissions"] = project_permissions
        if org_permissions is not UNSET:
            field_dict["org_permissions"] = org_permissions
        if custom_attributes is not UNSET:
            field_dict["custom_attributes"] = custom_attributes
        if restricted_custom_attributes is not UNSET:
            field_dict["restricted_custom_attributes"] = restricted_custom_attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.org_access_permissions import OrgAccessPermissions
        from ..models.patch_user_body_custom_attributes import (
            PatchUserBodyCustomAttributes,
        )
        from ..models.patch_user_body_restricted_custom_attributes import (
            PatchUserBodyRestrictedCustomAttributes,
        )
        from ..models.project_access_permissions import ProjectAccessPermissions

        d = src_dict.copy()
        username = d.pop("username", UNSET)

        email = d.pop("email", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        is_delete_protected = d.pop("is_delete_protected", UNSET)

        is_active = d.pop("is_active", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        locale = d.pop("locale", UNSET)

        zoneinfo = d.pop("zoneinfo", UNSET)

        picture = d.pop("picture", UNSET)

        nickname = d.pop("nickname", UNSET)

        first_name = d.pop("first_name", UNSET)

        middle_name = d.pop("middle_name", UNSET)

        last_name = d.pop("last_name", UNSET)

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
        custom_attributes: Union[Unset, PatchUserBodyCustomAttributes]
        if isinstance(_custom_attributes, Unset):
            custom_attributes = UNSET
        else:
            custom_attributes = PatchUserBodyCustomAttributes.from_dict(_custom_attributes)

        _restricted_custom_attributes = d.pop("restricted_custom_attributes", UNSET)
        restricted_custom_attributes: Union[Unset, PatchUserBodyRestrictedCustomAttributes]
        if isinstance(_restricted_custom_attributes, Unset):
            restricted_custom_attributes = UNSET
        else:
            restricted_custom_attributes = PatchUserBodyRestrictedCustomAttributes.from_dict(
                _restricted_custom_attributes
            )

        patch_user_body = cls(
            username=username,
            email=email,
            phone_number=phone_number,
            is_delete_protected=is_delete_protected,
            is_active=is_active,
            tags=tags,
            locale=locale,
            zoneinfo=zoneinfo,
            picture=picture,
            nickname=nickname,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            project_permissions=project_permissions,
            org_permissions=org_permissions,
            custom_attributes=custom_attributes,
            restricted_custom_attributes=restricted_custom_attributes,
        )

        patch_user_body.additional_properties = d
        return patch_user_body

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
