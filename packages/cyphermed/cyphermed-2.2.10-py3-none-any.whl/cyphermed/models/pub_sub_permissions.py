from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="PubSubPermissions")


@_attrs_define
class PubSubPermissions:
    """Publish/subscribe permissions for a given scope

    Attributes:
        can_publish (Union[Unset, bool]):  Default: False.
        can_subscribe (Union[Unset, bool]):  Default: False.
    """

    can_publish: Union[Unset, bool] = False
    can_subscribe: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        can_publish = self.can_publish

        can_subscribe = self.can_subscribe

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_publish is not UNSET:
            field_dict["can_publish"] = can_publish
        if can_subscribe is not UNSET:
            field_dict["can_subscribe"] = can_subscribe

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        can_publish = d.pop("can_publish", UNSET)

        can_subscribe = d.pop("can_subscribe", UNSET)

        pub_sub_permissions = cls(
            can_publish=can_publish,
            can_subscribe=can_subscribe,
        )

        pub_sub_permissions.additional_properties = d
        return pub_sub_permissions

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
