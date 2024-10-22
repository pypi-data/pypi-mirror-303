from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.widget_info_config import WidgetInfoConfig


T = TypeVar("T", bound="WidgetInfo")


@_attrs_define
class WidgetInfo:
    """Configuration for a single widget on the dashboard

    Attributes:
        order (int): Order in which to display the widget
        widget_type (str): Type of widget to display
        widget_title (str): Title of the widget
        config (WidgetInfoConfig): Settings for the widget
    """

    order: int
    widget_type: str
    widget_title: str
    config: "WidgetInfoConfig"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order = self.order

        widget_type = self.widget_type

        widget_title = self.widget_title

        config = self.config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order": order,
                "widget_type": widget_type,
                "widget_title": widget_title,
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.widget_info_config import WidgetInfoConfig

        d = src_dict.copy()
        order = d.pop("order")

        widget_type = d.pop("widget_type")

        widget_title = d.pop("widget_title")

        config = WidgetInfoConfig.from_dict(d.pop("config"))

        widget_info = cls(
            order=order,
            widget_type=widget_type,
            widget_title=widget_title,
            config=config,
        )

        widget_info.additional_properties = d
        return widget_info

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
