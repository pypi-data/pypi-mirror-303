from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="PatchGroupBody")


@_attrs_define
class PatchGroupBody:
    """Which Group fields to include in PATCH request bodies

    Attributes:
        description (Union[Unset, str]): Description of the group
        is_delete_protected (Union[Unset, bool]): This must be set false before the group can be deleted
        tags (Union[Unset, List[str]]): List of tags on this group
        require_delete_permission_to_put_data (Union[Unset, bool]): (Admin only) If true, require delete permission to
            put data
        name (Union[Unset, str]): Name of the group
        is_active (Union[Unset, bool]): Whether this group is active
    """

    description: Union[Unset, str] = UNSET
    is_delete_protected: Union[Unset, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    require_delete_permission_to_put_data: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        is_delete_protected = self.is_delete_protected

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        require_delete_permission_to_put_data = self.require_delete_permission_to_put_data

        name = self.name

        is_active = self.is_active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if is_delete_protected is not UNSET:
            field_dict["is_delete_protected"] = is_delete_protected
        if tags is not UNSET:
            field_dict["tags"] = tags
        if require_delete_permission_to_put_data is not UNSET:
            field_dict["require_delete_permission_to_put_data"] = (
                require_delete_permission_to_put_data
            )
        if name is not UNSET:
            field_dict["name"] = name
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        is_delete_protected = d.pop("is_delete_protected", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        require_delete_permission_to_put_data = d.pop(
            "require_delete_permission_to_put_data", UNSET
        )

        name = d.pop("name", UNSET)

        is_active = d.pop("is_active", UNSET)

        patch_group_body = cls(
            description=description,
            is_delete_protected=is_delete_protected,
            tags=tags,
            require_delete_permission_to_put_data=require_delete_permission_to_put_data,
            name=name,
            is_active=is_active,
        )

        patch_group_body.additional_properties = d
        return patch_group_body

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
