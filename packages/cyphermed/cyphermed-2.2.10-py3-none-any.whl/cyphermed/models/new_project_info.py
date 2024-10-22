from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.new_project_schema import NewProjectSchema


T = TypeVar("T", bound="NewProjectInfo")


@_attrs_define
class NewProjectInfo:
    """Info on one specific project

    Attributes:
        project (NewProjectSchema): Which Project fields to include in response bodies
    """

    project: "NewProjectSchema"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project = self.project.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project": project,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.new_project_schema import NewProjectSchema

        d = src_dict.copy()
        project = NewProjectSchema.from_dict(d.pop("project"))

        new_project_info = cls(
            project=project,
        )

        new_project_info.additional_properties = d
        return new_project_info

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
