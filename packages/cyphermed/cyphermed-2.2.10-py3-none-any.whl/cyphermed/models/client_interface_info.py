from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.interface_config import InterfaceConfig


T = TypeVar("T", bound="ClientInterfaceInfo")


@_attrs_define
class ClientInterfaceInfo:
    """Interface configuration for a given client ID

    Attributes:
        allowed_login_fields (List[str]): List of allowed login fields
        client_id (str): Client ID
        ui_config (InterfaceConfig): Configuration for the user interface
    """

    allowed_login_fields: List[str]
    client_id: str
    ui_config: "InterfaceConfig"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allowed_login_fields = self.allowed_login_fields

        client_id = self.client_id

        ui_config = self.ui_config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowed_login_fields": allowed_login_fields,
                "client_id": client_id,
                "ui_config": ui_config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.interface_config import InterfaceConfig

        d = src_dict.copy()
        allowed_login_fields = cast(List[str], d.pop("allowed_login_fields"))

        client_id = d.pop("client_id")

        ui_config = InterfaceConfig.from_dict(d.pop("ui_config"))

        client_interface_info = cls(
            allowed_login_fields=allowed_login_fields,
            client_id=client_id,
            ui_config=ui_config,
        )

        client_interface_info.additional_properties = d
        return client_interface_info

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
