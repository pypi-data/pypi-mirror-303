from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.admin_account_group_access_schema import AdminAccountGroupAccessSchema


T = TypeVar("T", bound="AdminAccountGroupAccessList")


@_attrs_define
class AdminAccountGroupAccessList:
    """List of group access granted to current account, including admin-only fields

    Attributes:
        group_access (Union[Unset, List['AdminAccountGroupAccessSchema']]):
        page_count (Union[Unset, int]):
        object_count (Union[Unset, int]):
    """

    group_access: Union[Unset, List["AdminAccountGroupAccessSchema"]] = UNSET
    page_count: Union[Unset, int] = UNSET
    object_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_access: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.group_access, Unset):
            group_access = []
            for group_access_item_data in self.group_access:
                group_access_item = group_access_item_data.to_dict()
                group_access.append(group_access_item)

        page_count = self.page_count

        object_count = self.object_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_access is not UNSET:
            field_dict["group_access"] = group_access
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if object_count is not UNSET:
            field_dict["object_count"] = object_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.admin_account_group_access_schema import (
            AdminAccountGroupAccessSchema,
        )

        d = src_dict.copy()
        group_access = []
        _group_access = d.pop("group_access", UNSET)
        for group_access_item_data in _group_access or []:
            group_access_item = AdminAccountGroupAccessSchema.from_dict(group_access_item_data)

            group_access.append(group_access_item)

        page_count = d.pop("page_count", UNSET)

        object_count = d.pop("object_count", UNSET)

        admin_account_group_access_list = cls(
            group_access=group_access,
            page_count=page_count,
            object_count=object_count,
        )

        admin_account_group_access_list.additional_properties = d
        return admin_account_group_access_list

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
