from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="WRDPermissions")


@_attrs_define
class WRDPermissions:
    """Collection of permissions, only for write, read, delete

    Attributes:
        can_write (Union[Unset, bool]):  Default: False.
        can_read (Union[Unset, bool]):  Default: False.
        can_delete (Union[Unset, bool]):  Default: False.
    """

    can_write: Union[Unset, bool] = False
    can_read: Union[Unset, bool] = False
    can_delete: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        can_write = self.can_write

        can_read = self.can_read

        can_delete = self.can_delete

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_write is not UNSET:
            field_dict["can_write"] = can_write
        if can_read is not UNSET:
            field_dict["can_read"] = can_read
        if can_delete is not UNSET:
            field_dict["can_delete"] = can_delete

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        can_write = d.pop("can_write", UNSET)

        can_read = d.pop("can_read", UNSET)

        can_delete = d.pop("can_delete", UNSET)

        wrd_permissions = cls(
            can_write=can_write,
            can_read=can_read,
            can_delete=can_delete,
        )

        wrd_permissions.additional_properties = d
        return wrd_permissions

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
