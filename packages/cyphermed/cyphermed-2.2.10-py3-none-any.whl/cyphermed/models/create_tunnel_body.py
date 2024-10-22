from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="CreateTunnelBody")


@_attrs_define
class CreateTunnelBody:
    """Create a new tunnel

    Attributes:
        services (List[str]): List of services to expose
        timeout (Union[Unset, int]): Tunnel timeout in minutes, default 1 hour, max 12 hours Default: 60.
        sendto_user_id (Union[Unset, str]): User who's email will receive tunnel info
    """

    services: List[str]
    timeout: Union[Unset, int] = 60
    sendto_user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        services = self.services

        timeout = self.timeout

        sendto_user_id = self.sendto_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "services": services,
            }
        )
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if sendto_user_id is not UNSET:
            field_dict["sendto_user_id"] = sendto_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        services = cast(List[str], d.pop("services"))

        timeout = d.pop("timeout", UNSET)

        sendto_user_id = d.pop("sendto_user_id", UNSET)

        create_tunnel_body = cls(
            services=services,
            timeout=timeout,
            sendto_user_id=sendto_user_id,
        )

        create_tunnel_body.additional_properties = d
        return create_tunnel_body

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
