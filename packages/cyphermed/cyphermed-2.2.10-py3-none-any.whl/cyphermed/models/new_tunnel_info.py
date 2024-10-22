from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.new_tunnel_schema import NewTunnelSchema


T = TypeVar("T", bound="NewTunnelInfo")


@_attrs_define
class NewTunnelInfo:
    """Info on one specific tunnel

    Attributes:
        tunnel (NewTunnelSchema): Info on one specific tunnel
    """

    tunnel: "NewTunnelSchema"
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
        from ..models.new_tunnel_schema import NewTunnelSchema

        d = src_dict.copy()
        tunnel = NewTunnelSchema.from_dict(d.pop("tunnel"))

        new_tunnel_info = cls(
            tunnel=tunnel,
        )

        new_tunnel_info.additional_properties = d
        return new_tunnel_info

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
