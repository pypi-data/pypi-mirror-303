import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_group_list import AdminGroupList
from ...models.group_list import GroupList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_count: Union[Unset, bool] = UNSET,
    object_count: Union[Unset, bool] = UNSET,
    desc: Union[Unset, bool] = UNSET,
    bust_cache: Union[Unset, bool] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    is_delete_protected: Union[Unset, bool] = UNSET,
    created_by: Union[Unset, str] = UNSET,
    last_updated_by: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    search_fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    created_date: Union[Unset, datetime.datetime] = UNSET,
    created_date_gte: Union[Unset, datetime.datetime] = UNSET,
    created_date_lte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_gte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_lte: Union[Unset, datetime.datetime] = UNSET,
    tags: Union[Unset, str] = UNSET,
    tags_contains: Union[Unset, str] = UNSET,
    tags_contains_any: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_regex: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["page_count"] = page_count

    params["object_count"] = object_count

    params["desc"] = desc

    params["bust_cache"] = bust_cache

    params["is_active"] = is_active

    params["is_delete_protected"] = is_delete_protected

    params["created_by"] = created_by

    params["last_updated_by"] = last_updated_by

    params["search"] = search

    params["search_fields"] = search_fields

    params["limit"] = limit

    params["page"] = page

    params["order_by"] = order_by

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

    params["tags"] = tags

    params["tags.contains"] = tags_contains

    params["tags.contains_any"] = tags_contains_any

    params["name"] = name

    params["name.regex"] = name_regex

    params["project_id"] = project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/groups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union["AdminGroupList", "GroupList"]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(data: object) -> Union["AdminGroupList", "GroupList"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = GroupList.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = AdminGroupList.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union["AdminGroupList", "GroupList"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page_count: Union[Unset, bool] = UNSET,
    object_count: Union[Unset, bool] = UNSET,
    desc: Union[Unset, bool] = UNSET,
    bust_cache: Union[Unset, bool] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    is_delete_protected: Union[Unset, bool] = UNSET,
    created_by: Union[Unset, str] = UNSET,
    last_updated_by: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    search_fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    created_date: Union[Unset, datetime.datetime] = UNSET,
    created_date_gte: Union[Unset, datetime.datetime] = UNSET,
    created_date_lte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_gte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_lte: Union[Unset, datetime.datetime] = UNSET,
    tags: Union[Unset, str] = UNSET,
    tags_contains: Union[Unset, str] = UNSET,
    tags_contains_any: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_regex: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
) -> Response[Union["AdminGroupList", "GroupList"]]:
    """Get Groups

     Get a list of all groups

    Args:
        page_count (Union[Unset, bool]): Whether to only return the number of pages
        object_count (Union[Unset, bool]): Whether to only return the number of matching entries
        desc (Union[Unset, bool]): Whether to order results in descending order
        bust_cache (Union[Unset, bool]): Whether to bypass the cache and get the latest data
        is_active (Union[Unset, bool]): (Admin only) Whether to only return active accounts
        is_delete_protected (Union[Unset, bool]): Whether to only return delete-protected accounts
        created_by (Union[Unset, str]): ID of the user who created the account
        last_updated_by (Union[Unset, str]): ID of the user who last updated the account
        search (Union[Unset, str]): Search term to filter accounts by
        search_fields (Union[Unset, str]): Comma-delimited list of fields to search in
        limit (Union[Unset, int]): Maximum number of objects to return
        page (Union[Unset, int]): Page number to return
        order_by (Union[Unset, str]): Field to order results by
        created_date (Union[Unset, datetime.datetime]): Created date of items to return
        created_date_gte (Union[Unset, datetime.datetime]):
        created_date_lte (Union[Unset, datetime.datetime]):
        last_updated_date (Union[Unset, datetime.datetime]): Last edited date of items to return
        last_updated_date_gte (Union[Unset, datetime.datetime]):
        last_updated_date_lte (Union[Unset, datetime.datetime]):
        tags (Union[Unset, str]): Comma delimited list of tags on this account
        tags_contains (Union[Unset, str]):
        tags_contains_any (Union[Unset, str]):
        name (Union[Unset, str]): Name of the group
        name_regex (Union[Unset, str]):
        project_id (Union[Unset, str]): ID of the project this group belongs to, if any

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['AdminGroupList', 'GroupList']]
    """

    kwargs = _get_kwargs(
        page_count=page_count,
        object_count=object_count,
        desc=desc,
        bust_cache=bust_cache,
        is_active=is_active,
        is_delete_protected=is_delete_protected,
        created_by=created_by,
        last_updated_by=last_updated_by,
        search=search,
        search_fields=search_fields,
        limit=limit,
        page=page,
        order_by=order_by,
        created_date=created_date,
        created_date_gte=created_date_gte,
        created_date_lte=created_date_lte,
        last_updated_date=last_updated_date,
        last_updated_date_gte=last_updated_date_gte,
        last_updated_date_lte=last_updated_date_lte,
        tags=tags,
        tags_contains=tags_contains,
        tags_contains_any=tags_contains_any,
        name=name,
        name_regex=name_regex,
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page_count: Union[Unset, bool] = UNSET,
    object_count: Union[Unset, bool] = UNSET,
    desc: Union[Unset, bool] = UNSET,
    bust_cache: Union[Unset, bool] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    is_delete_protected: Union[Unset, bool] = UNSET,
    created_by: Union[Unset, str] = UNSET,
    last_updated_by: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    search_fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    created_date: Union[Unset, datetime.datetime] = UNSET,
    created_date_gte: Union[Unset, datetime.datetime] = UNSET,
    created_date_lte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_gte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_lte: Union[Unset, datetime.datetime] = UNSET,
    tags: Union[Unset, str] = UNSET,
    tags_contains: Union[Unset, str] = UNSET,
    tags_contains_any: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_regex: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
) -> Optional[Union["AdminGroupList", "GroupList"]]:
    """Get Groups

     Get a list of all groups

    Args:
        page_count (Union[Unset, bool]): Whether to only return the number of pages
        object_count (Union[Unset, bool]): Whether to only return the number of matching entries
        desc (Union[Unset, bool]): Whether to order results in descending order
        bust_cache (Union[Unset, bool]): Whether to bypass the cache and get the latest data
        is_active (Union[Unset, bool]): (Admin only) Whether to only return active accounts
        is_delete_protected (Union[Unset, bool]): Whether to only return delete-protected accounts
        created_by (Union[Unset, str]): ID of the user who created the account
        last_updated_by (Union[Unset, str]): ID of the user who last updated the account
        search (Union[Unset, str]): Search term to filter accounts by
        search_fields (Union[Unset, str]): Comma-delimited list of fields to search in
        limit (Union[Unset, int]): Maximum number of objects to return
        page (Union[Unset, int]): Page number to return
        order_by (Union[Unset, str]): Field to order results by
        created_date (Union[Unset, datetime.datetime]): Created date of items to return
        created_date_gte (Union[Unset, datetime.datetime]):
        created_date_lte (Union[Unset, datetime.datetime]):
        last_updated_date (Union[Unset, datetime.datetime]): Last edited date of items to return
        last_updated_date_gte (Union[Unset, datetime.datetime]):
        last_updated_date_lte (Union[Unset, datetime.datetime]):
        tags (Union[Unset, str]): Comma delimited list of tags on this account
        tags_contains (Union[Unset, str]):
        tags_contains_any (Union[Unset, str]):
        name (Union[Unset, str]): Name of the group
        name_regex (Union[Unset, str]):
        project_id (Union[Unset, str]): ID of the project this group belongs to, if any

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['AdminGroupList', 'GroupList']
    """

    return sync_detailed(
        client=client,
        page_count=page_count,
        object_count=object_count,
        desc=desc,
        bust_cache=bust_cache,
        is_active=is_active,
        is_delete_protected=is_delete_protected,
        created_by=created_by,
        last_updated_by=last_updated_by,
        search=search,
        search_fields=search_fields,
        limit=limit,
        page=page,
        order_by=order_by,
        created_date=created_date,
        created_date_gte=created_date_gte,
        created_date_lte=created_date_lte,
        last_updated_date=last_updated_date,
        last_updated_date_gte=last_updated_date_gte,
        last_updated_date_lte=last_updated_date_lte,
        tags=tags,
        tags_contains=tags_contains,
        tags_contains_any=tags_contains_any,
        name=name,
        name_regex=name_regex,
        project_id=project_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page_count: Union[Unset, bool] = UNSET,
    object_count: Union[Unset, bool] = UNSET,
    desc: Union[Unset, bool] = UNSET,
    bust_cache: Union[Unset, bool] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    is_delete_protected: Union[Unset, bool] = UNSET,
    created_by: Union[Unset, str] = UNSET,
    last_updated_by: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    search_fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    created_date: Union[Unset, datetime.datetime] = UNSET,
    created_date_gte: Union[Unset, datetime.datetime] = UNSET,
    created_date_lte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_gte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_lte: Union[Unset, datetime.datetime] = UNSET,
    tags: Union[Unset, str] = UNSET,
    tags_contains: Union[Unset, str] = UNSET,
    tags_contains_any: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_regex: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
) -> Response[Union["AdminGroupList", "GroupList"]]:
    """Get Groups

     Get a list of all groups

    Args:
        page_count (Union[Unset, bool]): Whether to only return the number of pages
        object_count (Union[Unset, bool]): Whether to only return the number of matching entries
        desc (Union[Unset, bool]): Whether to order results in descending order
        bust_cache (Union[Unset, bool]): Whether to bypass the cache and get the latest data
        is_active (Union[Unset, bool]): (Admin only) Whether to only return active accounts
        is_delete_protected (Union[Unset, bool]): Whether to only return delete-protected accounts
        created_by (Union[Unset, str]): ID of the user who created the account
        last_updated_by (Union[Unset, str]): ID of the user who last updated the account
        search (Union[Unset, str]): Search term to filter accounts by
        search_fields (Union[Unset, str]): Comma-delimited list of fields to search in
        limit (Union[Unset, int]): Maximum number of objects to return
        page (Union[Unset, int]): Page number to return
        order_by (Union[Unset, str]): Field to order results by
        created_date (Union[Unset, datetime.datetime]): Created date of items to return
        created_date_gte (Union[Unset, datetime.datetime]):
        created_date_lte (Union[Unset, datetime.datetime]):
        last_updated_date (Union[Unset, datetime.datetime]): Last edited date of items to return
        last_updated_date_gte (Union[Unset, datetime.datetime]):
        last_updated_date_lte (Union[Unset, datetime.datetime]):
        tags (Union[Unset, str]): Comma delimited list of tags on this account
        tags_contains (Union[Unset, str]):
        tags_contains_any (Union[Unset, str]):
        name (Union[Unset, str]): Name of the group
        name_regex (Union[Unset, str]):
        project_id (Union[Unset, str]): ID of the project this group belongs to, if any

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['AdminGroupList', 'GroupList']]
    """

    kwargs = _get_kwargs(
        page_count=page_count,
        object_count=object_count,
        desc=desc,
        bust_cache=bust_cache,
        is_active=is_active,
        is_delete_protected=is_delete_protected,
        created_by=created_by,
        last_updated_by=last_updated_by,
        search=search,
        search_fields=search_fields,
        limit=limit,
        page=page,
        order_by=order_by,
        created_date=created_date,
        created_date_gte=created_date_gte,
        created_date_lte=created_date_lte,
        last_updated_date=last_updated_date,
        last_updated_date_gte=last_updated_date_gte,
        last_updated_date_lte=last_updated_date_lte,
        tags=tags,
        tags_contains=tags_contains,
        tags_contains_any=tags_contains_any,
        name=name,
        name_regex=name_regex,
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page_count: Union[Unset, bool] = UNSET,
    object_count: Union[Unset, bool] = UNSET,
    desc: Union[Unset, bool] = UNSET,
    bust_cache: Union[Unset, bool] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    is_delete_protected: Union[Unset, bool] = UNSET,
    created_by: Union[Unset, str] = UNSET,
    last_updated_by: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    search_fields: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    created_date: Union[Unset, datetime.datetime] = UNSET,
    created_date_gte: Union[Unset, datetime.datetime] = UNSET,
    created_date_lte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_gte: Union[Unset, datetime.datetime] = UNSET,
    last_updated_date_lte: Union[Unset, datetime.datetime] = UNSET,
    tags: Union[Unset, str] = UNSET,
    tags_contains: Union[Unset, str] = UNSET,
    tags_contains_any: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_regex: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
) -> Optional[Union["AdminGroupList", "GroupList"]]:
    """Get Groups

     Get a list of all groups

    Args:
        page_count (Union[Unset, bool]): Whether to only return the number of pages
        object_count (Union[Unset, bool]): Whether to only return the number of matching entries
        desc (Union[Unset, bool]): Whether to order results in descending order
        bust_cache (Union[Unset, bool]): Whether to bypass the cache and get the latest data
        is_active (Union[Unset, bool]): (Admin only) Whether to only return active accounts
        is_delete_protected (Union[Unset, bool]): Whether to only return delete-protected accounts
        created_by (Union[Unset, str]): ID of the user who created the account
        last_updated_by (Union[Unset, str]): ID of the user who last updated the account
        search (Union[Unset, str]): Search term to filter accounts by
        search_fields (Union[Unset, str]): Comma-delimited list of fields to search in
        limit (Union[Unset, int]): Maximum number of objects to return
        page (Union[Unset, int]): Page number to return
        order_by (Union[Unset, str]): Field to order results by
        created_date (Union[Unset, datetime.datetime]): Created date of items to return
        created_date_gte (Union[Unset, datetime.datetime]):
        created_date_lte (Union[Unset, datetime.datetime]):
        last_updated_date (Union[Unset, datetime.datetime]): Last edited date of items to return
        last_updated_date_gte (Union[Unset, datetime.datetime]):
        last_updated_date_lte (Union[Unset, datetime.datetime]):
        tags (Union[Unset, str]): Comma delimited list of tags on this account
        tags_contains (Union[Unset, str]):
        tags_contains_any (Union[Unset, str]):
        name (Union[Unset, str]): Name of the group
        name_regex (Union[Unset, str]):
        project_id (Union[Unset, str]): ID of the project this group belongs to, if any

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['AdminGroupList', 'GroupList']
    """

    return (
        await asyncio_detailed(
            client=client,
            page_count=page_count,
            object_count=object_count,
            desc=desc,
            bust_cache=bust_cache,
            is_active=is_active,
            is_delete_protected=is_delete_protected,
            created_by=created_by,
            last_updated_by=last_updated_by,
            search=search,
            search_fields=search_fields,
            limit=limit,
            page=page,
            order_by=order_by,
            created_date=created_date,
            created_date_gte=created_date_gte,
            created_date_lte=created_date_lte,
            last_updated_date=last_updated_date,
            last_updated_date_gte=last_updated_date_gte,
            last_updated_date_lte=last_updated_date_lte,
            tags=tags,
            tags_contains=tags_contains,
            tags_contains_any=tags_contains_any,
            name=name,
            name_regex=name_regex,
            project_id=project_id,
        )
    ).parsed
