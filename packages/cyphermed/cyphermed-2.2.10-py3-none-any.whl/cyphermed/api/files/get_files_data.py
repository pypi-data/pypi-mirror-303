import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.files_at_path import FilesAtPath
from ...models.get_files_data_last_evaluated_key_type_0 import (
    GetFilesDataLastEvaluatedKeyType0,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: str,
    path: str,
    *,
    cascade: Union[Unset, bool] = UNSET,
    paths_only: Union[Unset, bool] = UNSET,
    object_count: Union[Unset, bool] = UNSET,
    desc: Union[Unset, bool] = UNSET,
    bust_cache: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 100,
    order_by: Union[Unset, str] = UNSET,
    last_evaluated_key: Union["GetFilesDataLastEvaluatedKeyType0", Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    search_fields: Union[Unset, str] = UNSET,
    path_filter: Union[Unset, str] = UNSET,
    created_by: Union[Unset, str] = UNSET,
    last_updated_by: Union[Unset, str] = UNSET,
    created_date: Union[Unset, datetime.datetime] = UNSET,
    created_date_gte: Union[Unset, datetime.datetime] = UNSET,
    created_date_lte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_gte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_lte: Union[Unset, datetime.datetime] = UNSET,
    unicode_1: Union[Unset, str] = UNSET,
    unicode_1_sw: Union[Unset, str] = UNSET,
    unicode_1_contains: Union[Unset, str] = UNSET,
    unicode_1_gte: Union[Unset, str] = UNSET,
    unicode_1_lte: Union[Unset, str] = UNSET,
    unicode_2: Union[Unset, str] = UNSET,
    unicode_2_sw: Union[Unset, str] = UNSET,
    unicode_2_contains: Union[Unset, str] = UNSET,
    unicode_2_gte: Union[Unset, str] = UNSET,
    unicode_2_lte: Union[Unset, str] = UNSET,
    unicode_3: Union[Unset, str] = UNSET,
    unicode_3_sw: Union[Unset, str] = UNSET,
    unicode_3_contains: Union[Unset, str] = UNSET,
    unicode_3_gte: Union[Unset, str] = UNSET,
    unicode_3_lte: Union[Unset, str] = UNSET,
    unicode_4: Union[Unset, str] = UNSET,
    unicode_4_sw: Union[Unset, str] = UNSET,
    unicode_4_contains: Union[Unset, str] = UNSET,
    unicode_4_gte: Union[Unset, str] = UNSET,
    unicode_4_lte: Union[Unset, str] = UNSET,
    unicode_5: Union[Unset, str] = UNSET,
    unicode_5_sw: Union[Unset, str] = UNSET,
    unicode_5_contains: Union[Unset, str] = UNSET,
    unicode_5_gte: Union[Unset, str] = UNSET,
    unicode_5_lte: Union[Unset, str] = UNSET,
    unicode_6: Union[Unset, str] = UNSET,
    unicode_6_sw: Union[Unset, str] = UNSET,
    unicode_6_contains: Union[Unset, str] = UNSET,
    unicode_6_gte: Union[Unset, str] = UNSET,
    unicode_6_lte: Union[Unset, str] = UNSET,
    number_1: Union[Unset, float] = UNSET,
    number_1_gt: Union[Unset, float] = UNSET,
    number_1_gte: Union[Unset, float] = UNSET,
    number_1_lt: Union[Unset, float] = UNSET,
    number_1_lte: Union[Unset, float] = UNSET,
    number_2: Union[Unset, float] = UNSET,
    number_2_gt: Union[Unset, float] = UNSET,
    number_2_gte: Union[Unset, float] = UNSET,
    number_2_lt: Union[Unset, float] = UNSET,
    number_2_lte: Union[Unset, float] = UNSET,
    redirect: Union[Unset, bool] = UNSET,
    url_only: Union[Unset, bool] = UNSET,
    info_only: Union[Unset, bool] = UNSET,
    expires_in: Union[Unset, int] = UNSET,
    uploaded_date: Union[Unset, datetime.datetime] = UNSET,
    uploaded_date_gte: Union[Unset, datetime.datetime] = UNSET,
    uploaded_date_lte: Union[Unset, datetime.datetime] = UNSET,
    size: Union[Unset, int] = UNSET,
    size_gt: Union[Unset, float] = UNSET,
    size_gte: Union[Unset, float] = UNSET,
    size_lt: Union[Unset, float] = UNSET,
    size_lte: Union[Unset, float] = UNSET,
    filename: Union[Unset, str] = UNSET,
    filename_sw: Union[Unset, str] = UNSET,
    filename_contains: Union[Unset, str] = UNSET,
    etag: Union[Unset, str] = UNSET,
    etag_sw: Union[Unset, str] = UNSET,
    etag_contains: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["cascade"] = cascade

    params["paths_only"] = paths_only

    params["object_count"] = object_count

    params["desc"] = desc

    params["bust_cache"] = bust_cache

    params["limit"] = limit

    params["order_by"] = order_by

    json_last_evaluated_key: Union[Dict[str, Any], Unset, str]
    if isinstance(last_evaluated_key, Unset):
        json_last_evaluated_key = UNSET
    elif isinstance(last_evaluated_key, GetFilesDataLastEvaluatedKeyType0):
        json_last_evaluated_key = last_evaluated_key.to_dict()
    else:
        json_last_evaluated_key = last_evaluated_key
    params["last_evaluated_key"] = json_last_evaluated_key

    params["search"] = search

    params["search_fields"] = search_fields

    params["path_filter"] = path_filter

    params["created_by"] = created_by

    params["last_updated_by"] = last_updated_by

    json_created_date: Union[Unset, str] = UNSET
    if not isinstance(created_date, Unset):
        json_created_date = created_date.isoformat()
    params["created_date"] = json_created_date

    json_created_date_gte: Union[Unset, str] = UNSET
    if not isinstance(created_date_gte, Unset):
        json_created_date_gte = created_date_gte.isoformat()
    params["created_date.gte"] = json_created_date_gte

    json_created_date_lte: Union[Unset, str] = UNSET
    if not isinstance(created_date_lte, Unset):
        json_created_date_lte = created_date_lte.isoformat()
    params["created_date.lte"] = json_created_date_lte

    json_last_updated_date: Union[Unset, str] = UNSET
    if not isinstance(last_updated_date, Unset):
        json_last_updated_date = last_updated_date.isoformat()
    params["last_updated_date"] = json_last_updated_date

    json_last_updated_date_gte: Union[Unset, str] = UNSET
    if not isinstance(last_updated_date_gte, Unset):
        json_last_updated_date_gte = last_updated_date_gte.isoformat()
    params["last_updated_date.gte"] = json_last_updated_date_gte

    json_last_updated_date_lte: Union[Unset, str] = UNSET
    if not isinstance(last_updated_date_lte, Unset):
        json_last_updated_date_lte = last_updated_date_lte.isoformat()
    params["last_updated_date.lte"] = json_last_updated_date_lte

    params["unicode_1"] = unicode_1

    params["unicode_1.sw"] = unicode_1_sw

    params["unicode_1.contains"] = unicode_1_contains

    params["unicode_1.gte"] = unicode_1_gte

    params["unicode_1.lte"] = unicode_1_lte

    params["unicode_2"] = unicode_2

    params["unicode_2.sw"] = unicode_2_sw

    params["unicode_2.contains"] = unicode_2_contains

    params["unicode_2.gte"] = unicode_2_gte

    params["unicode_2.lte"] = unicode_2_lte

    params["unicode_3"] = unicode_3

    params["unicode_3.sw"] = unicode_3_sw

    params["unicode_3.contains"] = unicode_3_contains

    params["unicode_3.gte"] = unicode_3_gte

    params["unicode_3.lte"] = unicode_3_lte

    params["unicode_4"] = unicode_4

    params["unicode_4.sw"] = unicode_4_sw

    params["unicode_4.contains"] = unicode_4_contains

    params["unicode_4.gte"] = unicode_4_gte

    params["unicode_4.lte"] = unicode_4_lte

    params["unicode_5"] = unicode_5

    params["unicode_5.sw"] = unicode_5_sw

    params["unicode_5.contains"] = unicode_5_contains

    params["unicode_5.gte"] = unicode_5_gte

    params["unicode_5.lte"] = unicode_5_lte

    params["unicode_6"] = unicode_6

    params["unicode_6.sw"] = unicode_6_sw

    params["unicode_6.contains"] = unicode_6_contains

    params["unicode_6.gte"] = unicode_6_gte

    params["unicode_6.lte"] = unicode_6_lte

    params["number_1"] = number_1

    params["number_1.gt"] = number_1_gt

    params["number_1.gte"] = number_1_gte

    params["number_1.lt"] = number_1_lt

    params["number_1.lte"] = number_1_lte

    params["number_2"] = number_2

    params["number_2.gt"] = number_2_gt

    params["number_2.gte"] = number_2_gte

    params["number_2.lt"] = number_2_lt

    params["number_2.lte"] = number_2_lte

    params["redirect"] = redirect

    params["url_only"] = url_only

    params["info_only"] = info_only

    params["expires_in"] = expires_in

    json_uploaded_date: Union[Unset, str] = UNSET
    if not isinstance(uploaded_date, Unset):
        json_uploaded_date = uploaded_date.isoformat()
    params["uploaded_date"] = json_uploaded_date

    json_uploaded_date_gte: Union[Unset, str] = UNSET
    if not isinstance(uploaded_date_gte, Unset):
        json_uploaded_date_gte = uploaded_date_gte.isoformat()
    params["uploaded_date.gte"] = json_uploaded_date_gte

    json_uploaded_date_lte: Union[Unset, str] = UNSET
    if not isinstance(uploaded_date_lte, Unset):
        json_uploaded_date_lte = uploaded_date_lte.isoformat()
    params["uploaded_date.lte"] = json_uploaded_date_lte

    params["size"] = size

    params["size.gt"] = size_gt

    params["size.gte"] = size_gte

    params["size.lt"] = size_lt

    params["size.lte"] = size_lte

    params["filename"] = filename

    params["filename.sw"] = filename_sw

    params["filename.contains"] = filename_contains

    params["etag"] = etag

    params["etag.sw"] = etag_sw

    params["etag.contains"] = etag_contains

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/groups/{group_id}/files/{path}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, FilesAtPath]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FilesAtPath.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.PERMANENT_REDIRECT:
        response_308 = cast(Any, None)
        return response_308
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, FilesAtPath]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
    cascade: Union[Unset, bool] = UNSET,
    paths_only: Union[Unset, bool] = UNSET,
    object_count: Union[Unset, bool] = UNSET,
    desc: Union[Unset, bool] = UNSET,
    bust_cache: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 100,
    order_by: Union[Unset, str] = UNSET,
    last_evaluated_key: Union["GetFilesDataLastEvaluatedKeyType0", Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    search_fields: Union[Unset, str] = UNSET,
    path_filter: Union[Unset, str] = UNSET,
    created_by: Union[Unset, str] = UNSET,
    last_updated_by: Union[Unset, str] = UNSET,
    created_date: Union[Unset, datetime.datetime] = UNSET,
    created_date_gte: Union[Unset, datetime.datetime] = UNSET,
    created_date_lte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_gte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_lte: Union[Unset, datetime.datetime] = UNSET,
    unicode_1: Union[Unset, str] = UNSET,
    unicode_1_sw: Union[Unset, str] = UNSET,
    unicode_1_contains: Union[Unset, str] = UNSET,
    unicode_1_gte: Union[Unset, str] = UNSET,
    unicode_1_lte: Union[Unset, str] = UNSET,
    unicode_2: Union[Unset, str] = UNSET,
    unicode_2_sw: Union[Unset, str] = UNSET,
    unicode_2_contains: Union[Unset, str] = UNSET,
    unicode_2_gte: Union[Unset, str] = UNSET,
    unicode_2_lte: Union[Unset, str] = UNSET,
    unicode_3: Union[Unset, str] = UNSET,
    unicode_3_sw: Union[Unset, str] = UNSET,
    unicode_3_contains: Union[Unset, str] = UNSET,
    unicode_3_gte: Union[Unset, str] = UNSET,
    unicode_3_lte: Union[Unset, str] = UNSET,
    unicode_4: Union[Unset, str] = UNSET,
    unicode_4_sw: Union[Unset, str] = UNSET,
    unicode_4_contains: Union[Unset, str] = UNSET,
    unicode_4_gte: Union[Unset, str] = UNSET,
    unicode_4_lte: Union[Unset, str] = UNSET,
    unicode_5: Union[Unset, str] = UNSET,
    unicode_5_sw: Union[Unset, str] = UNSET,
    unicode_5_contains: Union[Unset, str] = UNSET,
    unicode_5_gte: Union[Unset, str] = UNSET,
    unicode_5_lte: Union[Unset, str] = UNSET,
    unicode_6: Union[Unset, str] = UNSET,
    unicode_6_sw: Union[Unset, str] = UNSET,
    unicode_6_contains: Union[Unset, str] = UNSET,
    unicode_6_gte: Union[Unset, str] = UNSET,
    unicode_6_lte: Union[Unset, str] = UNSET,
    number_1: Union[Unset, float] = UNSET,
    number_1_gt: Union[Unset, float] = UNSET,
    number_1_gte: Union[Unset, float] = UNSET,
    number_1_lt: Union[Unset, float] = UNSET,
    number_1_lte: Union[Unset, float] = UNSET,
    number_2: Union[Unset, float] = UNSET,
    number_2_gt: Union[Unset, float] = UNSET,
    number_2_gte: Union[Unset, float] = UNSET,
    number_2_lt: Union[Unset, float] = UNSET,
    number_2_lte: Union[Unset, float] = UNSET,
    redirect: Union[Unset, bool] = UNSET,
    url_only: Union[Unset, bool] = UNSET,
    info_only: Union[Unset, bool] = UNSET,
    expires_in: Union[Unset, int] = UNSET,
    uploaded_date: Union[Unset, datetime.datetime] = UNSET,
    uploaded_date_gte: Union[Unset, datetime.datetime] = UNSET,
    uploaded_date_lte: Union[Unset, datetime.datetime] = UNSET,
    size: Union[Unset, int] = UNSET,
    size_gt: Union[Unset, float] = UNSET,
    size_gte: Union[Unset, float] = UNSET,
    size_lt: Union[Unset, float] = UNSET,
    size_lte: Union[Unset, float] = UNSET,
    filename: Union[Unset, str] = UNSET,
    filename_sw: Union[Unset, str] = UNSET,
    filename_contains: Union[Unset, str] = UNSET,
    etag: Union[Unset, str] = UNSET,
    etag_sw: Union[Unset, str] = UNSET,
    etag_contains: Union[Unset, str] = UNSET,
) -> Response[Union[Any, FilesAtPath]]:
    """Get Files Data

     Get a files info and/or presigned GET URLs by group ID and path

    Args:
        group_id (str):
        path (str):
        cascade (Union[Unset, bool]): If true, return all paths starting with the specified path
        paths_only (Union[Unset, bool]): If true, only return list of matching file paths
        object_count (Union[Unset, bool]): If true, only return the number of objects in the file
        desc (Union[Unset, bool]): Whether to order results in descending order
        bust_cache (Union[Unset, bool]): Whether to bypass the cache and get the latest data
        limit (Union[Unset, int]): Maximum number of results to return Default: 100.
        order_by (Union[Unset, str]): Field to order results by
        last_evaluated_key (Union['GetFilesDataLastEvaluatedKeyType0', Unset,
            str]): Key to start results from
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
        redirect (Union[Unset, bool]): If true, redirect to presigned GET URL
        url_only (Union[Unset, bool]): If true, only return a list of presigned GET URLs
        info_only (Union[Unset, bool]): If true, only return file info (includes paths)
        expires_in (Union[Unset, int]): Number of seconds before presigned URLs expire
        uploaded_date (Union[Unset, datetime.datetime]): Uploaded date of files to return
        uploaded_date_gte (Union[Unset, datetime.datetime]):
        uploaded_date_lte (Union[Unset, datetime.datetime]):
        size (Union[Unset, int]): Size of file in bytes
        size_gt (Union[Unset, float]):
        size_gte (Union[Unset, float]):
        size_lt (Union[Unset, float]):
        size_lte (Union[Unset, float]):
        filename (Union[Unset, str]): Filename of file
        filename_sw (Union[Unset, str]):
        filename_contains (Union[Unset, str]):
        etag (Union[Unset, str]): ETag of file
        etag_sw (Union[Unset, str]):
        etag_contains (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FilesAtPath]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        path=path,
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
        redirect=redirect,
        url_only=url_only,
        info_only=info_only,
        expires_in=expires_in,
        uploaded_date=uploaded_date,
        uploaded_date_gte=uploaded_date_gte,
        uploaded_date_lte=uploaded_date_lte,
        size=size,
        size_gt=size_gt,
        size_gte=size_gte,
        size_lt=size_lt,
        size_lte=size_lte,
        filename=filename,
        filename_sw=filename_sw,
        filename_contains=filename_contains,
        etag=etag,
        etag_sw=etag_sw,
        etag_contains=etag_contains,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
    cascade: Union[Unset, bool] = UNSET,
    paths_only: Union[Unset, bool] = UNSET,
    object_count: Union[Unset, bool] = UNSET,
    desc: Union[Unset, bool] = UNSET,
    bust_cache: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 100,
    order_by: Union[Unset, str] = UNSET,
    last_evaluated_key: Union["GetFilesDataLastEvaluatedKeyType0", Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    search_fields: Union[Unset, str] = UNSET,
    path_filter: Union[Unset, str] = UNSET,
    created_by: Union[Unset, str] = UNSET,
    last_updated_by: Union[Unset, str] = UNSET,
    created_date: Union[Unset, datetime.datetime] = UNSET,
    created_date_gte: Union[Unset, datetime.datetime] = UNSET,
    created_date_lte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_gte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_lte: Union[Unset, datetime.datetime] = UNSET,
    unicode_1: Union[Unset, str] = UNSET,
    unicode_1_sw: Union[Unset, str] = UNSET,
    unicode_1_contains: Union[Unset, str] = UNSET,
    unicode_1_gte: Union[Unset, str] = UNSET,
    unicode_1_lte: Union[Unset, str] = UNSET,
    unicode_2: Union[Unset, str] = UNSET,
    unicode_2_sw: Union[Unset, str] = UNSET,
    unicode_2_contains: Union[Unset, str] = UNSET,
    unicode_2_gte: Union[Unset, str] = UNSET,
    unicode_2_lte: Union[Unset, str] = UNSET,
    unicode_3: Union[Unset, str] = UNSET,
    unicode_3_sw: Union[Unset, str] = UNSET,
    unicode_3_contains: Union[Unset, str] = UNSET,
    unicode_3_gte: Union[Unset, str] = UNSET,
    unicode_3_lte: Union[Unset, str] = UNSET,
    unicode_4: Union[Unset, str] = UNSET,
    unicode_4_sw: Union[Unset, str] = UNSET,
    unicode_4_contains: Union[Unset, str] = UNSET,
    unicode_4_gte: Union[Unset, str] = UNSET,
    unicode_4_lte: Union[Unset, str] = UNSET,
    unicode_5: Union[Unset, str] = UNSET,
    unicode_5_sw: Union[Unset, str] = UNSET,
    unicode_5_contains: Union[Unset, str] = UNSET,
    unicode_5_gte: Union[Unset, str] = UNSET,
    unicode_5_lte: Union[Unset, str] = UNSET,
    unicode_6: Union[Unset, str] = UNSET,
    unicode_6_sw: Union[Unset, str] = UNSET,
    unicode_6_contains: Union[Unset, str] = UNSET,
    unicode_6_gte: Union[Unset, str] = UNSET,
    unicode_6_lte: Union[Unset, str] = UNSET,
    number_1: Union[Unset, float] = UNSET,
    number_1_gt: Union[Unset, float] = UNSET,
    number_1_gte: Union[Unset, float] = UNSET,
    number_1_lt: Union[Unset, float] = UNSET,
    number_1_lte: Union[Unset, float] = UNSET,
    number_2: Union[Unset, float] = UNSET,
    number_2_gt: Union[Unset, float] = UNSET,
    number_2_gte: Union[Unset, float] = UNSET,
    number_2_lt: Union[Unset, float] = UNSET,
    number_2_lte: Union[Unset, float] = UNSET,
    redirect: Union[Unset, bool] = UNSET,
    url_only: Union[Unset, bool] = UNSET,
    info_only: Union[Unset, bool] = UNSET,
    expires_in: Union[Unset, int] = UNSET,
    uploaded_date: Union[Unset, datetime.datetime] = UNSET,
    uploaded_date_gte: Union[Unset, datetime.datetime] = UNSET,
    uploaded_date_lte: Union[Unset, datetime.datetime] = UNSET,
    size: Union[Unset, int] = UNSET,
    size_gt: Union[Unset, float] = UNSET,
    size_gte: Union[Unset, float] = UNSET,
    size_lt: Union[Unset, float] = UNSET,
    size_lte: Union[Unset, float] = UNSET,
    filename: Union[Unset, str] = UNSET,
    filename_sw: Union[Unset, str] = UNSET,
    filename_contains: Union[Unset, str] = UNSET,
    etag: Union[Unset, str] = UNSET,
    etag_sw: Union[Unset, str] = UNSET,
    etag_contains: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, FilesAtPath]]:
    """Get Files Data

     Get a files info and/or presigned GET URLs by group ID and path

    Args:
        group_id (str):
        path (str):
        cascade (Union[Unset, bool]): If true, return all paths starting with the specified path
        paths_only (Union[Unset, bool]): If true, only return list of matching file paths
        object_count (Union[Unset, bool]): If true, only return the number of objects in the file
        desc (Union[Unset, bool]): Whether to order results in descending order
        bust_cache (Union[Unset, bool]): Whether to bypass the cache and get the latest data
        limit (Union[Unset, int]): Maximum number of results to return Default: 100.
        order_by (Union[Unset, str]): Field to order results by
        last_evaluated_key (Union['GetFilesDataLastEvaluatedKeyType0', Unset,
            str]): Key to start results from
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
        redirect (Union[Unset, bool]): If true, redirect to presigned GET URL
        url_only (Union[Unset, bool]): If true, only return a list of presigned GET URLs
        info_only (Union[Unset, bool]): If true, only return file info (includes paths)
        expires_in (Union[Unset, int]): Number of seconds before presigned URLs expire
        uploaded_date (Union[Unset, datetime.datetime]): Uploaded date of files to return
        uploaded_date_gte (Union[Unset, datetime.datetime]):
        uploaded_date_lte (Union[Unset, datetime.datetime]):
        size (Union[Unset, int]): Size of file in bytes
        size_gt (Union[Unset, float]):
        size_gte (Union[Unset, float]):
        size_lt (Union[Unset, float]):
        size_lte (Union[Unset, float]):
        filename (Union[Unset, str]): Filename of file
        filename_sw (Union[Unset, str]):
        filename_contains (Union[Unset, str]):
        etag (Union[Unset, str]): ETag of file
        etag_sw (Union[Unset, str]):
        etag_contains (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FilesAtPath]
    """

    return sync_detailed(
        group_id=group_id,
        path=path,
        client=client,
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
        redirect=redirect,
        url_only=url_only,
        info_only=info_only,
        expires_in=expires_in,
        uploaded_date=uploaded_date,
        uploaded_date_gte=uploaded_date_gte,
        uploaded_date_lte=uploaded_date_lte,
        size=size,
        size_gt=size_gt,
        size_gte=size_gte,
        size_lt=size_lt,
        size_lte=size_lte,
        filename=filename,
        filename_sw=filename_sw,
        filename_contains=filename_contains,
        etag=etag,
        etag_sw=etag_sw,
        etag_contains=etag_contains,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
    cascade: Union[Unset, bool] = UNSET,
    paths_only: Union[Unset, bool] = UNSET,
    object_count: Union[Unset, bool] = UNSET,
    desc: Union[Unset, bool] = UNSET,
    bust_cache: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 100,
    order_by: Union[Unset, str] = UNSET,
    last_evaluated_key: Union["GetFilesDataLastEvaluatedKeyType0", Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    search_fields: Union[Unset, str] = UNSET,
    path_filter: Union[Unset, str] = UNSET,
    created_by: Union[Unset, str] = UNSET,
    last_updated_by: Union[Unset, str] = UNSET,
    created_date: Union[Unset, datetime.datetime] = UNSET,
    created_date_gte: Union[Unset, datetime.datetime] = UNSET,
    created_date_lte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_gte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_lte: Union[Unset, datetime.datetime] = UNSET,
    unicode_1: Union[Unset, str] = UNSET,
    unicode_1_sw: Union[Unset, str] = UNSET,
    unicode_1_contains: Union[Unset, str] = UNSET,
    unicode_1_gte: Union[Unset, str] = UNSET,
    unicode_1_lte: Union[Unset, str] = UNSET,
    unicode_2: Union[Unset, str] = UNSET,
    unicode_2_sw: Union[Unset, str] = UNSET,
    unicode_2_contains: Union[Unset, str] = UNSET,
    unicode_2_gte: Union[Unset, str] = UNSET,
    unicode_2_lte: Union[Unset, str] = UNSET,
    unicode_3: Union[Unset, str] = UNSET,
    unicode_3_sw: Union[Unset, str] = UNSET,
    unicode_3_contains: Union[Unset, str] = UNSET,
    unicode_3_gte: Union[Unset, str] = UNSET,
    unicode_3_lte: Union[Unset, str] = UNSET,
    unicode_4: Union[Unset, str] = UNSET,
    unicode_4_sw: Union[Unset, str] = UNSET,
    unicode_4_contains: Union[Unset, str] = UNSET,
    unicode_4_gte: Union[Unset, str] = UNSET,
    unicode_4_lte: Union[Unset, str] = UNSET,
    unicode_5: Union[Unset, str] = UNSET,
    unicode_5_sw: Union[Unset, str] = UNSET,
    unicode_5_contains: Union[Unset, str] = UNSET,
    unicode_5_gte: Union[Unset, str] = UNSET,
    unicode_5_lte: Union[Unset, str] = UNSET,
    unicode_6: Union[Unset, str] = UNSET,
    unicode_6_sw: Union[Unset, str] = UNSET,
    unicode_6_contains: Union[Unset, str] = UNSET,
    unicode_6_gte: Union[Unset, str] = UNSET,
    unicode_6_lte: Union[Unset, str] = UNSET,
    number_1: Union[Unset, float] = UNSET,
    number_1_gt: Union[Unset, float] = UNSET,
    number_1_gte: Union[Unset, float] = UNSET,
    number_1_lt: Union[Unset, float] = UNSET,
    number_1_lte: Union[Unset, float] = UNSET,
    number_2: Union[Unset, float] = UNSET,
    number_2_gt: Union[Unset, float] = UNSET,
    number_2_gte: Union[Unset, float] = UNSET,
    number_2_lt: Union[Unset, float] = UNSET,
    number_2_lte: Union[Unset, float] = UNSET,
    redirect: Union[Unset, bool] = UNSET,
    url_only: Union[Unset, bool] = UNSET,
    info_only: Union[Unset, bool] = UNSET,
    expires_in: Union[Unset, int] = UNSET,
    uploaded_date: Union[Unset, datetime.datetime] = UNSET,
    uploaded_date_gte: Union[Unset, datetime.datetime] = UNSET,
    uploaded_date_lte: Union[Unset, datetime.datetime] = UNSET,
    size: Union[Unset, int] = UNSET,
    size_gt: Union[Unset, float] = UNSET,
    size_gte: Union[Unset, float] = UNSET,
    size_lt: Union[Unset, float] = UNSET,
    size_lte: Union[Unset, float] = UNSET,
    filename: Union[Unset, str] = UNSET,
    filename_sw: Union[Unset, str] = UNSET,
    filename_contains: Union[Unset, str] = UNSET,
    etag: Union[Unset, str] = UNSET,
    etag_sw: Union[Unset, str] = UNSET,
    etag_contains: Union[Unset, str] = UNSET,
) -> Response[Union[Any, FilesAtPath]]:
    """Get Files Data

     Get a files info and/or presigned GET URLs by group ID and path

    Args:
        group_id (str):
        path (str):
        cascade (Union[Unset, bool]): If true, return all paths starting with the specified path
        paths_only (Union[Unset, bool]): If true, only return list of matching file paths
        object_count (Union[Unset, bool]): If true, only return the number of objects in the file
        desc (Union[Unset, bool]): Whether to order results in descending order
        bust_cache (Union[Unset, bool]): Whether to bypass the cache and get the latest data
        limit (Union[Unset, int]): Maximum number of results to return Default: 100.
        order_by (Union[Unset, str]): Field to order results by
        last_evaluated_key (Union['GetFilesDataLastEvaluatedKeyType0', Unset,
            str]): Key to start results from
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
        redirect (Union[Unset, bool]): If true, redirect to presigned GET URL
        url_only (Union[Unset, bool]): If true, only return a list of presigned GET URLs
        info_only (Union[Unset, bool]): If true, only return file info (includes paths)
        expires_in (Union[Unset, int]): Number of seconds before presigned URLs expire
        uploaded_date (Union[Unset, datetime.datetime]): Uploaded date of files to return
        uploaded_date_gte (Union[Unset, datetime.datetime]):
        uploaded_date_lte (Union[Unset, datetime.datetime]):
        size (Union[Unset, int]): Size of file in bytes
        size_gt (Union[Unset, float]):
        size_gte (Union[Unset, float]):
        size_lt (Union[Unset, float]):
        size_lte (Union[Unset, float]):
        filename (Union[Unset, str]): Filename of file
        filename_sw (Union[Unset, str]):
        filename_contains (Union[Unset, str]):
        etag (Union[Unset, str]): ETag of file
        etag_sw (Union[Unset, str]):
        etag_contains (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FilesAtPath]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        path=path,
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
        redirect=redirect,
        url_only=url_only,
        info_only=info_only,
        expires_in=expires_in,
        uploaded_date=uploaded_date,
        uploaded_date_gte=uploaded_date_gte,
        uploaded_date_lte=uploaded_date_lte,
        size=size,
        size_gt=size_gt,
        size_gte=size_gte,
        size_lt=size_lt,
        size_lte=size_lte,
        filename=filename,
        filename_sw=filename_sw,
        filename_contains=filename_contains,
        etag=etag,
        etag_sw=etag_sw,
        etag_contains=etag_contains,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
    cascade: Union[Unset, bool] = UNSET,
    paths_only: Union[Unset, bool] = UNSET,
    object_count: Union[Unset, bool] = UNSET,
    desc: Union[Unset, bool] = UNSET,
    bust_cache: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 100,
    order_by: Union[Unset, str] = UNSET,
    last_evaluated_key: Union["GetFilesDataLastEvaluatedKeyType0", Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    search_fields: Union[Unset, str] = UNSET,
    path_filter: Union[Unset, str] = UNSET,
    created_by: Union[Unset, str] = UNSET,
    last_updated_by: Union[Unset, str] = UNSET,
    created_date: Union[Unset, datetime.datetime] = UNSET,
    created_date_gte: Union[Unset, datetime.datetime] = UNSET,
    created_date_lte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_gte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_lte: Union[Unset, datetime.datetime] = UNSET,
    unicode_1: Union[Unset, str] = UNSET,
    unicode_1_sw: Union[Unset, str] = UNSET,
    unicode_1_contains: Union[Unset, str] = UNSET,
    unicode_1_gte: Union[Unset, str] = UNSET,
    unicode_1_lte: Union[Unset, str] = UNSET,
    unicode_2: Union[Unset, str] = UNSET,
    unicode_2_sw: Union[Unset, str] = UNSET,
    unicode_2_contains: Union[Unset, str] = UNSET,
    unicode_2_gte: Union[Unset, str] = UNSET,
    unicode_2_lte: Union[Unset, str] = UNSET,
    unicode_3: Union[Unset, str] = UNSET,
    unicode_3_sw: Union[Unset, str] = UNSET,
    unicode_3_contains: Union[Unset, str] = UNSET,
    unicode_3_gte: Union[Unset, str] = UNSET,
    unicode_3_lte: Union[Unset, str] = UNSET,
    unicode_4: Union[Unset, str] = UNSET,
    unicode_4_sw: Union[Unset, str] = UNSET,
    unicode_4_contains: Union[Unset, str] = UNSET,
    unicode_4_gte: Union[Unset, str] = UNSET,
    unicode_4_lte: Union[Unset, str] = UNSET,
    unicode_5: Union[Unset, str] = UNSET,
    unicode_5_sw: Union[Unset, str] = UNSET,
    unicode_5_contains: Union[Unset, str] = UNSET,
    unicode_5_gte: Union[Unset, str] = UNSET,
    unicode_5_lte: Union[Unset, str] = UNSET,
    unicode_6: Union[Unset, str] = UNSET,
    unicode_6_sw: Union[Unset, str] = UNSET,
    unicode_6_contains: Union[Unset, str] = UNSET,
    unicode_6_gte: Union[Unset, str] = UNSET,
    unicode_6_lte: Union[Unset, str] = UNSET,
    number_1: Union[Unset, float] = UNSET,
    number_1_gt: Union[Unset, float] = UNSET,
    number_1_gte: Union[Unset, float] = UNSET,
    number_1_lt: Union[Unset, float] = UNSET,
    number_1_lte: Union[Unset, float] = UNSET,
    number_2: Union[Unset, float] = UNSET,
    number_2_gt: Union[Unset, float] = UNSET,
    number_2_gte: Union[Unset, float] = UNSET,
    number_2_lt: Union[Unset, float] = UNSET,
    number_2_lte: Union[Unset, float] = UNSET,
    redirect: Union[Unset, bool] = UNSET,
    url_only: Union[Unset, bool] = UNSET,
    info_only: Union[Unset, bool] = UNSET,
    expires_in: Union[Unset, int] = UNSET,
    uploaded_date: Union[Unset, datetime.datetime] = UNSET,
    uploaded_date_gte: Union[Unset, datetime.datetime] = UNSET,
    uploaded_date_lte: Union[Unset, datetime.datetime] = UNSET,
    size: Union[Unset, int] = UNSET,
    size_gt: Union[Unset, float] = UNSET,
    size_gte: Union[Unset, float] = UNSET,
    size_lt: Union[Unset, float] = UNSET,
    size_lte: Union[Unset, float] = UNSET,
    filename: Union[Unset, str] = UNSET,
    filename_sw: Union[Unset, str] = UNSET,
    filename_contains: Union[Unset, str] = UNSET,
    etag: Union[Unset, str] = UNSET,
    etag_sw: Union[Unset, str] = UNSET,
    etag_contains: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, FilesAtPath]]:
    """Get Files Data

     Get a files info and/or presigned GET URLs by group ID and path

    Args:
        group_id (str):
        path (str):
        cascade (Union[Unset, bool]): If true, return all paths starting with the specified path
        paths_only (Union[Unset, bool]): If true, only return list of matching file paths
        object_count (Union[Unset, bool]): If true, only return the number of objects in the file
        desc (Union[Unset, bool]): Whether to order results in descending order
        bust_cache (Union[Unset, bool]): Whether to bypass the cache and get the latest data
        limit (Union[Unset, int]): Maximum number of results to return Default: 100.
        order_by (Union[Unset, str]): Field to order results by
        last_evaluated_key (Union['GetFilesDataLastEvaluatedKeyType0', Unset,
            str]): Key to start results from
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
        redirect (Union[Unset, bool]): If true, redirect to presigned GET URL
        url_only (Union[Unset, bool]): If true, only return a list of presigned GET URLs
        info_only (Union[Unset, bool]): If true, only return file info (includes paths)
        expires_in (Union[Unset, int]): Number of seconds before presigned URLs expire
        uploaded_date (Union[Unset, datetime.datetime]): Uploaded date of files to return
        uploaded_date_gte (Union[Unset, datetime.datetime]):
        uploaded_date_lte (Union[Unset, datetime.datetime]):
        size (Union[Unset, int]): Size of file in bytes
        size_gt (Union[Unset, float]):
        size_gte (Union[Unset, float]):
        size_lt (Union[Unset, float]):
        size_lte (Union[Unset, float]):
        filename (Union[Unset, str]): Filename of file
        filename_sw (Union[Unset, str]):
        filename_contains (Union[Unset, str]):
        etag (Union[Unset, str]): ETag of file
        etag_sw (Union[Unset, str]):
        etag_contains (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FilesAtPath]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            path=path,
            client=client,
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
            redirect=redirect,
            url_only=url_only,
            info_only=info_only,
            expires_in=expires_in,
            uploaded_date=uploaded_date,
            uploaded_date_gte=uploaded_date_gte,
            uploaded_date_lte=uploaded_date_lte,
            size=size,
            size_gt=size_gt,
            size_gte=size_gte,
            size_lt=size_lt,
            size_lte=size_lte,
            filename=filename,
            filename_sw=filename_sw,
            filename_contains=filename_contains,
            etag=etag,
            etag_sw=etag_sw,
            etag_contains=etag_contains,
        )
    ).parsed
