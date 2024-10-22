from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.interface_images import InterfaceImages


T = TypeVar("T", bound="InterfaceConfig")


@_attrs_define
class InterfaceConfig:
    """Configuration for the user interface

    Attributes:
        images (Union[Unset, InterfaceImages]): Logos for the user interface
        primary_color (Union[Unset, str]): Primary color for the dashboard
        use_dark_mode (Union[Unset, bool]): Use dark mode for the dashboard
    """

    images: Union[Unset, "InterfaceImages"] = UNSET
    primary_color: Union[Unset, str] = UNSET
    use_dark_mode: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        primary_color = self.primary_color

        use_dark_mode = self.use_dark_mode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if images is not UNSET:
            field_dict["images"] = images
        if primary_color is not UNSET:
            field_dict["primary_color"] = primary_color
        if use_dark_mode is not UNSET:
            field_dict["use_dark_mode"] = use_dark_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.interface_images import InterfaceImages

        d = src_dict.copy()
        _images = d.pop("images", UNSET)
        images: Union[Unset, InterfaceImages]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = InterfaceImages.from_dict(_images)

        primary_color = d.pop("primary_color", UNSET)

        use_dark_mode = d.pop("use_dark_mode", UNSET)

        interface_config = cls(
            images=images,
            primary_color=primary_color,
            use_dark_mode=use_dark_mode,
        )

        interface_config.additional_properties = d
        return interface_config

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
