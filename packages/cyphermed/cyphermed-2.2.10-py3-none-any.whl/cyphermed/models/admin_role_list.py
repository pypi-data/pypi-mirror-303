from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.admin_role_schema import AdminRoleSchema


T = TypeVar("T", bound="AdminRoleList")


@_attrs_define
class AdminRoleList:
    """List of roles

    Attributes:
        roles (Union[Unset, List['AdminRoleSchema']]):
        page_count (Union[Unset, int]):
        object_count (Union[Unset, int]):
    """

    roles: Union[Unset, List["AdminRoleSchema"]] = UNSET
    page_count: Union[Unset, int] = UNSET
    object_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        page_count = self.page_count

        object_count = self.object_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if roles is not UNSET:
            field_dict["roles"] = roles
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if object_count is not UNSET:
            field_dict["object_count"] = object_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.admin_role_schema import AdminRoleSchema

        d = src_dict.copy()
        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = AdminRoleSchema.from_dict(roles_item_data)

            roles.append(roles_item)

        page_count = d.pop("page_count", UNSET)

        object_count = d.pop("object_count", UNSET)

        admin_role_list = cls(
            roles=roles,
            page_count=page_count,
            object_count=object_count,
        )

        admin_role_list.additional_properties = d
        return admin_role_list

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
