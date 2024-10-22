from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.new_role_schema import NewRoleSchema


T = TypeVar("T", bound="NewRoleInfo")


@_attrs_define
class NewRoleInfo:
    """Info on one specific role

    Attributes:
        role (NewRoleSchema): Which Role fields to include in request bodies
    """

    role: "NewRoleSchema"
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
        from ..models.new_role_schema import NewRoleSchema

        d = src_dict.copy()
        role = NewRoleSchema.from_dict(d.pop("role"))

        new_role_info = cls(
            role=role,
        )

        new_role_info.additional_properties = d
        return new_role_info

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
