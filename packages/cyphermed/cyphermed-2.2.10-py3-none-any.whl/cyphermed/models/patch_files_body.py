import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset


T = TypeVar("T", bound="PatchFilesBody")


@_attrs_define
class PatchFilesBody:
    """Which File fields to include in PATCH request bodies

    Attributes:
        unicode_1 (Union[Unset, str]): Custom unicode index 1
        unicode_2 (Union[Unset, str]): Custom unicode index 2
        unicode_3 (Union[Unset, str]): Custom unicode index 3
        unicode_4 (Union[Unset, str]): Custom unicode index 4
        unicode_5 (Union[Unset, str]): Custom unicode index 5
        unicode_6 (Union[Unset, str]): Custom unicode index 6
        number_1 (Union[Unset, float, int]): Custom number index 1
        number_2 (Union[Unset, float, int]): Custom number index 2
        size (Union[Unset, int]): Size of file in bytes
        uploaded_date (Union[Unset, datetime.datetime]): Uploaded date of files to return
        etag (Union[Unset, str]): ETag of file
    """

    unicode_1: Union[Unset, str] = UNSET
    unicode_2: Union[Unset, str] = UNSET
    unicode_3: Union[Unset, str] = UNSET
    unicode_4: Union[Unset, str] = UNSET
    unicode_5: Union[Unset, str] = UNSET
    unicode_6: Union[Unset, str] = UNSET
    number_1: Union[Unset, float, int] = UNSET
    number_2: Union[Unset, float, int] = UNSET
    size: Union[Unset, int] = UNSET
    uploaded_date: Union[Unset, datetime.datetime] = UNSET
    etag: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unicode_1 = self.unicode_1

        unicode_2 = self.unicode_2

        unicode_3 = self.unicode_3

        unicode_4 = self.unicode_4

        unicode_5 = self.unicode_5

        unicode_6 = self.unicode_6

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

        size = self.size

        uploaded_date: Union[Unset, str] = UNSET
        if not isinstance(self.uploaded_date, Unset):
            uploaded_date = self.uploaded_date.isoformat()

        etag = self.etag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if number_1 is not UNSET:
            field_dict["number_1"] = number_1
        if number_2 is not UNSET:
            field_dict["number_2"] = number_2
        if size is not UNSET:
            field_dict["size"] = size
        if uploaded_date is not UNSET:
            field_dict["uploaded_date"] = uploaded_date
        if etag is not UNSET:
            field_dict["etag"] = etag

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unicode_1 = d.pop("unicode_1", UNSET)

        unicode_2 = d.pop("unicode_2", UNSET)

        unicode_3 = d.pop("unicode_3", UNSET)

        unicode_4 = d.pop("unicode_4", UNSET)

        unicode_5 = d.pop("unicode_5", UNSET)

        unicode_6 = d.pop("unicode_6", UNSET)

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

        size = d.pop("size", UNSET)

        _uploaded_date = d.pop("uploaded_date", UNSET)
        uploaded_date: Union[Unset, datetime.datetime]
        if isinstance(_uploaded_date, Unset):
            uploaded_date = UNSET
        else:
            uploaded_date = isoparse(_uploaded_date)

        etag = d.pop("etag", UNSET)

        patch_files_body = cls(
            unicode_1=unicode_1,
            unicode_2=unicode_2,
            unicode_3=unicode_3,
            unicode_4=unicode_4,
            unicode_5=unicode_5,
            unicode_6=unicode_6,
            number_1=number_1,
            number_2=number_2,
            size=size,
            uploaded_date=uploaded_date,
            etag=etag,
        )

        patch_files_body.additional_properties = d
        return patch_files_body

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
