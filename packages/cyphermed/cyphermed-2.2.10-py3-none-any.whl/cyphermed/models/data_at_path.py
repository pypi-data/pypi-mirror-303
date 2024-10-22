from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.data_at_path_last_evaluated_key import DataAtPathLastEvaluatedKey
    from ..models.data_schema import DataSchema


T = TypeVar("T", bound="DataAtPath")


@_attrs_define
class DataAtPath:
    """List of group data

    Attributes:
        paths (Union[Unset, List[str]]):
        object_count (Union[Unset, int]):
        last_evaluated_key (Union[Unset, DataAtPathLastEvaluatedKey]):
        data (Union['DataSchema', List['DataSchema'], Unset]):
    """

    paths: Union[Unset, List[str]] = UNSET
    object_count: Union[Unset, int] = UNSET
    last_evaluated_key: Union[Unset, "DataAtPathLastEvaluatedKey"] = UNSET
    data: Union["DataSchema", List["DataSchema"], Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        paths: Union[Unset, List[str]] = UNSET
        if not isinstance(self.paths, Unset):
            paths = self.paths

        object_count = self.object_count

        last_evaluated_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_evaluated_key, Unset):
            last_evaluated_key = self.last_evaluated_key.to_dict()

        data: Union[Dict[str, Any], List[Dict[str, Any]], Unset]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)

        else:
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if paths is not UNSET:
            field_dict["paths"] = paths
        if object_count is not UNSET:
            field_dict["object_count"] = object_count
        if last_evaluated_key is not UNSET:
            field_dict["last_evaluated_key"] = last_evaluated_key
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_at_path_last_evaluated_key import DataAtPathLastEvaluatedKey
        from ..models.data_schema import DataSchema

        d = src_dict.copy()
        paths = cast(List[str], d.pop("paths", UNSET))

        object_count = d.pop("object_count", UNSET)

        _last_evaluated_key = d.pop("last_evaluated_key", UNSET)
        last_evaluated_key: Union[Unset, DataAtPathLastEvaluatedKey]
        if isinstance(_last_evaluated_key, Unset):
            last_evaluated_key = UNSET
        else:
            last_evaluated_key = DataAtPathLastEvaluatedKey.from_dict(_last_evaluated_key)

        def _parse_data(data: object) -> Union["DataSchema", List["DataSchema"], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = DataSchema.from_dict(data_type_0_item_data)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_1 = DataSchema.from_dict(data)

            return data_type_1

        data = _parse_data(d.pop("data", UNSET))

        data_at_path = cls(
            paths=paths,
            object_count=object_count,
            last_evaluated_key=last_evaluated_key,
            data=data,
        )

        data_at_path.additional_properties = d
        return data_at_path

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
