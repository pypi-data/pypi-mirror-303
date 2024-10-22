from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.file_schema import FileSchema
    from ..models.files_at_path_last_evaluated_key import FilesAtPathLastEvaluatedKey


T = TypeVar("T", bound="FilesAtPath")


@_attrs_define
class FilesAtPath:
    """List of file info

    Attributes:
        url (Union[Unset, str]): Pre-signed S3 URL
        urls (Union[Unset, List[str]]): List of pre-signed S3 URLs
        paths (Union[Unset, List[str]]):
        object_count (Union[Unset, int]):
        last_evaluated_key (Union[Unset, FilesAtPathLastEvaluatedKey]):
        file (Union[Unset, FileSchema]): File info fields to include in the response bodies
        files (Union[Unset, List['FileSchema']]): List of file info
    """

    url: Union[Unset, str] = UNSET
    urls: Union[Unset, List[str]] = UNSET
    paths: Union[Unset, List[str]] = UNSET
    object_count: Union[Unset, int] = UNSET
    last_evaluated_key: Union[Unset, "FilesAtPathLastEvaluatedKey"] = UNSET
    file: Union[Unset, "FileSchema"] = UNSET
    files: Union[Unset, List["FileSchema"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url

        urls: Union[Unset, List[str]] = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls

        paths: Union[Unset, List[str]] = UNSET
        if not isinstance(self.paths, Unset):
            paths = self.paths

        object_count = self.object_count

        last_evaluated_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_evaluated_key, Unset):
            last_evaluated_key = self.last_evaluated_key.to_dict()

        file: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        files: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if urls is not UNSET:
            field_dict["urls"] = urls
        if paths is not UNSET:
            field_dict["paths"] = paths
        if object_count is not UNSET:
            field_dict["object_count"] = object_count
        if last_evaluated_key is not UNSET:
            field_dict["last_evaluated_key"] = last_evaluated_key
        if file is not UNSET:
            field_dict["file"] = file
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_schema import FileSchema
        from ..models.files_at_path_last_evaluated_key import (
            FilesAtPathLastEvaluatedKey,
        )

        d = src_dict.copy()
        url = d.pop("url", UNSET)

        urls = cast(List[str], d.pop("urls", UNSET))

        paths = cast(List[str], d.pop("paths", UNSET))

        object_count = d.pop("object_count", UNSET)

        _last_evaluated_key = d.pop("last_evaluated_key", UNSET)
        last_evaluated_key: Union[Unset, FilesAtPathLastEvaluatedKey]
        if isinstance(_last_evaluated_key, Unset):
            last_evaluated_key = UNSET
        else:
            last_evaluated_key = FilesAtPathLastEvaluatedKey.from_dict(_last_evaluated_key)

        _file = d.pop("file", UNSET)
        file: Union[Unset, FileSchema]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = FileSchema.from_dict(_file)

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = FileSchema.from_dict(files_item_data)

            files.append(files_item)

        files_at_path = cls(
            url=url,
            urls=urls,
            paths=paths,
            object_count=object_count,
            last_evaluated_key=last_evaluated_key,
            file=file,
            files=files,
        )

        files_at_path.additional_properties = d
        return files_at_path

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
