from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.data_info_last_evaluated_key import DataInfoLastEvaluatedKey


T = TypeVar("T", bound="DataInfo")


@_attrs_define
class DataInfo:
    """List of group data

    Attributes:
        paths (Union[Unset, List[str]]):
        object_count (Union[Unset, int]):
        last_evaluated_key (Union[Unset, DataInfoLastEvaluatedKey]):
    """

    paths: Union[Unset, List[str]] = UNSET
    object_count: Union[Unset, int] = UNSET
    last_evaluated_key: Union[Unset, "DataInfoLastEvaluatedKey"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        paths: Union[Unset, List[str]] = UNSET
        if not isinstance(self.paths, Unset):
            paths = self.paths

        object_count = self.object_count

        last_evaluated_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_evaluated_key, Unset):
            last_evaluated_key = self.last_evaluated_key.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if paths is not UNSET:
            field_dict["paths"] = paths
        if object_count is not UNSET:
            field_dict["object_count"] = object_count
        if last_evaluated_key is not UNSET:
            field_dict["last_evaluated_key"] = last_evaluated_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_info_last_evaluated_key import DataInfoLastEvaluatedKey

        d = src_dict.copy()
        paths = cast(List[str], d.pop("paths", UNSET))

        object_count = d.pop("object_count", UNSET)

        _last_evaluated_key = d.pop("last_evaluated_key", UNSET)
        last_evaluated_key: Union[Unset, DataInfoLastEvaluatedKey]
        if isinstance(_last_evaluated_key, Unset):
            last_evaluated_key = UNSET
        else:
            last_evaluated_key = DataInfoLastEvaluatedKey.from_dict(_last_evaluated_key)

        data_info = cls(
            paths=paths,
            object_count=object_count,
            last_evaluated_key=last_evaluated_key,
        )

        data_info.additional_properties = d
        return data_info

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
