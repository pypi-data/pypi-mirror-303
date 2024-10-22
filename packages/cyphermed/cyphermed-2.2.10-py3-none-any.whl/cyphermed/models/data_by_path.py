from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.data_by_path_data_by_path import DataByPathDataByPath


T = TypeVar("T", bound="DataByPath")


@_attrs_define
class DataByPath:
    """List of group data

    Attributes:
        data_by_path (DataByPathDataByPath):
    """

    data_by_path: "DataByPathDataByPath"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_by_path = self.data_by_path.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data_by_path": data_by_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_by_path_data_by_path import DataByPathDataByPath

        d = src_dict.copy()
        data_by_path = DataByPathDataByPath.from_dict(d.pop("data_by_path"))

        data_by_path = cls(
            data_by_path=data_by_path,
        )

        data_by_path.additional_properties = d
        return data_by_path

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
