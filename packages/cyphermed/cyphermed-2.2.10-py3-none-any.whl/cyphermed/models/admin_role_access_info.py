from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.admin_role_access_schema import AdminRoleAccessSchema


T = TypeVar("T", bound="AdminRoleAccessInfo")


@_attrs_define
class AdminRoleAccessInfo:
    """Info on one specific role access

    Attributes:
        role_access (AdminRoleAccessSchema): Role access schema
    """

    role_access: "AdminRoleAccessSchema"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role_access = self.role_access.to_dict()

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
        from ..models.admin_role_access_schema import AdminRoleAccessSchema

        d = src_dict.copy()
        role_access = AdminRoleAccessSchema.from_dict(d.pop("role_access"))

        admin_role_access_info = cls(
            role_access=role_access,
        )

        admin_role_access_info.additional_properties = d
        return admin_role_access_info

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
