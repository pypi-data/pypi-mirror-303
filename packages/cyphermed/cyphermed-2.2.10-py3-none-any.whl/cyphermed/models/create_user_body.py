from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.create_user_body_custom_attributes import (
        CreateUserBodyCustomAttributes,
    )
    from ..models.create_user_body_restricted_custom_attributes import (
        CreateUserBodyRestrictedCustomAttributes,
    )
    from ..models.org_access_permissions import OrgAccessPermissions
    from ..models.project_access_permissions import ProjectAccessPermissions


T = TypeVar("T", bound="CreateUserBody")


@_attrs_define
class CreateUserBody:
    """Request payload for POST /users

    Attributes:
        email (str): Email of the user
        is_active (Union[Unset, bool]): (Admin only) Whether this account is active
        is_delete_protected (Union[Unset, bool]): Whether this account is delete protected
        locale (Union[Unset, str]): Locale of the account
        zoneinfo (Union[Unset, str]): Timezone of the account
        picture (Union[Unset, str]): URL of the account's picture
        tags (Union[Unset, List[str]]): List of tags on this account
        project_id (Union[Unset, str]): ID of project to create them in (org admins only)
        project_permissions (Union[Unset, ProjectAccessPermissions]): Collection of permissions for project access
        org_permissions (Union[Unset, OrgAccessPermissions]): Collection of permissions for org access
        custom_attributes (Union[Unset, CreateUserBodyCustomAttributes]): Custom attributes for this user
        restricted_custom_attributes (Union[Unset, CreateUserBodyRestrictedCustomAttributes]): Custom attributes only
            admins can update
        username (Union[Unset, str]): Username of the user
        phone_number (Union[Unset, str]): Phone number of the user
        password (Union[Unset, str]): Password of the user
        temp_password (Union[Unset, str]): Temporary password
        nickname (Union[Unset, str]): Nickname of the user
        first_name (Union[Unset, str]): First (or given) name of the user
        middle_name (Union[Unset, str]): Middle name of the user
        last_name (Union[Unset, str]): Last (or family) name of the user
    """

    email: str
    is_active: Union[Unset, bool] = UNSET
    is_delete_protected: Union[Unset, bool] = UNSET
    locale: Union[Unset, str] = UNSET
    zoneinfo: Union[Unset, str] = UNSET
    picture: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    project_id: Union[Unset, str] = UNSET
    project_permissions: Union[Unset, "ProjectAccessPermissions"] = UNSET
    org_permissions: Union[Unset, "OrgAccessPermissions"] = UNSET
    custom_attributes: Union[Unset, "CreateUserBodyCustomAttributes"] = UNSET
    restricted_custom_attributes: Union[Unset, "CreateUserBodyRestrictedCustomAttributes"] = UNSET
    username: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    temp_password: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        is_active = self.is_active

        is_delete_protected = self.is_delete_protected

        locale = self.locale

        zoneinfo = self.zoneinfo

        picture = self.picture

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        project_id = self.project_id

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

        username = self.username

        phone_number = self.phone_number

        password = self.password

        temp_password = self.temp_password

        nickname = self.nickname

        first_name = self.first_name

        middle_name = self.middle_name

        last_name = self.last_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
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
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if project_permissions is not UNSET:
            field_dict["project_permissions"] = project_permissions
        if org_permissions is not UNSET:
            field_dict["org_permissions"] = org_permissions
        if custom_attributes is not UNSET:
            field_dict["custom_attributes"] = custom_attributes
        if restricted_custom_attributes is not UNSET:
            field_dict["restricted_custom_attributes"] = restricted_custom_attributes
        if username is not UNSET:
            field_dict["username"] = username
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if password is not UNSET:
            field_dict["password"] = password
        if temp_password is not UNSET:
            field_dict["temp_password"] = temp_password
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_user_body_custom_attributes import (
            CreateUserBodyCustomAttributes,
        )
        from ..models.create_user_body_restricted_custom_attributes import (
            CreateUserBodyRestrictedCustomAttributes,
        )
        from ..models.org_access_permissions import OrgAccessPermissions
        from ..models.project_access_permissions import ProjectAccessPermissions

        d = src_dict.copy()
        email = d.pop("email")

        is_active = d.pop("is_active", UNSET)

        is_delete_protected = d.pop("is_delete_protected", UNSET)

        locale = d.pop("locale", UNSET)

        zoneinfo = d.pop("zoneinfo", UNSET)

        picture = d.pop("picture", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        project_id = d.pop("project_id", UNSET)

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
        custom_attributes: Union[Unset, CreateUserBodyCustomAttributes]
        if isinstance(_custom_attributes, Unset):
            custom_attributes = UNSET
        else:
            custom_attributes = CreateUserBodyCustomAttributes.from_dict(_custom_attributes)

        _restricted_custom_attributes = d.pop("restricted_custom_attributes", UNSET)
        restricted_custom_attributes: Union[Unset, CreateUserBodyRestrictedCustomAttributes]
        if isinstance(_restricted_custom_attributes, Unset):
            restricted_custom_attributes = UNSET
        else:
            restricted_custom_attributes = CreateUserBodyRestrictedCustomAttributes.from_dict(
                _restricted_custom_attributes
            )

        username = d.pop("username", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        password = d.pop("password", UNSET)

        temp_password = d.pop("temp_password", UNSET)

        nickname = d.pop("nickname", UNSET)

        first_name = d.pop("first_name", UNSET)

        middle_name = d.pop("middle_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        create_user_body = cls(
            email=email,
            is_active=is_active,
            is_delete_protected=is_delete_protected,
            locale=locale,
            zoneinfo=zoneinfo,
            picture=picture,
            tags=tags,
            project_id=project_id,
            project_permissions=project_permissions,
            org_permissions=org_permissions,
            custom_attributes=custom_attributes,
            restricted_custom_attributes=restricted_custom_attributes,
            username=username,
            phone_number=phone_number,
            password=password,
            temp_password=temp_password,
            nickname=nickname,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
        )

        create_user_body.additional_properties = d
        return create_user_body

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
