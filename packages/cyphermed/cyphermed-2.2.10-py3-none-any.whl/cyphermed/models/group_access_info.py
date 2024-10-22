from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.group_access_schema import GroupAccessSchema


T = TypeVar("T", bound="GroupAccessInfo")


@_attrs_define
class GroupAccessInfo:
    """Access for a group

    Attributes:
        group_access (GroupAccessSchema): Access for a group
    """

    group_access: "GroupAccessSchema"
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
        from ..models.group_access_schema import GroupAccessSchema

        d = src_dict.copy()
        group_access = GroupAccessSchema.from_dict(d.pop("group_access"))

        group_access_info = cls(
            group_access=group_access,
        )

        group_access_info.additional_properties = d
        return group_access_info

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
