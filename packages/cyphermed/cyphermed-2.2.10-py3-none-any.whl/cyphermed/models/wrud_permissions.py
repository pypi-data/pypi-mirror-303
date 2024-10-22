from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="WRUDPermissions")


@_attrs_define
class WRUDPermissions:
    """Collection of permissions, only for write, read, delete

    Attributes:
        can_write (Union[Unset, bool]):  Default: False.
        can_read (Union[Unset, bool]):  Default: False.
        can_update (Union[Unset, bool]):  Default: False.
        can_delete (Union[Unset, bool]):  Default: False.
    """

    can_write: Union[Unset, bool] = False
    can_read: Union[Unset, bool] = False
    can_update: Union[Unset, bool] = False
    can_delete: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        can_write = self.can_write

        can_read = self.can_read

        can_update = self.can_update

        can_delete = self.can_delete

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_write is not UNSET:
            field_dict["can_write"] = can_write
        if can_read is not UNSET:
            field_dict["can_read"] = can_read
        if can_update is not UNSET:
            field_dict["can_update"] = can_update
        if can_delete is not UNSET:
            field_dict["can_delete"] = can_delete

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        can_write = d.pop("can_write", UNSET)

        can_read = d.pop("can_read", UNSET)

        can_update = d.pop("can_update", UNSET)

        can_delete = d.pop("can_delete", UNSET)

        wrud_permissions = cls(
            can_write=can_write,
            can_read=can_read,
            can_update=can_update,
            can_delete=can_delete,
        )

        wrud_permissions.additional_properties = d
        return wrud_permissions

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
