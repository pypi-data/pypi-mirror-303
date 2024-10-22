import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.get_data_job_last_evaluated_key_type_0 import (
        GetDataJobLastEvaluatedKeyType0,
    )


T = TypeVar("T", bound="GetDataJob")


@_attrs_define
class GetDataJob:
    """Represents a single GET in a bulk request

    Attributes:
        paths (List[str]): Paths to get
        cascade (Union[Unset, bool]): If true, return all paths starting with the specified path
        paths_only (Union[Unset, bool]): If true, only return list of matching file paths
        object_count (Union[Unset, bool]): If true, only return the number of objects in the file
        desc (Union[Unset, bool]): Whether to order results in descending order
        bust_cache (Union[Unset, bool]): Whether to bypass the cache and get the latest data
        limit (Union[Unset, int]): Maximum number of results to return Default: 100.
        order_by (Union[Unset, str]): Field to order results by
        last_evaluated_key (Union['GetDataJobLastEvaluatedKeyType0', Unset, str]): Key to start results from
        search (Union[Unset, str]): Search term to filter accounts by
        search_fields (Union[Unset, str]): Fields to search in
        path_filter (Union[Unset, str]): Regex pattern to match result paths against
        created_by (Union[Unset, str]): ID of the user who created the entry
        last_updated_by (Union[Unset, str]): ID of the user who last updated the entry
        created_date (Union[Unset, datetime.datetime]): Created date of items to return
        created_date_gte (Union[Unset, datetime.datetime]):
        created_date_lte (Union[Unset, datetime.datetime]):
        last_updated_date (Union[Unset, datetime.datetime]): Last edited date of items to return
        last_updated_date_gte (Union[Unset, datetime.datetime]):
        last_updated_date_lte (Union[Unset, datetime.datetime]):
        unicode_1 (Union[Unset, str]): Custom unicode index 1
        unicode_1_sw (Union[Unset, str]):
        unicode_1_contains (Union[Unset, str]):
        unicode_1_gte (Union[Unset, str]):
        unicode_1_lte (Union[Unset, str]):
        unicode_2 (Union[Unset, str]): Custom unicode index 2
        unicode_2_sw (Union[Unset, str]):
        unicode_2_contains (Union[Unset, str]):
        unicode_2_gte (Union[Unset, str]):
        unicode_2_lte (Union[Unset, str]):
        unicode_3 (Union[Unset, str]): Custom unicode index 3
        unicode_3_sw (Union[Unset, str]):
        unicode_3_contains (Union[Unset, str]):
        unicode_3_gte (Union[Unset, str]):
        unicode_3_lte (Union[Unset, str]):
        unicode_4 (Union[Unset, str]): Custom unicode index 4
        unicode_4_sw (Union[Unset, str]):
        unicode_4_contains (Union[Unset, str]):
        unicode_4_gte (Union[Unset, str]):
        unicode_4_lte (Union[Unset, str]):
        unicode_5 (Union[Unset, str]): Custom unicode index 5
        unicode_5_sw (Union[Unset, str]):
        unicode_5_contains (Union[Unset, str]):
        unicode_5_gte (Union[Unset, str]):
        unicode_5_lte (Union[Unset, str]):
        unicode_6 (Union[Unset, str]): Custom unicode index 6
        unicode_6_sw (Union[Unset, str]):
        unicode_6_contains (Union[Unset, str]):
        unicode_6_gte (Union[Unset, str]):
        unicode_6_lte (Union[Unset, str]):
        number_1 (Union[Unset, float]): Custom number index 1
        number_1_gt (Union[Unset, float]):
        number_1_gte (Union[Unset, float]):
        number_1_lt (Union[Unset, float]):
        number_1_lte (Union[Unset, float]):
        number_2 (Union[Unset, float]): Custom number index 2
        number_2_gt (Union[Unset, float]):
        number_2_gte (Union[Unset, float]):
        number_2_lt (Union[Unset, float]):
        number_2_lte (Union[Unset, float]):
        verify (Union[Unset, bool]): Whether to verify the signature on the item
        unicode_7 (Union[Unset, str]): Custom unicode index 7
        unicode_7_sw (Union[Unset, str]):
        unicode_7_contains (Union[Unset, str]):
        unicode_7_gte (Union[Unset, str]):
        unicode_7_lte (Union[Unset, str]):
        unicode_8 (Union[Unset, str]): Custom unicode index 8
        unicode_8_sw (Union[Unset, str]):
        unicode_8_contains (Union[Unset, str]):
        unicode_8_gte (Union[Unset, str]):
        unicode_8_lte (Union[Unset, str]):
        unicode_9 (Union[Unset, str]): Custom unicode index 9
        unicode_9_sw (Union[Unset, str]):
        unicode_9_contains (Union[Unset, str]):
        unicode_9_gte (Union[Unset, str]):
        unicode_9_lte (Union[Unset, str]):
        unicode_10 (Union[Unset, str]): Custom unicode index 10
        unicode_10_sw (Union[Unset, str]):
        unicode_10_contains (Union[Unset, str]):
        unicode_10_gte (Union[Unset, str]):
        unicode_10_lte (Union[Unset, str]):
    """

    paths: List[str]
    cascade: Union[Unset, bool] = UNSET
    paths_only: Union[Unset, bool] = UNSET
    object_count: Union[Unset, bool] = UNSET
    desc: Union[Unset, bool] = UNSET
    bust_cache: Union[Unset, bool] = UNSET
    limit: Union[Unset, int] = 100
    order_by: Union[Unset, str] = UNSET
    last_evaluated_key: Union["GetDataJobLastEvaluatedKeyType0", Unset, str] = UNSET
    search: Union[Unset, str] = UNSET
    search_fields: Union[Unset, str] = UNSET
    path_filter: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    last_updated_by: Union[Unset, str] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    created_date_gte: Union[Unset, datetime.datetime] = UNSET
    created_date_lte: Union[Unset, datetime.datetime] = UNSET
    last_updated_date: Union[Unset, datetime.datetime] = UNSET
    last_updated_date_gte: Union[Unset, datetime.datetime] = UNSET
    last_updated_date_lte: Union[Unset, datetime.datetime] = UNSET
    unicode_1: Union[Unset, str] = UNSET
    unicode_1_sw: Union[Unset, str] = UNSET
    unicode_1_contains: Union[Unset, str] = UNSET
    unicode_1_gte: Union[Unset, str] = UNSET
    unicode_1_lte: Union[Unset, str] = UNSET
    unicode_2: Union[Unset, str] = UNSET
    unicode_2_sw: Union[Unset, str] = UNSET
    unicode_2_contains: Union[Unset, str] = UNSET
    unicode_2_gte: Union[Unset, str] = UNSET
    unicode_2_lte: Union[Unset, str] = UNSET
    unicode_3: Union[Unset, str] = UNSET
    unicode_3_sw: Union[Unset, str] = UNSET
    unicode_3_contains: Union[Unset, str] = UNSET
    unicode_3_gte: Union[Unset, str] = UNSET
    unicode_3_lte: Union[Unset, str] = UNSET
    unicode_4: Union[Unset, str] = UNSET
    unicode_4_sw: Union[Unset, str] = UNSET
    unicode_4_contains: Union[Unset, str] = UNSET
    unicode_4_gte: Union[Unset, str] = UNSET
    unicode_4_lte: Union[Unset, str] = UNSET
    unicode_5: Union[Unset, str] = UNSET
    unicode_5_sw: Union[Unset, str] = UNSET
    unicode_5_contains: Union[Unset, str] = UNSET
    unicode_5_gte: Union[Unset, str] = UNSET
    unicode_5_lte: Union[Unset, str] = UNSET
    unicode_6: Union[Unset, str] = UNSET
    unicode_6_sw: Union[Unset, str] = UNSET
    unicode_6_contains: Union[Unset, str] = UNSET
    unicode_6_gte: Union[Unset, str] = UNSET
    unicode_6_lte: Union[Unset, str] = UNSET
    number_1: Union[Unset, float] = UNSET
    number_1_gt: Union[Unset, float] = UNSET
    number_1_gte: Union[Unset, float] = UNSET
    number_1_lt: Union[Unset, float] = UNSET
    number_1_lte: Union[Unset, float] = UNSET
    number_2: Union[Unset, float] = UNSET
    number_2_gt: Union[Unset, float] = UNSET
    number_2_gte: Union[Unset, float] = UNSET
    number_2_lt: Union[Unset, float] = UNSET
    number_2_lte: Union[Unset, float] = UNSET
    verify: Union[Unset, bool] = UNSET
    unicode_7: Union[Unset, str] = UNSET
    unicode_7_sw: Union[Unset, str] = UNSET
    unicode_7_contains: Union[Unset, str] = UNSET
    unicode_7_gte: Union[Unset, str] = UNSET
    unicode_7_lte: Union[Unset, str] = UNSET
    unicode_8: Union[Unset, str] = UNSET
    unicode_8_sw: Union[Unset, str] = UNSET
    unicode_8_contains: Union[Unset, str] = UNSET
    unicode_8_gte: Union[Unset, str] = UNSET
    unicode_8_lte: Union[Unset, str] = UNSET
    unicode_9: Union[Unset, str] = UNSET
    unicode_9_sw: Union[Unset, str] = UNSET
    unicode_9_contains: Union[Unset, str] = UNSET
    unicode_9_gte: Union[Unset, str] = UNSET
    unicode_9_lte: Union[Unset, str] = UNSET
    unicode_10: Union[Unset, str] = UNSET
    unicode_10_sw: Union[Unset, str] = UNSET
    unicode_10_contains: Union[Unset, str] = UNSET
    unicode_10_gte: Union[Unset, str] = UNSET
    unicode_10_lte: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.get_data_job_last_evaluated_key_type_0 import (
            GetDataJobLastEvaluatedKeyType0,
        )

        paths = self.paths

        cascade = self.cascade

        paths_only = self.paths_only

        object_count = self.object_count

        desc = self.desc

        bust_cache = self.bust_cache

        limit = self.limit

        order_by = self.order_by

        last_evaluated_key: Union[Dict[str, Any], Unset, str]
        if isinstance(self.last_evaluated_key, Unset):
            last_evaluated_key = UNSET
        elif isinstance(self.last_evaluated_key, GetDataJobLastEvaluatedKeyType0):
            last_evaluated_key = self.last_evaluated_key.to_dict()
        else:
            last_evaluated_key = self.last_evaluated_key

        search = self.search

        search_fields = self.search_fields

        path_filter = self.path_filter

        created_by = self.created_by

        last_updated_by = self.last_updated_by

        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        created_date_gte: Union[Unset, str] = UNSET
        if not isinstance(self.created_date_gte, Unset):
            created_date_gte = self.created_date_gte.isoformat()

        created_date_lte: Union[Unset, str] = UNSET
        if not isinstance(self.created_date_lte, Unset):
            created_date_lte = self.created_date_lte.isoformat()

        last_updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.isoformat()

        last_updated_date_gte: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date_gte, Unset):
            last_updated_date_gte = self.last_updated_date_gte.isoformat()

        last_updated_date_lte: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date_lte, Unset):
            last_updated_date_lte = self.last_updated_date_lte.isoformat()

        unicode_1 = self.unicode_1

        unicode_1_sw = self.unicode_1_sw

        unicode_1_contains = self.unicode_1_contains

        unicode_1_gte = self.unicode_1_gte

        unicode_1_lte = self.unicode_1_lte

        unicode_2 = self.unicode_2

        unicode_2_sw = self.unicode_2_sw

        unicode_2_contains = self.unicode_2_contains

        unicode_2_gte = self.unicode_2_gte

        unicode_2_lte = self.unicode_2_lte

        unicode_3 = self.unicode_3

        unicode_3_sw = self.unicode_3_sw

        unicode_3_contains = self.unicode_3_contains

        unicode_3_gte = self.unicode_3_gte

        unicode_3_lte = self.unicode_3_lte

        unicode_4 = self.unicode_4

        unicode_4_sw = self.unicode_4_sw

        unicode_4_contains = self.unicode_4_contains

        unicode_4_gte = self.unicode_4_gte

        unicode_4_lte = self.unicode_4_lte

        unicode_5 = self.unicode_5

        unicode_5_sw = self.unicode_5_sw

        unicode_5_contains = self.unicode_5_contains

        unicode_5_gte = self.unicode_5_gte

        unicode_5_lte = self.unicode_5_lte

        unicode_6 = self.unicode_6

        unicode_6_sw = self.unicode_6_sw

        unicode_6_contains = self.unicode_6_contains

        unicode_6_gte = self.unicode_6_gte

        unicode_6_lte = self.unicode_6_lte

        number_1 = self.number_1

        number_1_gt = self.number_1_gt

        number_1_gte = self.number_1_gte

        number_1_lt = self.number_1_lt

        number_1_lte = self.number_1_lte

        number_2 = self.number_2

        number_2_gt = self.number_2_gt

        number_2_gte = self.number_2_gte

        number_2_lt = self.number_2_lt

        number_2_lte = self.number_2_lte

        verify = self.verify

        unicode_7 = self.unicode_7

        unicode_7_sw = self.unicode_7_sw

        unicode_7_contains = self.unicode_7_contains

        unicode_7_gte = self.unicode_7_gte

        unicode_7_lte = self.unicode_7_lte

        unicode_8 = self.unicode_8

        unicode_8_sw = self.unicode_8_sw

        unicode_8_contains = self.unicode_8_contains

        unicode_8_gte = self.unicode_8_gte

        unicode_8_lte = self.unicode_8_lte

        unicode_9 = self.unicode_9

        unicode_9_sw = self.unicode_9_sw

        unicode_9_contains = self.unicode_9_contains

        unicode_9_gte = self.unicode_9_gte

        unicode_9_lte = self.unicode_9_lte

        unicode_10 = self.unicode_10

        unicode_10_sw = self.unicode_10_sw

        unicode_10_contains = self.unicode_10_contains

        unicode_10_gte = self.unicode_10_gte

        unicode_10_lte = self.unicode_10_lte

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paths": paths,
            }
        )
        if cascade is not UNSET:
            field_dict["cascade"] = cascade
        if paths_only is not UNSET:
            field_dict["paths_only"] = paths_only
        if object_count is not UNSET:
            field_dict["object_count"] = object_count
        if desc is not UNSET:
            field_dict["desc"] = desc
        if bust_cache is not UNSET:
            field_dict["bust_cache"] = bust_cache
        if limit is not UNSET:
            field_dict["limit"] = limit
        if order_by is not UNSET:
            field_dict["order_by"] = order_by
        if last_evaluated_key is not UNSET:
            field_dict["last_evaluated_key"] = last_evaluated_key
        if search is not UNSET:
            field_dict["search"] = search
        if search_fields is not UNSET:
            field_dict["search_fields"] = search_fields
        if path_filter is not UNSET:
            field_dict["path_filter"] = path_filter
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if last_updated_by is not UNSET:
            field_dict["last_updated_by"] = last_updated_by
        if created_date is not UNSET:
            field_dict["created_date"] = created_date
        if created_date_gte is not UNSET:
            field_dict["created_date.gte"] = created_date_gte
        if created_date_lte is not UNSET:
            field_dict["created_date.lte"] = created_date_lte
        if last_updated_date is not UNSET:
            field_dict["last_updated_date"] = last_updated_date
        if last_updated_date_gte is not UNSET:
            field_dict["last_updated_date.gte"] = last_updated_date_gte
        if last_updated_date_lte is not UNSET:
            field_dict["last_updated_date.lte"] = last_updated_date_lte
        if unicode_1 is not UNSET:
            field_dict["unicode_1"] = unicode_1
        if unicode_1_sw is not UNSET:
            field_dict["unicode_1.sw"] = unicode_1_sw
        if unicode_1_contains is not UNSET:
            field_dict["unicode_1.contains"] = unicode_1_contains
        if unicode_1_gte is not UNSET:
            field_dict["unicode_1.gte"] = unicode_1_gte
        if unicode_1_lte is not UNSET:
            field_dict["unicode_1.lte"] = unicode_1_lte
        if unicode_2 is not UNSET:
            field_dict["unicode_2"] = unicode_2
        if unicode_2_sw is not UNSET:
            field_dict["unicode_2.sw"] = unicode_2_sw
        if unicode_2_contains is not UNSET:
            field_dict["unicode_2.contains"] = unicode_2_contains
        if unicode_2_gte is not UNSET:
            field_dict["unicode_2.gte"] = unicode_2_gte
        if unicode_2_lte is not UNSET:
            field_dict["unicode_2.lte"] = unicode_2_lte
        if unicode_3 is not UNSET:
            field_dict["unicode_3"] = unicode_3
        if unicode_3_sw is not UNSET:
            field_dict["unicode_3.sw"] = unicode_3_sw
        if unicode_3_contains is not UNSET:
            field_dict["unicode_3.contains"] = unicode_3_contains
        if unicode_3_gte is not UNSET:
            field_dict["unicode_3.gte"] = unicode_3_gte
        if unicode_3_lte is not UNSET:
            field_dict["unicode_3.lte"] = unicode_3_lte
        if unicode_4 is not UNSET:
            field_dict["unicode_4"] = unicode_4
        if unicode_4_sw is not UNSET:
            field_dict["unicode_4.sw"] = unicode_4_sw
        if unicode_4_contains is not UNSET:
            field_dict["unicode_4.contains"] = unicode_4_contains
        if unicode_4_gte is not UNSET:
            field_dict["unicode_4.gte"] = unicode_4_gte
        if unicode_4_lte is not UNSET:
            field_dict["unicode_4.lte"] = unicode_4_lte
        if unicode_5 is not UNSET:
            field_dict["unicode_5"] = unicode_5
        if unicode_5_sw is not UNSET:
            field_dict["unicode_5.sw"] = unicode_5_sw
        if unicode_5_contains is not UNSET:
            field_dict["unicode_5.contains"] = unicode_5_contains
        if unicode_5_gte is not UNSET:
            field_dict["unicode_5.gte"] = unicode_5_gte
        if unicode_5_lte is not UNSET:
            field_dict["unicode_5.lte"] = unicode_5_lte
        if unicode_6 is not UNSET:
            field_dict["unicode_6"] = unicode_6
        if unicode_6_sw is not UNSET:
            field_dict["unicode_6.sw"] = unicode_6_sw
        if unicode_6_contains is not UNSET:
            field_dict["unicode_6.contains"] = unicode_6_contains
        if unicode_6_gte is not UNSET:
            field_dict["unicode_6.gte"] = unicode_6_gte
        if unicode_6_lte is not UNSET:
            field_dict["unicode_6.lte"] = unicode_6_lte
        if number_1 is not UNSET:
            field_dict["number_1"] = number_1
        if number_1_gt is not UNSET:
            field_dict["number_1.gt"] = number_1_gt
        if number_1_gte is not UNSET:
            field_dict["number_1.gte"] = number_1_gte
        if number_1_lt is not UNSET:
            field_dict["number_1.lt"] = number_1_lt
        if number_1_lte is not UNSET:
            field_dict["number_1.lte"] = number_1_lte
        if number_2 is not UNSET:
            field_dict["number_2"] = number_2
        if number_2_gt is not UNSET:
            field_dict["number_2.gt"] = number_2_gt
        if number_2_gte is not UNSET:
            field_dict["number_2.gte"] = number_2_gte
        if number_2_lt is not UNSET:
            field_dict["number_2.lt"] = number_2_lt
        if number_2_lte is not UNSET:
            field_dict["number_2.lte"] = number_2_lte
        if verify is not UNSET:
            field_dict["verify"] = verify
        if unicode_7 is not UNSET:
            field_dict["unicode_7"] = unicode_7
        if unicode_7_sw is not UNSET:
            field_dict["unicode_7.sw"] = unicode_7_sw
        if unicode_7_contains is not UNSET:
            field_dict["unicode_7.contains"] = unicode_7_contains
        if unicode_7_gte is not UNSET:
            field_dict["unicode_7.gte"] = unicode_7_gte
        if unicode_7_lte is not UNSET:
            field_dict["unicode_7.lte"] = unicode_7_lte
        if unicode_8 is not UNSET:
            field_dict["unicode_8"] = unicode_8
        if unicode_8_sw is not UNSET:
            field_dict["unicode_8.sw"] = unicode_8_sw
        if unicode_8_contains is not UNSET:
            field_dict["unicode_8.contains"] = unicode_8_contains
        if unicode_8_gte is not UNSET:
            field_dict["unicode_8.gte"] = unicode_8_gte
        if unicode_8_lte is not UNSET:
            field_dict["unicode_8.lte"] = unicode_8_lte
        if unicode_9 is not UNSET:
            field_dict["unicode_9"] = unicode_9
        if unicode_9_sw is not UNSET:
            field_dict["unicode_9.sw"] = unicode_9_sw
        if unicode_9_contains is not UNSET:
            field_dict["unicode_9.contains"] = unicode_9_contains
        if unicode_9_gte is not UNSET:
            field_dict["unicode_9.gte"] = unicode_9_gte
        if unicode_9_lte is not UNSET:
            field_dict["unicode_9.lte"] = unicode_9_lte
        if unicode_10 is not UNSET:
            field_dict["unicode_10"] = unicode_10
        if unicode_10_sw is not UNSET:
            field_dict["unicode_10.sw"] = unicode_10_sw
        if unicode_10_contains is not UNSET:
            field_dict["unicode_10.contains"] = unicode_10_contains
        if unicode_10_gte is not UNSET:
            field_dict["unicode_10.gte"] = unicode_10_gte
        if unicode_10_lte is not UNSET:
            field_dict["unicode_10.lte"] = unicode_10_lte

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_data_job_last_evaluated_key_type_0 import (
            GetDataJobLastEvaluatedKeyType0,
        )

        d = src_dict.copy()
        paths = cast(List[str], d.pop("paths"))

        cascade = d.pop("cascade", UNSET)

        paths_only = d.pop("paths_only", UNSET)

        object_count = d.pop("object_count", UNSET)

        desc = d.pop("desc", UNSET)

        bust_cache = d.pop("bust_cache", UNSET)

        limit = d.pop("limit", UNSET)

        order_by = d.pop("order_by", UNSET)

        def _parse_last_evaluated_key(
            data: object,
        ) -> Union["GetDataJobLastEvaluatedKeyType0", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_evaluated_key_type_0 = GetDataJobLastEvaluatedKeyType0.from_dict(data)

                return last_evaluated_key_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GetDataJobLastEvaluatedKeyType0", Unset, str], data)

        last_evaluated_key = _parse_last_evaluated_key(d.pop("last_evaluated_key", UNSET))

        search = d.pop("search", UNSET)

        search_fields = d.pop("search_fields", UNSET)

        path_filter = d.pop("path_filter", UNSET)

        created_by = d.pop("created_by", UNSET)

        last_updated_by = d.pop("last_updated_by", UNSET)

        _created_date = d.pop("created_date", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        _created_date_gte = d.pop("created_date.gte", UNSET)
        created_date_gte: Union[Unset, datetime.datetime]
        if isinstance(_created_date_gte, Unset):
            created_date_gte = UNSET
        else:
            created_date_gte = isoparse(_created_date_gte)

        _created_date_lte = d.pop("created_date.lte", UNSET)
        created_date_lte: Union[Unset, datetime.datetime]
        if isinstance(_created_date_lte, Unset):
            created_date_lte = UNSET
        else:
            created_date_lte = isoparse(_created_date_lte)

        _last_updated_date = d.pop("last_updated_date", UNSET)
        last_updated_date: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = isoparse(_last_updated_date)

        _last_updated_date_gte = d.pop("last_updated_date.gte", UNSET)
        last_updated_date_gte: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date_gte, Unset):
            last_updated_date_gte = UNSET
        else:
            last_updated_date_gte = isoparse(_last_updated_date_gte)

        _last_updated_date_lte = d.pop("last_updated_date.lte", UNSET)
        last_updated_date_lte: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date_lte, Unset):
            last_updated_date_lte = UNSET
        else:
            last_updated_date_lte = isoparse(_last_updated_date_lte)

        unicode_1 = d.pop("unicode_1", UNSET)

        unicode_1_sw = d.pop("unicode_1.sw", UNSET)

        unicode_1_contains = d.pop("unicode_1.contains", UNSET)

        unicode_1_gte = d.pop("unicode_1.gte", UNSET)

        unicode_1_lte = d.pop("unicode_1.lte", UNSET)

        unicode_2 = d.pop("unicode_2", UNSET)

        unicode_2_sw = d.pop("unicode_2.sw", UNSET)

        unicode_2_contains = d.pop("unicode_2.contains", UNSET)

        unicode_2_gte = d.pop("unicode_2.gte", UNSET)

        unicode_2_lte = d.pop("unicode_2.lte", UNSET)

        unicode_3 = d.pop("unicode_3", UNSET)

        unicode_3_sw = d.pop("unicode_3.sw", UNSET)

        unicode_3_contains = d.pop("unicode_3.contains", UNSET)

        unicode_3_gte = d.pop("unicode_3.gte", UNSET)

        unicode_3_lte = d.pop("unicode_3.lte", UNSET)

        unicode_4 = d.pop("unicode_4", UNSET)

        unicode_4_sw = d.pop("unicode_4.sw", UNSET)

        unicode_4_contains = d.pop("unicode_4.contains", UNSET)

        unicode_4_gte = d.pop("unicode_4.gte", UNSET)

        unicode_4_lte = d.pop("unicode_4.lte", UNSET)

        unicode_5 = d.pop("unicode_5", UNSET)

        unicode_5_sw = d.pop("unicode_5.sw", UNSET)

        unicode_5_contains = d.pop("unicode_5.contains", UNSET)

        unicode_5_gte = d.pop("unicode_5.gte", UNSET)

        unicode_5_lte = d.pop("unicode_5.lte", UNSET)

        unicode_6 = d.pop("unicode_6", UNSET)

        unicode_6_sw = d.pop("unicode_6.sw", UNSET)

        unicode_6_contains = d.pop("unicode_6.contains", UNSET)

        unicode_6_gte = d.pop("unicode_6.gte", UNSET)

        unicode_6_lte = d.pop("unicode_6.lte", UNSET)

        number_1 = d.pop("number_1", UNSET)

        number_1_gt = d.pop("number_1.gt", UNSET)

        number_1_gte = d.pop("number_1.gte", UNSET)

        number_1_lt = d.pop("number_1.lt", UNSET)

        number_1_lte = d.pop("number_1.lte", UNSET)

        number_2 = d.pop("number_2", UNSET)

        number_2_gt = d.pop("number_2.gt", UNSET)

        number_2_gte = d.pop("number_2.gte", UNSET)

        number_2_lt = d.pop("number_2.lt", UNSET)

        number_2_lte = d.pop("number_2.lte", UNSET)

        verify = d.pop("verify", UNSET)

        unicode_7 = d.pop("unicode_7", UNSET)

        unicode_7_sw = d.pop("unicode_7.sw", UNSET)

        unicode_7_contains = d.pop("unicode_7.contains", UNSET)

        unicode_7_gte = d.pop("unicode_7.gte", UNSET)

        unicode_7_lte = d.pop("unicode_7.lte", UNSET)

        unicode_8 = d.pop("unicode_8", UNSET)

        unicode_8_sw = d.pop("unicode_8.sw", UNSET)

        unicode_8_contains = d.pop("unicode_8.contains", UNSET)

        unicode_8_gte = d.pop("unicode_8.gte", UNSET)

        unicode_8_lte = d.pop("unicode_8.lte", UNSET)

        unicode_9 = d.pop("unicode_9", UNSET)

        unicode_9_sw = d.pop("unicode_9.sw", UNSET)

        unicode_9_contains = d.pop("unicode_9.contains", UNSET)

        unicode_9_gte = d.pop("unicode_9.gte", UNSET)

        unicode_9_lte = d.pop("unicode_9.lte", UNSET)

        unicode_10 = d.pop("unicode_10", UNSET)

        unicode_10_sw = d.pop("unicode_10.sw", UNSET)

        unicode_10_contains = d.pop("unicode_10.contains", UNSET)

        unicode_10_gte = d.pop("unicode_10.gte", UNSET)

        unicode_10_lte = d.pop("unicode_10.lte", UNSET)

        get_data_job = cls(
            paths=paths,
            cascade=cascade,
            paths_only=paths_only,
            object_count=object_count,
            desc=desc,
            bust_cache=bust_cache,
            limit=limit,
            order_by=order_by,
            last_evaluated_key=last_evaluated_key,
            search=search,
            search_fields=search_fields,
            path_filter=path_filter,
            created_by=created_by,
            last_updated_by=last_updated_by,
            created_date=created_date,
            created_date_gte=created_date_gte,
            created_date_lte=created_date_lte,
            last_updated_date=last_updated_date,
            last_updated_date_gte=last_updated_date_gte,
            last_updated_date_lte=last_updated_date_lte,
            unicode_1=unicode_1,
            unicode_1_sw=unicode_1_sw,
            unicode_1_contains=unicode_1_contains,
            unicode_1_gte=unicode_1_gte,
            unicode_1_lte=unicode_1_lte,
            unicode_2=unicode_2,
            unicode_2_sw=unicode_2_sw,
            unicode_2_contains=unicode_2_contains,
            unicode_2_gte=unicode_2_gte,
            unicode_2_lte=unicode_2_lte,
            unicode_3=unicode_3,
            unicode_3_sw=unicode_3_sw,
            unicode_3_contains=unicode_3_contains,
            unicode_3_gte=unicode_3_gte,
            unicode_3_lte=unicode_3_lte,
            unicode_4=unicode_4,
            unicode_4_sw=unicode_4_sw,
            unicode_4_contains=unicode_4_contains,
            unicode_4_gte=unicode_4_gte,
            unicode_4_lte=unicode_4_lte,
            unicode_5=unicode_5,
            unicode_5_sw=unicode_5_sw,
            unicode_5_contains=unicode_5_contains,
            unicode_5_gte=unicode_5_gte,
            unicode_5_lte=unicode_5_lte,
            unicode_6=unicode_6,
            unicode_6_sw=unicode_6_sw,
            unicode_6_contains=unicode_6_contains,
            unicode_6_gte=unicode_6_gte,
            unicode_6_lte=unicode_6_lte,
            number_1=number_1,
            number_1_gt=number_1_gt,
            number_1_gte=number_1_gte,
            number_1_lt=number_1_lt,
            number_1_lte=number_1_lte,
            number_2=number_2,
            number_2_gt=number_2_gt,
            number_2_gte=number_2_gte,
            number_2_lt=number_2_lt,
            number_2_lte=number_2_lte,
            verify=verify,
            unicode_7=unicode_7,
            unicode_7_sw=unicode_7_sw,
            unicode_7_contains=unicode_7_contains,
            unicode_7_gte=unicode_7_gte,
            unicode_7_lte=unicode_7_lte,
            unicode_8=unicode_8,
            unicode_8_sw=unicode_8_sw,
            unicode_8_contains=unicode_8_contains,
            unicode_8_gte=unicode_8_gte,
            unicode_8_lte=unicode_8_lte,
            unicode_9=unicode_9,
            unicode_9_sw=unicode_9_sw,
            unicode_9_contains=unicode_9_contains,
            unicode_9_gte=unicode_9_gte,
            unicode_9_lte=unicode_9_lte,
            unicode_10=unicode_10,
            unicode_10_sw=unicode_10_sw,
            unicode_10_contains=unicode_10_contains,
            unicode_10_gte=unicode_10_gte,
            unicode_10_lte=unicode_10_lte,
        )

        get_data_job.additional_properties = d
        return get_data_job

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
