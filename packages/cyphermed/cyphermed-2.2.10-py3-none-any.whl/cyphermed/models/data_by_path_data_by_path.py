from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.data_info import DataInfo
    from ..models.data_schema import DataSchema


T = TypeVar("T", bound="DataByPathDataByPath")


@_attrs_define
class DataByPathDataByPath:
    """ """

    additional_properties: Dict[str, Union["DataInfo", "DataSchema", List["DataSchema"]]] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> Dict[str, Any]:
        from ..models.data_info import DataInfo

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, DataInfo):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, list):
                field_dict[prop_name] = []
                for additional_property_type_1_item_data in prop:
                    additional_property_type_1_item = additional_property_type_1_item_data.to_dict()
                    field_dict[prop_name].append(additional_property_type_1_item)

            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_info import DataInfo
        from ..models.data_schema import DataSchema

        d = src_dict.copy()
        data_by_path_data_by_path = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> Union["DataInfo", "DataSchema", List["DataSchema"]]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = DataInfo.from_dict(data)

                    return additional_property_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    additional_property_type_1 = []
                    _additional_property_type_1 = data
                    for additional_property_type_1_item_data in _additional_property_type_1:
                        additional_property_type_1_item = DataSchema.from_dict(
                            additional_property_type_1_item_data
                        )

                        additional_property_type_1.append(additional_property_type_1_item)

                    return additional_property_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                additional_property_type_2 = DataSchema.from_dict(data)

                return additional_property_type_2

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        data_by_path_data_by_path.additional_properties = additional_properties
        return data_by_path_data_by_path

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union["DataInfo", "DataSchema", List["DataSchema"]]:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: Union["DataInfo", "DataSchema", List["DataSchema"]]
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
