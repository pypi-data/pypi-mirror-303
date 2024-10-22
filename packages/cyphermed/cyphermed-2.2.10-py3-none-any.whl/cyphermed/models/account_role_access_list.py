from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.role_access_schema import RoleAccessSchema


T = TypeVar("T", bound="AccountRoleAccessList")


@_attrs_define
class AccountRoleAccessList:
    """List of role access granted to current account

    Attributes:
        role_access (List['RoleAccessSchema']):
    """

    role_access: List["RoleAccessSchema"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role_access = []
        for role_access_item_data in self.role_access:
            role_access_item = role_access_item_data.to_dict()

            role_access.append(role_access_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role_access": role_access,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.role_access_schema import RoleAccessSchema

        d = src_dict.copy()
        role_access = []
        _role_access = d.pop("role_access")
        for role_access_item_data in _role_access:
            role_access_item = RoleAccessSchema.from_dict(role_access_item_data)

            role_access.append(role_access_item)

        account_role_access_list = cls(
            role_access=role_access,
        )

        account_role_access_list.additional_properties = d
        return account_role_access_list

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
