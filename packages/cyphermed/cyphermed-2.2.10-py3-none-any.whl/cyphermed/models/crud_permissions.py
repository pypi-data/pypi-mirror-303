from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="CRUDPermissions")


@_attrs_define
class CRUDPermissions:
    """Collection of CRUD permissions

    Attributes:
        can_create (Union[Unset, bool]):  Default: False.
        can_read (Union[Unset, bool]):  Default: False.
        can_update (Union[Unset, bool]):  Default: False.
        can_delete (Union[Unset, bool]):  Default: False.
    """

    can_create: Union[Unset, bool] = False
    can_read: Union[Unset, bool] = False
    can_update: Union[Unset, bool] = False
    can_delete: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        can_create = self.can_create

        can_read = self.can_read

        can_update = self.can_update

        can_delete = self.can_delete

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_create is not UNSET:
            field_dict["can_create"] = can_create
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
        can_create = d.pop("can_create", UNSET)

        can_read = d.pop("can_read", UNSET)

        can_update = d.pop("can_update", UNSET)

        can_delete = d.pop("can_delete", UNSET)

        crud_permissions = cls(
            can_create=can_create,
            can_read=can_read,
            can_update=can_update,
            can_delete=can_delete,
        )

        crud_permissions.additional_properties = d
        return crud_permissions

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
