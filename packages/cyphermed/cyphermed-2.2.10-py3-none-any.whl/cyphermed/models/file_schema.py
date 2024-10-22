import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.file_schema_etag_by_part import FileSchemaEtagByPart


T = TypeVar("T", bound="FileSchema")


@_attrs_define
class FileSchema:
    """File info fields to include in the response bodies

    Attributes:
        path (str): Path this file is stored at
        filename (str): Filename of file
        created_by (str): ID of the user who created the file
        created_date (datetime.datetime): Date and time the file was created
        revision (int): Revison number of the data entry
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
        etag_by_part (Union[Unset, FileSchemaEtagByPart]): List of ETags for each part of the multipart upload
        url (Union[Unset, str]): Pre-signed GET URL
        size (Union[Unset, int]): Size of file in bytes
        etag (Union[Unset, str]): ETag of file
        uploaded_date (Union[Unset, datetime.datetime]): Date and time the file was uploaded
        updated_by_list (Union[Unset, List[str]]): List of account IDs for most recent editors
        updated_date_list (Union[Unset, List[datetime.datetime]]): List of dates for most recent edits
    """

    path: str
    filename: str
    created_by: str
    created_date: datetime.datetime
    revision: int
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
    etag_by_part: Union[Unset, "FileSchemaEtagByPart"] = UNSET
    url: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    uploaded_date: Union[Unset, datetime.datetime] = UNSET
    updated_by_list: Union[Unset, List[str]] = UNSET
    updated_date_list: Union[Unset, List[datetime.datetime]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path

        filename = self.filename

        created_by = self.created_by

        created_date = self.created_date.isoformat()

        revision = self.revision

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

        url = self.url

        size = self.size

        etag = self.etag

        uploaded_date: Union[Unset, str] = UNSET
        if not isinstance(self.uploaded_date, Unset):
            uploaded_date = self.uploaded_date.isoformat()

        updated_by_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.updated_by_list, Unset):
            updated_by_list = self.updated_by_list

        updated_date_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.updated_date_list, Unset):
            updated_date_list = []
            for updated_date_list_item_data in self.updated_date_list:
                updated_date_list_item = updated_date_list_item_data.isoformat()
                updated_date_list.append(updated_date_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "filename": filename,
                "created_by": created_by,
                "created_date": created_date,
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
        if url is not UNSET:
            field_dict["url"] = url
        if size is not UNSET:
            field_dict["size"] = size
        if etag is not UNSET:
            field_dict["etag"] = etag
        if uploaded_date is not UNSET:
            field_dict["uploaded_date"] = uploaded_date
        if updated_by_list is not UNSET:
            field_dict["updated_by_list"] = updated_by_list
        if updated_date_list is not UNSET:
            field_dict["updated_date_list"] = updated_date_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_schema_etag_by_part import FileSchemaEtagByPart

        d = src_dict.copy()
        path = d.pop("path")

        filename = d.pop("filename")

        created_by = d.pop("created_by")

        created_date = isoparse(d.pop("created_date"))

        revision = d.pop("revision")

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
        etag_by_part: Union[Unset, FileSchemaEtagByPart]
        if isinstance(_etag_by_part, Unset):
            etag_by_part = UNSET
        else:
            etag_by_part = FileSchemaEtagByPart.from_dict(_etag_by_part)

        url = d.pop("url", UNSET)

        size = d.pop("size", UNSET)

        etag = d.pop("etag", UNSET)

        _uploaded_date = d.pop("uploaded_date", UNSET)
        uploaded_date: Union[Unset, datetime.datetime]
        if isinstance(_uploaded_date, Unset):
            uploaded_date = UNSET
        else:
            uploaded_date = isoparse(_uploaded_date)

        updated_by_list = cast(List[str], d.pop("updated_by_list", UNSET))

        updated_date_list = []
        _updated_date_list = d.pop("updated_date_list", UNSET)
        for updated_date_list_item_data in _updated_date_list or []:
            updated_date_list_item = isoparse(updated_date_list_item_data)

            updated_date_list.append(updated_date_list_item)

        file_schema = cls(
            path=path,
            filename=filename,
            created_by=created_by,
            created_date=created_date,
            revision=revision,
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
            url=url,
            size=size,
            etag=etag,
            uploaded_date=uploaded_date,
            updated_by_list=updated_by_list,
            updated_date_list=updated_date_list,
        )

        file_schema.additional_properties = d
        return file_schema

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
