import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset


T = TypeVar("T", bound="AnonAccountSchema")


@_attrs_define
class AnonAccountSchema:
    """Anonymous account base schema

    Attributes:
        username (str):
        created_date (datetime.datetime):
        id (str): ID of the account
        is_delete_protected (Union[Unset, bool]):  Default: False.
        last_updated_date (Union[Unset, datetime.datetime]):
    """

    username: str
    created_date: datetime.datetime
    id: str
    is_delete_protected: Union[Unset, bool] = False
    last_updated_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username

        created_date = self.created_date.isoformat()

        id = self.id

        is_delete_protected = self.is_delete_protected

        last_updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "created_date": created_date,
                "id": id,
            }
        )
        if is_delete_protected is not UNSET:
            field_dict["is_delete_protected"] = is_delete_protected
        if last_updated_date is not UNSET:
            field_dict["last_updated_date"] = last_updated_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username")

        created_date = isoparse(d.pop("created_date"))

        id = d.pop("id")

        is_delete_protected = d.pop("is_delete_protected", UNSET)

        _last_updated_date = d.pop("last_updated_date", UNSET)
        last_updated_date: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = isoparse(_last_updated_date)

        anon_account_schema = cls(
            username=username,
            created_date=created_date,
            id=id,
            is_delete_protected=is_delete_protected,
            last_updated_date=last_updated_date,
        )

        anon_account_schema.additional_properties = d
        return anon_account_schema

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
