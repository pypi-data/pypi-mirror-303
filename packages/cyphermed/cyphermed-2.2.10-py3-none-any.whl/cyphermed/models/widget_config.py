from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


T = TypeVar("T", bound="WidgetConfig")


@_attrs_define
class WidgetConfig:
    """Settings for a single widget on the dashboard

    Attributes:
        plot_type (str): Type of plot
        group_id (str): Group ID
        data_path (str): Path to the data (or parent path)
        use_latest_child (bool): Use latest child data under provided path
    """

    plot_type: str
    group_id: str
    data_path: str
    use_latest_child: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        plot_type = self.plot_type

        group_id = self.group_id

        data_path = self.data_path

        use_latest_child = self.use_latest_child

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plot_type": plot_type,
                "group_id": group_id,
                "data_path": data_path,
                "use_latest_child": use_latest_child,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        plot_type = d.pop("plot_type")

        group_id = d.pop("group_id")

        data_path = d.pop("data_path")

        use_latest_child = d.pop("use_latest_child")

        widget_config = cls(
            plot_type=plot_type,
            group_id=group_id,
            data_path=data_path,
            use_latest_child=use_latest_child,
        )

        widget_config.additional_properties = d
        return widget_config

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
