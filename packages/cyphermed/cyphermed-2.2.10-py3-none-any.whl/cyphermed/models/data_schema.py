import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.data_schema_value import DataSchemaValue


T = TypeVar("T", bound="DataSchema")


@_attrs_define
class DataSchema:
    """Group data

    Attributes:
        path (str): Path this data entry is stored at
        value (DataSchemaValue): Data stored at this path
        created_by (str): ID of the account that created this data
        created_date (datetime.datetime): Date this data was created
        updated_by_list (List[str]): List of account IDs for most recent editors
        updated_date_list (List[datetime.datetime]): List of dates for most recent edits
        verified (bool): Whether the signature on this entry was verified on retrieval
        revision (int): Revison number of the data entry
        unicode_1 (Union[Unset, str]): Custom unicode index 1
        unicode_2 (Union[Unset, str]): Custom unicode index 2
        unicode_3 (Union[Unset, str]): Custom unicode index 3
        unicode_4 (Union[Unset, str]): Custom unicode index 4
        unicode_5 (Union[Unset, str]): Custom unicode index 5
        unicode_6 (Union[Unset, str]): Custom unicode index 6
        unicode_7 (Union[Unset, str]): Custom unicode index 7
        unicode_8 (Union[Unset, str]): Custom unicode index 8
        unicode_9 (Union[Unset, str]): Custom unicode index 9
        unicode_10 (Union[Unset, str]): Custom unicode index 10
        number_1 (Union[Unset, float, int]): Custom number index 1
        number_2 (Union[Unset, float, int]): Custom number index 2
    """

    path: str
    value: "DataSchemaValue"
    created_by: str
    created_date: datetime.datetime
    updated_by_list: List[str]
    updated_date_list: List[datetime.datetime]
    verified: bool
    revision: int
    unicode_1: Union[Unset, str] = UNSET
    unicode_2: Union[Unset, str] = UNSET
    unicode_3: Union[Unset, str] = UNSET
    unicode_4: Union[Unset, str] = UNSET
    unicode_5: Union[Unset, str] = UNSET
    unicode_6: Union[Unset, str] = UNSET
    unicode_7: Union[Unset, str] = UNSET
    unicode_8: Union[Unset, str] = UNSET
    unicode_9: Union[Unset, str] = UNSET
    unicode_10: Union[Unset, str] = UNSET
    number_1: Union[Unset, float, int] = UNSET
    number_2: Union[Unset, float, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path

        value = self.value.to_dict()

        created_by = self.created_by

        created_date = self.created_date.isoformat()

        updated_by_list = self.updated_by_list

        updated_date_list = []
        for updated_date_list_item_data in self.updated_date_list:
            updated_date_list_item = updated_date_list_item_data.isoformat()
            updated_date_list.append(updated_date_list_item)

        verified = self.verified

        revision = self.revision

        unicode_1 = self.unicode_1

        unicode_2 = self.unicode_2

        unicode_3 = self.unicode_3

        unicode_4 = self.unicode_4

        unicode_5 = self.unicode_5

        unicode_6 = self.unicode_6

        unicode_7 = self.unicode_7

        unicode_8 = self.unicode_8

        unicode_9 = self.unicode_9

        unicode_10 = self.unicode_10

        number_1: Union[Unset, float, int]
        if isinstance(self.number_1, Unset):
            number_1 = UNSET
        else:
            number_1 = self.number_1

        number_2: Union[Unset, float, int]
        if isinstance(self.number_2, Unset):
            number_2 = UNSET
        else:
            number_2 = self.number_2

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "value": value,
                "created_by": created_by,
                "created_date": created_date,
                "updated_by_list": updated_by_list,
                "updated_date_list": updated_date_list,
                "verified": verified,
                "revision": revision,
            }
        )
        if unicode_1 is not UNSET:
            field_dict["unicode_1"] = unicode_1
        if unicode_2 is not UNSET:
            field_dict["unicode_2"] = unicode_2
        if unicode_3 is not UNSET:
            field_dict["unicode_3"] = unicode_3
        if unicode_4 is not UNSET:
            field_dict["unicode_4"] = unicode_4
        if unicode_5 is not UNSET:
            field_dict["unicode_5"] = unicode_5
        if unicode_6 is not UNSET:
            field_dict["unicode_6"] = unicode_6
        if unicode_7 is not UNSET:
            field_dict["unicode_7"] = unicode_7
        if unicode_8 is not UNSET:
            field_dict["unicode_8"] = unicode_8
        if unicode_9 is not UNSET:
            field_dict["unicode_9"] = unicode_9
        if unicode_10 is not UNSET:
            field_dict["unicode_10"] = unicode_10
        if number_1 is not UNSET:
            field_dict["number_1"] = number_1
        if number_2 is not UNSET:
            field_dict["number_2"] = number_2

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_schema_value import DataSchemaValue

        d = src_dict.copy()
        path = d.pop("path")

        value = DataSchemaValue.from_dict(d.pop("value"))

        created_by = d.pop("created_by")

        created_date = isoparse(d.pop("created_date"))

        updated_by_list = cast(List[str], d.pop("updated_by_list"))

        updated_date_list = []
        _updated_date_list = d.pop("updated_date_list")
        for updated_date_list_item_data in _updated_date_list:
            updated_date_list_item = isoparse(updated_date_list_item_data)

            updated_date_list.append(updated_date_list_item)

        verified = d.pop("verified")

        revision = d.pop("revision")

        unicode_1 = d.pop("unicode_1", UNSET)

        unicode_2 = d.pop("unicode_2", UNSET)

        unicode_3 = d.pop("unicode_3", UNSET)

        unicode_4 = d.pop("unicode_4", UNSET)

        unicode_5 = d.pop("unicode_5", UNSET)

        unicode_6 = d.pop("unicode_6", UNSET)

        unicode_7 = d.pop("unicode_7", UNSET)

        unicode_8 = d.pop("unicode_8", UNSET)

        unicode_9 = d.pop("unicode_9", UNSET)

        unicode_10 = d.pop("unicode_10", UNSET)

        def _parse_number_1(data: object) -> Union[Unset, float, int]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, float, int], data)

        number_1 = _parse_number_1(d.pop("number_1", UNSET))

        def _parse_number_2(data: object) -> Union[Unset, float, int]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, float, int], data)

        number_2 = _parse_number_2(d.pop("number_2", UNSET))

        data_schema = cls(
            path=path,
            value=value,
            created_by=created_by,
            created_date=created_date,
            updated_by_list=updated_by_list,
            updated_date_list=updated_date_list,
            verified=verified,
            revision=revision,
            unicode_1=unicode_1,
            unicode_2=unicode_2,
            unicode_3=unicode_3,
            unicode_4=unicode_4,
            unicode_5=unicode_5,
            unicode_6=unicode_6,
            unicode_7=unicode_7,
            unicode_8=unicode_8,
            unicode_9=unicode_9,
            unicode_10=unicode_10,
            number_1=number_1,
            number_2=number_2,
        )

        data_schema.additional_properties = d
        return data_schema

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
