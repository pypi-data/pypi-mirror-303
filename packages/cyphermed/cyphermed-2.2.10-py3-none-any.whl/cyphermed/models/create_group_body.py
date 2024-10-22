from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="CreateGroupBody")


@_attrs_define
class CreateGroupBody:
    """Which Group fields to include in request bodies

    Attributes:
        name (str): Name of the group
        description (Union[Unset, str]): Description of the group
        is_delete_protected (Union[Unset, bool]): This must be set false before the group can be deleted
        tags (Union[Unset, List[str]]): List of tags on this group
        require_delete_permission_to_put_data (Union[Unset, bool]): (Admin only) If true, require delete permission to
            put data
        project_id (Union[Unset, str]): ID of the project this group belongs to, if any
        create_own_access (Union[Unset, bool]): If true, full access to the group is automatically created for the
            requester Default: True.
    """

    name: str
    description: Union[Unset, str] = UNSET
    is_delete_protected: Union[Unset, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    require_delete_permission_to_put_data: Union[Unset, bool] = UNSET
    project_id: Union[Unset, str] = UNSET
    create_own_access: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        is_delete_protected = self.is_delete_protected

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        require_delete_permission_to_put_data = self.require_delete_permission_to_put_data

        project_id = self.project_id

        create_own_access = self.create_own_access

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
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
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if create_own_access is not UNSET:
            field_dict["create_own_access"] = create_own_access

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description", UNSET)

        is_delete_protected = d.pop("is_delete_protected", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        require_delete_permission_to_put_data = d.pop(
            "require_delete_permission_to_put_data", UNSET
        )

        project_id = d.pop("project_id", UNSET)

        create_own_access = d.pop("create_own_access", UNSET)

        create_group_body = cls(
            name=name,
            description=description,
            is_delete_protected=is_delete_protected,
            tags=tags,
            require_delete_permission_to_put_data=require_delete_permission_to_put_data,
            project_id=project_id,
            create_own_access=create_own_access,
        )

        create_group_body.additional_properties = d
        return create_group_body

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
