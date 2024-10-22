from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


T = TypeVar("T", bound="NewTunnelSchema")


@_attrs_define
class NewTunnelSchema:
    """Info on one specific tunnel

    Attributes:
        uuid (str):
        timeout (int):
        client_access_token (str):
    """

    uuid: str
    timeout: int
    client_access_token: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid

        timeout = self.timeout

        client_access_token = self.client_access_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "timeout": timeout,
                "client_access_token": client_access_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid")

        timeout = d.pop("timeout")

        client_access_token = d.pop("client_access_token")

        new_tunnel_schema = cls(
            uuid=uuid,
            timeout=timeout,
            client_access_token=client_access_token,
        )

        new_tunnel_schema.additional_properties = d
        return new_tunnel_schema

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
