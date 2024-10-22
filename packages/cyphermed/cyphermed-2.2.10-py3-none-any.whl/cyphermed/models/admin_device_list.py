from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.admin_device_schema import AdminDeviceSchema


T = TypeVar("T", bound="AdminDeviceList")


@_attrs_define
class AdminDeviceList:
    """
    Attributes:
        devices (Union[Unset, List['AdminDeviceSchema']]):
        page_count (Union[Unset, int]):
        object_count (Union[Unset, int]):
    """

    devices: Union[Unset, List["AdminDeviceSchema"]] = UNSET
    page_count: Union[Unset, int] = UNSET
    object_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        devices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        page_count = self.page_count

        object_count = self.object_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if devices is not UNSET:
            field_dict["devices"] = devices
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if object_count is not UNSET:
            field_dict["object_count"] = object_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.admin_device_schema import AdminDeviceSchema

        d = src_dict.copy()
        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in _devices or []:
            devices_item = AdminDeviceSchema.from_dict(devices_item_data)

            devices.append(devices_item)

        page_count = d.pop("page_count", UNSET)

        object_count = d.pop("object_count", UNSET)

        admin_device_list = cls(
            devices=devices,
            page_count=page_count,
            object_count=object_count,
        )

        admin_device_list.additional_properties = d
        return admin_device_list

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
