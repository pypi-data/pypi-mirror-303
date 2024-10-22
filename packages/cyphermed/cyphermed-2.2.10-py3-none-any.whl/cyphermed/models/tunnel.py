import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset


T = TypeVar("T", bound="Tunnel")


@_attrs_define
class Tunnel:
    """
    Attributes:
        uuid (Union[Unset, str]): UUID of the IoT tunnel
        opened_date (Union[Unset, datetime.datetime]): UTC datetime the tunnel was opened
        opened_by (Union[Unset, str]): ID of the user who opened the tunnel
        timeout (Union[Unset, int]): Timeout in seconds for this tunnel
    """

    uuid: Union[Unset, str] = UNSET
    opened_date: Union[Unset, datetime.datetime] = UNSET
    opened_by: Union[Unset, str] = UNSET
    timeout: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid

        opened_date: Union[Unset, str] = UNSET
        if not isinstance(self.opened_date, Unset):
            opened_date = self.opened_date.isoformat()

        opened_by = self.opened_by

        timeout = self.timeout

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if opened_date is not UNSET:
            field_dict["opened_date"] = opened_date
        if opened_by is not UNSET:
            field_dict["opened_by"] = opened_by
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

        _opened_date = d.pop("opened_date", UNSET)
        opened_date: Union[Unset, datetime.datetime]
        if isinstance(_opened_date, Unset):
            opened_date = UNSET
        else:
            opened_date = isoparse(_opened_date)

        opened_by = d.pop("opened_by", UNSET)

        timeout = d.pop("timeout", UNSET)

        tunnel = cls(
            uuid=uuid,
            opened_date=opened_date,
            opened_by=opened_by,
            timeout=timeout,
        )

        tunnel.additional_properties = d
        return tunnel

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
