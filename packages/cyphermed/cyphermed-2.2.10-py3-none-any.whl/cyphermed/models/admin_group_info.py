from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.admin_group_schema import AdminGroupSchema


T = TypeVar("T", bound="AdminGroupInfo")


@_attrs_define
class AdminGroupInfo:
    """Info on one specific group

    Attributes:
        group (AdminGroupSchema): Group schema plus admin-only fields
    """

    group: "AdminGroupSchema"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group = self.group.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group": group,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.admin_group_schema import AdminGroupSchema

        d = src_dict.copy()
        group = AdminGroupSchema.from_dict(d.pop("group"))

        admin_group_info = cls(
            group=group,
        )

        admin_group_info.additional_properties = d
        return admin_group_info

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
