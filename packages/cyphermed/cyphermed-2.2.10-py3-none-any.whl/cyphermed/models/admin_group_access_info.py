from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.admin_group_access_schema import AdminGroupAccessSchema


T = TypeVar("T", bound="AdminGroupAccessInfo")


@_attrs_define
class AdminGroupAccessInfo:
    """Access for a group

    Attributes:
        group_access (AdminGroupAccessSchema): Access for a group plus admin-only fields
    """

    group_access: "AdminGroupAccessSchema"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_access = self.group_access.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group_access": group_access,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.admin_group_access_schema import AdminGroupAccessSchema

        d = src_dict.copy()
        group_access = AdminGroupAccessSchema.from_dict(d.pop("group_access"))

        admin_group_access_info = cls(
            group_access=group_access,
        )

        admin_group_access_info.additional_properties = d
        return admin_group_access_info

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
