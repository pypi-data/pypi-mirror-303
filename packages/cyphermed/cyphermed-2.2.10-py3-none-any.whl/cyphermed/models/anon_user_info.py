from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.anon_account_schema import AnonAccountSchema


T = TypeVar("T", bound="AnonUserInfo")


@_attrs_define
class AnonUserInfo:
    """Info on one specific user

    Attributes:
        user (AnonAccountSchema): Anonymous account base schema
    """

    user: "AnonAccountSchema"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.anon_account_schema import AnonAccountSchema

        d = src_dict.copy()
        user = AnonAccountSchema.from_dict(d.pop("user"))

        anon_user_info = cls(
            user=user,
        )

        anon_user_info.additional_properties = d
        return anon_user_info

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
