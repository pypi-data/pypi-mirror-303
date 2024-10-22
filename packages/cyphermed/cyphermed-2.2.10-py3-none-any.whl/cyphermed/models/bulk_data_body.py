from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.delete_data_job import DeleteDataJob
    from ..models.get_data_job import GetDataJob
    from ..models.patch_data_job import PatchDataJob
    from ..models.upload_data_job import UploadDataJob


T = TypeVar("T", bound="BulkDataBody")


@_attrs_define
class BulkDataBody:
    """Bulk request body

    Attributes:
        method (str): Method to use for bulk request
        jobs (List[Union['DeleteDataJob', 'GetDataJob', 'PatchDataJob', 'UploadDataJob']]): Jobs to perform, grouped by
            group ID, all of the same method
    """

    method: str
    jobs: List[Union["DeleteDataJob", "GetDataJob", "PatchDataJob", "UploadDataJob"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.get_data_job import GetDataJob
        from ..models.patch_data_job import PatchDataJob
        from ..models.upload_data_job import UploadDataJob

        method = self.method

        jobs = []
        for jobs_item_data in self.jobs:
            jobs_item: Dict[str, Any]
            if isinstance(jobs_item_data, UploadDataJob):
                jobs_item = jobs_item_data.to_dict()
            elif isinstance(jobs_item_data, PatchDataJob):
                jobs_item = jobs_item_data.to_dict()
            elif isinstance(jobs_item_data, GetDataJob):
                jobs_item = jobs_item_data.to_dict()
            else:
                jobs_item = jobs_item_data.to_dict()

            jobs.append(jobs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "jobs": jobs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.delete_data_job import DeleteDataJob
        from ..models.get_data_job import GetDataJob
        from ..models.patch_data_job import PatchDataJob
        from ..models.upload_data_job import UploadDataJob

        d = src_dict.copy()
        method = d.pop("method")

        jobs = []
        _jobs = d.pop("jobs")
        for jobs_item_data in _jobs:

            def _parse_jobs_item(
                data: object,
            ) -> Union["DeleteDataJob", "GetDataJob", "PatchDataJob", "UploadDataJob"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    jobs_item_type_0 = UploadDataJob.from_dict(data)

                    return jobs_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    jobs_item_type_1 = PatchDataJob.from_dict(data)

                    return jobs_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    jobs_item_type_2 = GetDataJob.from_dict(data)

                    return jobs_item_type_2
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                jobs_item_type_3 = DeleteDataJob.from_dict(data)

                return jobs_item_type_3

            jobs_item = _parse_jobs_item(jobs_item_data)

            jobs.append(jobs_item)

        bulk_data_body = cls(
            method=method,
            jobs=jobs,
        )

        bulk_data_body.additional_properties = d
        return bulk_data_body

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
