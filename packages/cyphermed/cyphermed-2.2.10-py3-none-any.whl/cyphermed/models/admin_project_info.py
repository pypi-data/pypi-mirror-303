from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.admin_project_schema import AdminProjectSchema


T = TypeVar("T", bound="AdminProjectInfo")


@_attrs_define
class AdminProjectInfo:
    """Info on one specific project plus admin-only fields

    Attributes:
        project (AdminProjectSchema): Project schema plus admin-only fields
    """

    project: "AdminProjectSchema"
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
        from ..models.admin_project_schema import AdminProjectSchema

        d = src_dict.copy()
        project = AdminProjectSchema.from_dict(d.pop("project"))

        admin_project_info = cls(
            project=project,
        )

        admin_project_info.additional_properties = d
        return admin_project_info

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
