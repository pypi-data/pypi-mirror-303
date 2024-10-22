from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.put_files_body_etag_by_part import PutFilesBodyEtagByPart


T = TypeVar("T", bound="PutFilesBody")


@_attrs_define
class PutFilesBody:
    """Which File fields to include in PUT request bodies

    Attributes:
        unicode_1 (Union[Unset, str]): Custom unicode index 1
        unicode_2 (Union[Unset, str]): Custom unicode index 2
        unicode_3 (Union[Unset, str]): Custom unicode index 3
        unicode_4 (Union[Unset, str]): Custom unicode index 4
        unicode_5 (Union[Unset, str]): Custom unicode index 5
        unicode_6 (Union[Unset, str]): Custom unicode index 6
        number_1 (Union[Unset, float, int]): Custom number index 1
        number_2 (Union[Unset, float, int]): Custom number index 2
        expires_in (Union[Unset, int]): Number of seconds before presigned URLs expire Default: 3600.
        content_type (Union[Unset, str]): Optionally specify the content type of the file you will upload
        num_parts (Union[Unset, int]): Number of parts to upload
        completed_upload_id (Union[Unset, str]): ID of completed multipart upload to merge
        etag_by_part (Union[Unset, PutFilesBodyEtagByPart]): List of ETags for each part of the multipart upload
    """

    unicode_1: Union[Unset, str] = UNSET
    unicode_2: Union[Unset, str] = UNSET
    unicode_3: Union[Unset, str] = UNSET
    unicode_4: Union[Unset, str] = UNSET
    unicode_5: Union[Unset, str] = UNSET
    unicode_6: Union[Unset, str] = UNSET
    number_1: Union[Unset, float, int] = UNSET
    number_2: Union[Unset, float, int] = UNSET
    expires_in: Union[Unset, int] = 3600
    content_type: Union[Unset, str] = UNSET
    num_parts: Union[Unset, int] = UNSET
    completed_upload_id: Union[Unset, str] = UNSET
    etag_by_part: Union[Unset, "PutFilesBodyEtagByPart"] = UNSET
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

        expires_in = self.expires_in

        content_type = self.content_type

        num_parts = self.num_parts

        completed_upload_id = self.completed_upload_id

        etag_by_part: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.etag_by_part, Unset):
            etag_by_part = self.etag_by_part.to_dict()

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
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if num_parts is not UNSET:
            field_dict["num_parts"] = num_parts
        if completed_upload_id is not UNSET:
            field_dict["completed_upload_id"] = completed_upload_id
        if etag_by_part is not UNSET:
            field_dict["etag_by_part"] = etag_by_part

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.put_files_body_etag_by_part import PutFilesBodyEtagByPart

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

        expires_in = d.pop("expires_in", UNSET)

        content_type = d.pop("content_type", UNSET)

        num_parts = d.pop("num_parts", UNSET)

        completed_upload_id = d.pop("completed_upload_id", UNSET)

        _etag_by_part = d.pop("etag_by_part", UNSET)
        etag_by_part: Union[Unset, PutFilesBodyEtagByPart]
        if isinstance(_etag_by_part, Unset):
            etag_by_part = UNSET
        else:
            etag_by_part = PutFilesBodyEtagByPart.from_dict(_etag_by_part)

        put_files_body = cls(
            unicode_1=unicode_1,
            unicode_2=unicode_2,
            unicode_3=unicode_3,
            unicode_4=unicode_4,
            unicode_5=unicode_5,
            unicode_6=unicode_6,
            number_1=number_1,
            number_2=number_2,
            expires_in=expires_in,
            content_type=content_type,
            num_parts=num_parts,
            completed_upload_id=completed_upload_id,
            etag_by_part=etag_by_part,
        )

        put_files_body.additional_properties = d
        return put_files_body

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
