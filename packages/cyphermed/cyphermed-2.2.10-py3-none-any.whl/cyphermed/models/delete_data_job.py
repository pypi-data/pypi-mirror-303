from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="DeleteDataJob")


@_attrs_define
class DeleteDataJob:
    """Represents a single DELETE in a bulk request

    Attributes:
        paths (List[str]): Paths to delete
        cascade (Union[Unset, bool]): Whether to delete all child paths
    """

    paths: List[str]
    cascade: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        paths = self.paths

        cascade = self.cascade

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paths": paths,
            }
        )
        if cascade is not UNSET:
            field_dict["cascade"] = cascade

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        paths = cast(List[str], d.pop("paths"))

        cascade = d.pop("cascade", UNSET)

        delete_data_job = cls(
            paths=paths,
            cascade=cascade,
        )

        delete_data_job.additional_properties = d
        return delete_data_job

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
