from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


T = TypeVar("T", bound="NewMqttCredentials")


@_attrs_define
class NewMqttCredentials:
    """ "Info on new MQTT credentials

    Attributes:
        certificate (str): PEM-encoded certificate for this device
        root_ca (str): URL for the root CA certificate, which is in PEM format
        public_key (str): Public key for this device
        private_key (str): Private key for this device
        broker (str): Domain of the MQTT broker, does not include protocol or port
        root_scope (str): Root MQTT scope for topics this device can utilize
    """

    certificate: str
    root_ca: str
    public_key: str
    private_key: str
    broker: str
    root_scope: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificate = self.certificate

        root_ca = self.root_ca

        public_key = self.public_key

        private_key = self.private_key

        broker = self.broker

        root_scope = self.root_scope

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "certificate": certificate,
                "root_ca": root_ca,
                "public_key": public_key,
                "private_key": private_key,
                "broker": broker,
                "root_scope": root_scope,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        certificate = d.pop("certificate")

        root_ca = d.pop("root_ca")

        public_key = d.pop("public_key")

        private_key = d.pop("private_key")

        broker = d.pop("broker")

        root_scope = d.pop("root_scope")

        new_mqtt_credentials = cls(
            certificate=certificate,
            root_ca=root_ca,
            public_key=public_key,
            private_key=private_key,
            broker=broker,
            root_scope=root_scope,
        )

        new_mqtt_credentials.additional_properties = d
        return new_mqtt_credentials

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
