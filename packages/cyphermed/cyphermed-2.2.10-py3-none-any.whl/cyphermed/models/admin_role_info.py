from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.admin_role_schema import AdminRoleSchema


T = TypeVar("T", bound="AdminRoleInfo")


@_attrs_define
class AdminRoleInfo:
    """Info on one specific role

    Attributes:
        role (AdminRoleSchema): Which Role fields to include in response bodies for admins
    """

    role: "AdminRoleSchema"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role = self.role.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.admin_role_schema import AdminRoleSchema

        d = src_dict.copy()
        role = AdminRoleSchema.from_dict(d.pop("role"))

        admin_role_info = cls(
            role=role,
        )

        admin_role_info.additional_properties = d
        return admin_role_info

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
