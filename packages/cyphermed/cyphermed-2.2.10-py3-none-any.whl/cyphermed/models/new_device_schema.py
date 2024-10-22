from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="NewDeviceSchema")


@_attrs_define
class NewDeviceSchema:
    """Which Device fields to include in response bodies

    Attributes:
        id (str): ID of the newly created device
        api_key (str): API key for this device - ONLY SHOWN ONCE, NOT STORED
        certificate (str): PEM-encoded certificate for this device
        root_ca (str): URL for the root CA certificate, which is in PEM format
        public_key (str): Public key for this device
        private_key (str): Private key for this device
        broker (str): Domain of the MQTT broker, does not include protocol or port
        root_scope (str): Root MQTT scope for topics this device can utilize
        owner_id (Union[Unset, str]): ID of the device owner
    """

    id: str
    api_key: str
    certificate: str
    root_ca: str
    public_key: str
    private_key: str
    broker: str
    root_scope: str
    owner_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        api_key = self.api_key

        certificate = self.certificate

        root_ca = self.root_ca

        public_key = self.public_key

        private_key = self.private_key

        broker = self.broker

        root_scope = self.root_scope

        owner_id = self.owner_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "api_key": api_key,
                "certificate": certificate,
                "root_ca": root_ca,
                "public_key": public_key,
                "private_key": private_key,
                "broker": broker,
                "root_scope": root_scope,
            }
        )
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        api_key = d.pop("api_key")

        certificate = d.pop("certificate")

        root_ca = d.pop("root_ca")

        public_key = d.pop("public_key")

        private_key = d.pop("private_key")

        broker = d.pop("broker")

        root_scope = d.pop("root_scope")

        owner_id = d.pop("owner_id", UNSET)

        new_device_schema = cls(
            id=id,
            api_key=api_key,
            certificate=certificate,
            root_ca=root_ca,
            public_key=public_key,
            private_key=private_key,
            broker=broker,
            root_scope=root_scope,
            owner_id=owner_id,
        )

        new_device_schema.additional_properties = d
        return new_device_schema

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
