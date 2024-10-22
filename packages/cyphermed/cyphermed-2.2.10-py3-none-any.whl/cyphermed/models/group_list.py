from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.group_schema import GroupSchema


T = TypeVar("T", bound="GroupList")


@_attrs_define
class GroupList:
    """List of groups

    Attributes:
        groups (Union[Unset, List['GroupSchema']]):
        page_count (Union[Unset, int]):
        object_count (Union[Unset, int]):
    """

    groups: Union[Unset, List["GroupSchema"]] = UNSET
    page_count: Union[Unset, int] = UNSET
    object_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        page_count = self.page_count

        object_count = self.object_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if object_count is not UNSET:
            field_dict["object_count"] = object_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.group_schema import GroupSchema

        d = src_dict.copy()
        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = GroupSchema.from_dict(groups_item_data)

            groups.append(groups_item)

        page_count = d.pop("page_count", UNSET)

        object_count = d.pop("object_count", UNSET)

        group_list = cls(
            groups=groups,
            page_count=page_count,
            object_count=object_count,
        )

        group_list.additional_properties = d
        return group_list

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
