from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.tunnel import Tunnel


T = TypeVar("T", bound="TunnelInfo")


@_attrs_define
class TunnelInfo:
    """Info on one specific tunnel

    Attributes:
        tunnel (Tunnel):
    """

    tunnel: "Tunnel"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tunnel = self.tunnel.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tunnel": tunnel,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tunnel import Tunnel

        d = src_dict.copy()
        tunnel = Tunnel.from_dict(d.pop("tunnel"))

        tunnel_info = cls(
            tunnel=tunnel,
        )

        tunnel_info.additional_properties = d
        return tunnel_info

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
