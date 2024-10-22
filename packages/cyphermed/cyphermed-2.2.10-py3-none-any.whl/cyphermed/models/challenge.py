from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


T = TypeVar("T", bound="Challenge")


@_attrs_define
class Challenge:
    """Challenge response schema

    Attributes:
        challenge (str): Challenge code, a unique identifier for the type of challenge
        message (str): Message to display to the user
        session (str): Session token to use in the challenge response
    """

    challenge: str
    message: str
    session: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        challenge = self.challenge

        message = self.message

        session = self.session

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "challenge": challenge,
                "message": message,
                "session": session,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        challenge = d.pop("challenge")

        message = d.pop("message")

        session = d.pop("session")

        challenge = cls(
            challenge=challenge,
            message=message,
            session=session,
        )

        challenge.additional_properties = d
        return challenge

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
