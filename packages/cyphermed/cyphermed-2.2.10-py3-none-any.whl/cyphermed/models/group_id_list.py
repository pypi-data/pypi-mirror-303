from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="GroupIdList")


@_attrs_define
class GroupIdList:
    """List of group IDs

    Attributes:
        group_ids (Union[Unset, List[str]]):
        page_count (Union[Unset, int]):
        object_count (Union[Unset, int]):
    """

    group_ids: Union[Unset, List[str]] = UNSET
    page_count: Union[Unset, int] = UNSET
    object_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        page_count = self.page_count

        object_count = self.object_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if object_count is not UNSET:
            field_dict["object_count"] = object_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_ids = cast(List[str], d.pop("group_ids", UNSET))

        page_count = d.pop("page_count", UNSET)

        object_count = d.pop("object_count", UNSET)

        group_id_list = cls(
            group_ids=group_ids,
            page_count=page_count,
            object_count=object_count,
        )

        group_id_list.additional_properties = d
        return group_id_list

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
