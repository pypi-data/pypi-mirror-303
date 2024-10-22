from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


T = TypeVar("T", bound="PatchMfaSettingsFormParams")


@_attrs_define
class PatchMfaSettingsFormParams:
    """
    Attributes:
        preferred_mfa (str): Preferred MFA device
    """

    preferred_mfa: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        preferred_mfa = self.preferred_mfa

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "preferred_mfa": preferred_mfa,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        preferred_mfa = d.pop("preferred_mfa")

        patch_mfa_settings_form_params = cls(
            preferred_mfa=preferred_mfa,
        )

        patch_mfa_settings_form_params.additional_properties = d
        return patch_mfa_settings_form_params

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
