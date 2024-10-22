import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_project_access_list import AccountProjectAccessList
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
    ids_only: Union[Unset, bool] = UNSET,
    can_read: Union[Unset, bool] = UNSET,
    can_update: Union[Unset, bool] = UNSET,
    user_permissions_can_create: Union[Unset, bool] = UNSET,
    user_permissions_can_read: Union[Unset, bool] = UNSET,
    user_permissions_can_update: Union[Unset, bool] = UNSET,
    user_permissions_can_delete: Union[Unset, bool] = UNSET,
    device_permissions_can_create: Union[Unset, bool] = UNSET,
    device_permissions_can_read: Union[Unset, bool] = UNSET,
    device_permissions_can_update: Union[Unset, bool] = UNSET,
    device_permissions_can_delete: Union[Unset, bool] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_description: Union[Unset, str] = UNSET,
    project_tags: Union[Unset, str] = UNSET,
    project_tags_contains: Union[Unset, str] = UNSET,
    project_tags_contains_any: Union[Unset, str] = UNSET,
    is_admin: Union[Unset, bool] = UNSET,
    group_permissions_can_create: Union[Unset, bool] = UNSET,
    group_permissions_can_read: Union[Unset, bool] = UNSET,
    group_permissions_can_update: Union[Unset, bool] = UNSET,
    group_permissions_can_delete: Union[Unset, bool] = UNSET,
    role_permissions_can_create: Union[Unset, bool] = UNSET,
    role_permissions_can_read: Union[Unset, bool] = UNSET,
    role_permissions_can_update: Union[Unset, bool] = UNSET,
    role_permissions_can_delete: Union[Unset, bool] = UNSET,
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

    params["ids_only"] = ids_only

    params["can_read"] = can_read

    params["can_update"] = can_update

    params["user_permissions.can_create"] = user_permissions_can_create

    params["user_permissions.can_read"] = user_permissions_can_read

    params["user_permissions.can_update"] = user_permissions_can_update

    params["user_permissions.can_delete"] = user_permissions_can_delete

    params["device_permissions.can_create"] = device_permissions_can_create

    params["device_permissions.can_read"] = device_permissions_can_read

    params["device_permissions.can_update"] = device_permissions_can_update

    params["device_permissions.can_delete"] = device_permissions_can_delete

    params["project_name"] = project_name

    params["project_description"] = project_description

    params["project_tags"] = project_tags

    params["project_tags.contains"] = project_tags_contains

    params["project_tags.contains_any"] = project_tags_contains_any

    params["is_admin"] = is_admin

    params["group_permissions.can_create"] = group_permissions_can_create

    params["group_permissions.can_read"] = group_permissions_can_read

    params["group_permissions.can_update"] = group_permissions_can_update

    params["group_permissions.can_delete"] = group_permissions_can_delete

    params["role_permissions.can_create"] = role_permissions_can_create

    params["role_permissions.can_read"] = role_permissions_can_read

    params["role_permissions.can_update"] = role_permissions_can_update

    params["role_permissions.can_delete"] = role_permissions_can_delete

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/account/access/projects",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AccountProjectAccessList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AccountProjectAccessList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AccountProjectAccessList]:
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
    ids_only: Union[Unset, bool] = UNSET,
    can_read: Union[Unset, bool] = UNSET,
    can_update: Union[Unset, bool] = UNSET,
    user_permissions_can_create: Union[Unset, bool] = UNSET,
    user_permissions_can_read: Union[Unset, bool] = UNSET,
    user_permissions_can_update: Union[Unset, bool] = UNSET,
    user_permissions_can_delete: Union[Unset, bool] = UNSET,
    device_permissions_can_create: Union[Unset, bool] = UNSET,
    device_permissions_can_read: Union[Unset, bool] = UNSET,
    device_permissions_can_update: Union[Unset, bool] = UNSET,
    device_permissions_can_delete: Union[Unset, bool] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_description: Union[Unset, str] = UNSET,
    project_tags: Union[Unset, str] = UNSET,
    project_tags_contains: Union[Unset, str] = UNSET,
    project_tags_contains_any: Union[Unset, str] = UNSET,
    is_admin: Union[Unset, bool] = UNSET,
    group_permissions_can_create: Union[Unset, bool] = UNSET,
    group_permissions_can_read: Union[Unset, bool] = UNSET,
    group_permissions_can_update: Union[Unset, bool] = UNSET,
    group_permissions_can_delete: Union[Unset, bool] = UNSET,
    role_permissions_can_create: Union[Unset, bool] = UNSET,
    role_permissions_can_read: Union[Unset, bool] = UNSET,
    role_permissions_can_update: Union[Unset, bool] = UNSET,
    role_permissions_can_delete: Union[Unset, bool] = UNSET,
) -> Response[AccountProjectAccessList]:
    """Get Account Project Access

     Get project access granted to the current account

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
        ids_only (Union[Unset, bool]): Return list(s) of IDs only
        can_read (Union[Unset, bool]): Return only access for resources you can read
        can_update (Union[Unset, bool]): Return only access for resources you can update
        user_permissions_can_create (Union[Unset, bool]): User membership create permission
        user_permissions_can_read (Union[Unset, bool]): User membership read permission
        user_permissions_can_update (Union[Unset, bool]): User membership update permission
        user_permissions_can_delete (Union[Unset, bool]): User membership delete permission
        device_permissions_can_create (Union[Unset, bool]): Device membership create permissions
        device_permissions_can_read (Union[Unset, bool]): Device membership read permissions
        device_permissions_can_update (Union[Unset, bool]): Device membership update permissions
        device_permissions_can_delete (Union[Unset, bool]): Device membership delete permissions
        project_name (Union[Unset, str]): Return access for projects with a specific name
        project_description (Union[Unset, str]): Return access for projects with a specific
            description
        project_tags (Union[Unset, str]): Return access for projects with specific tags
        project_tags_contains (Union[Unset, str]):
        project_tags_contains_any (Union[Unset, str]):
        is_admin (Union[Unset, bool]): Only return project access with admin access
        group_permissions_can_create (Union[Unset, bool]): Linked groups create permissions
        group_permissions_can_read (Union[Unset, bool]): Linked groups read permissions
        group_permissions_can_update (Union[Unset, bool]): Linked groups update permissions
        group_permissions_can_delete (Union[Unset, bool]): Linked groups delete permissions
        role_permissions_can_create (Union[Unset, bool]): Role membership CRUD permissions
        role_permissions_can_read (Union[Unset, bool]): Role membership CRUD permissions
        role_permissions_can_update (Union[Unset, bool]): Role membership CRUD permissions
        role_permissions_can_delete (Union[Unset, bool]): Role membership CRUD permissions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProjectAccessList]
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
        ids_only=ids_only,
        can_read=can_read,
        can_update=can_update,
        user_permissions_can_create=user_permissions_can_create,
        user_permissions_can_read=user_permissions_can_read,
        user_permissions_can_update=user_permissions_can_update,
        user_permissions_can_delete=user_permissions_can_delete,
        device_permissions_can_create=device_permissions_can_create,
        device_permissions_can_read=device_permissions_can_read,
        device_permissions_can_update=device_permissions_can_update,
        device_permissions_can_delete=device_permissions_can_delete,
        project_name=project_name,
        project_description=project_description,
        project_tags=project_tags,
        project_tags_contains=project_tags_contains,
        project_tags_contains_any=project_tags_contains_any,
        is_admin=is_admin,
        group_permissions_can_create=group_permissions_can_create,
        group_permissions_can_read=group_permissions_can_read,
        group_permissions_can_update=group_permissions_can_update,
        group_permissions_can_delete=group_permissions_can_delete,
        role_permissions_can_create=role_permissions_can_create,
        role_permissions_can_read=role_permissions_can_read,
        role_permissions_can_update=role_permissions_can_update,
        role_permissions_can_delete=role_permissions_can_delete,
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
    ids_only: Union[Unset, bool] = UNSET,
    can_read: Union[Unset, bool] = UNSET,
    can_update: Union[Unset, bool] = UNSET,
    user_permissions_can_create: Union[Unset, bool] = UNSET,
    user_permissions_can_read: Union[Unset, bool] = UNSET,
    user_permissions_can_update: Union[Unset, bool] = UNSET,
    user_permissions_can_delete: Union[Unset, bool] = UNSET,
    device_permissions_can_create: Union[Unset, bool] = UNSET,
    device_permissions_can_read: Union[Unset, bool] = UNSET,
    device_permissions_can_update: Union[Unset, bool] = UNSET,
    device_permissions_can_delete: Union[Unset, bool] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_description: Union[Unset, str] = UNSET,
    project_tags: Union[Unset, str] = UNSET,
    project_tags_contains: Union[Unset, str] = UNSET,
    project_tags_contains_any: Union[Unset, str] = UNSET,
    is_admin: Union[Unset, bool] = UNSET,
    group_permissions_can_create: Union[Unset, bool] = UNSET,
    group_permissions_can_read: Union[Unset, bool] = UNSET,
    group_permissions_can_update: Union[Unset, bool] = UNSET,
    group_permissions_can_delete: Union[Unset, bool] = UNSET,
    role_permissions_can_create: Union[Unset, bool] = UNSET,
    role_permissions_can_read: Union[Unset, bool] = UNSET,
    role_permissions_can_update: Union[Unset, bool] = UNSET,
    role_permissions_can_delete: Union[Unset, bool] = UNSET,
) -> Optional[AccountProjectAccessList]:
    """Get Account Project Access

     Get project access granted to the current account

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
        ids_only (Union[Unset, bool]): Return list(s) of IDs only
        can_read (Union[Unset, bool]): Return only access for resources you can read
        can_update (Union[Unset, bool]): Return only access for resources you can update
        user_permissions_can_create (Union[Unset, bool]): User membership create permission
        user_permissions_can_read (Union[Unset, bool]): User membership read permission
        user_permissions_can_update (Union[Unset, bool]): User membership update permission
        user_permissions_can_delete (Union[Unset, bool]): User membership delete permission
        device_permissions_can_create (Union[Unset, bool]): Device membership create permissions
        device_permissions_can_read (Union[Unset, bool]): Device membership read permissions
        device_permissions_can_update (Union[Unset, bool]): Device membership update permissions
        device_permissions_can_delete (Union[Unset, bool]): Device membership delete permissions
        project_name (Union[Unset, str]): Return access for projects with a specific name
        project_description (Union[Unset, str]): Return access for projects with a specific
            description
        project_tags (Union[Unset, str]): Return access for projects with specific tags
        project_tags_contains (Union[Unset, str]):
        project_tags_contains_any (Union[Unset, str]):
        is_admin (Union[Unset, bool]): Only return project access with admin access
        group_permissions_can_create (Union[Unset, bool]): Linked groups create permissions
        group_permissions_can_read (Union[Unset, bool]): Linked groups read permissions
        group_permissions_can_update (Union[Unset, bool]): Linked groups update permissions
        group_permissions_can_delete (Union[Unset, bool]): Linked groups delete permissions
        role_permissions_can_create (Union[Unset, bool]): Role membership CRUD permissions
        role_permissions_can_read (Union[Unset, bool]): Role membership CRUD permissions
        role_permissions_can_update (Union[Unset, bool]): Role membership CRUD permissions
        role_permissions_can_delete (Union[Unset, bool]): Role membership CRUD permissions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProjectAccessList
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
        ids_only=ids_only,
        can_read=can_read,
        can_update=can_update,
        user_permissions_can_create=user_permissions_can_create,
        user_permissions_can_read=user_permissions_can_read,
        user_permissions_can_update=user_permissions_can_update,
        user_permissions_can_delete=user_permissions_can_delete,
        device_permissions_can_create=device_permissions_can_create,
        device_permissions_can_read=device_permissions_can_read,
        device_permissions_can_update=device_permissions_can_update,
        device_permissions_can_delete=device_permissions_can_delete,
        project_name=project_name,
        project_description=project_description,
        project_tags=project_tags,
        project_tags_contains=project_tags_contains,
        project_tags_contains_any=project_tags_contains_any,
        is_admin=is_admin,
        group_permissions_can_create=group_permissions_can_create,
        group_permissions_can_read=group_permissions_can_read,
        group_permissions_can_update=group_permissions_can_update,
        group_permissions_can_delete=group_permissions_can_delete,
        role_permissions_can_create=role_permissions_can_create,
        role_permissions_can_read=role_permissions_can_read,
        role_permissions_can_update=role_permissions_can_update,
        role_permissions_can_delete=role_permissions_can_delete,
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
    ids_only: Union[Unset, bool] = UNSET,
    can_read: Union[Unset, bool] = UNSET,
    can_update: Union[Unset, bool] = UNSET,
    user_permissions_can_create: Union[Unset, bool] = UNSET,
    user_permissions_can_read: Union[Unset, bool] = UNSET,
    user_permissions_can_update: Union[Unset, bool] = UNSET,
    user_permissions_can_delete: Union[Unset, bool] = UNSET,
    device_permissions_can_create: Union[Unset, bool] = UNSET,
    device_permissions_can_read: Union[Unset, bool] = UNSET,
    device_permissions_can_update: Union[Unset, bool] = UNSET,
    device_permissions_can_delete: Union[Unset, bool] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_description: Union[Unset, str] = UNSET,
    project_tags: Union[Unset, str] = UNSET,
    project_tags_contains: Union[Unset, str] = UNSET,
    project_tags_contains_any: Union[Unset, str] = UNSET,
    is_admin: Union[Unset, bool] = UNSET,
    group_permissions_can_create: Union[Unset, bool] = UNSET,
    group_permissions_can_read: Union[Unset, bool] = UNSET,
    group_permissions_can_update: Union[Unset, bool] = UNSET,
    group_permissions_can_delete: Union[Unset, bool] = UNSET,
    role_permissions_can_create: Union[Unset, bool] = UNSET,
    role_permissions_can_read: Union[Unset, bool] = UNSET,
    role_permissions_can_update: Union[Unset, bool] = UNSET,
    role_permissions_can_delete: Union[Unset, bool] = UNSET,
) -> Response[AccountProjectAccessList]:
    """Get Account Project Access

     Get project access granted to the current account

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
        ids_only (Union[Unset, bool]): Return list(s) of IDs only
        can_read (Union[Unset, bool]): Return only access for resources you can read
        can_update (Union[Unset, bool]): Return only access for resources you can update
        user_permissions_can_create (Union[Unset, bool]): User membership create permission
        user_permissions_can_read (Union[Unset, bool]): User membership read permission
        user_permissions_can_update (Union[Unset, bool]): User membership update permission
        user_permissions_can_delete (Union[Unset, bool]): User membership delete permission
        device_permissions_can_create (Union[Unset, bool]): Device membership create permissions
        device_permissions_can_read (Union[Unset, bool]): Device membership read permissions
        device_permissions_can_update (Union[Unset, bool]): Device membership update permissions
        device_permissions_can_delete (Union[Unset, bool]): Device membership delete permissions
        project_name (Union[Unset, str]): Return access for projects with a specific name
        project_description (Union[Unset, str]): Return access for projects with a specific
            description
        project_tags (Union[Unset, str]): Return access for projects with specific tags
        project_tags_contains (Union[Unset, str]):
        project_tags_contains_any (Union[Unset, str]):
        is_admin (Union[Unset, bool]): Only return project access with admin access
        group_permissions_can_create (Union[Unset, bool]): Linked groups create permissions
        group_permissions_can_read (Union[Unset, bool]): Linked groups read permissions
        group_permissions_can_update (Union[Unset, bool]): Linked groups update permissions
        group_permissions_can_delete (Union[Unset, bool]): Linked groups delete permissions
        role_permissions_can_create (Union[Unset, bool]): Role membership CRUD permissions
        role_permissions_can_read (Union[Unset, bool]): Role membership CRUD permissions
        role_permissions_can_update (Union[Unset, bool]): Role membership CRUD permissions
        role_permissions_can_delete (Union[Unset, bool]): Role membership CRUD permissions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountProjectAccessList]
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
        ids_only=ids_only,
        can_read=can_read,
        can_update=can_update,
        user_permissions_can_create=user_permissions_can_create,
        user_permissions_can_read=user_permissions_can_read,
        user_permissions_can_update=user_permissions_can_update,
        user_permissions_can_delete=user_permissions_can_delete,
        device_permissions_can_create=device_permissions_can_create,
        device_permissions_can_read=device_permissions_can_read,
        device_permissions_can_update=device_permissions_can_update,
        device_permissions_can_delete=device_permissions_can_delete,
        project_name=project_name,
        project_description=project_description,
        project_tags=project_tags,
        project_tags_contains=project_tags_contains,
        project_tags_contains_any=project_tags_contains_any,
        is_admin=is_admin,
        group_permissions_can_create=group_permissions_can_create,
        group_permissions_can_read=group_permissions_can_read,
        group_permissions_can_update=group_permissions_can_update,
        group_permissions_can_delete=group_permissions_can_delete,
        role_permissions_can_create=role_permissions_can_create,
        role_permissions_can_read=role_permissions_can_read,
        role_permissions_can_update=role_permissions_can_update,
        role_permissions_can_delete=role_permissions_can_delete,
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
    ids_only: Union[Unset, bool] = UNSET,
    can_read: Union[Unset, bool] = UNSET,
    can_update: Union[Unset, bool] = UNSET,
    user_permissions_can_create: Union[Unset, bool] = UNSET,
    user_permissions_can_read: Union[Unset, bool] = UNSET,
    user_permissions_can_update: Union[Unset, bool] = UNSET,
    user_permissions_can_delete: Union[Unset, bool] = UNSET,
    device_permissions_can_create: Union[Unset, bool] = UNSET,
    device_permissions_can_read: Union[Unset, bool] = UNSET,
    device_permissions_can_update: Union[Unset, bool] = UNSET,
    device_permissions_can_delete: Union[Unset, bool] = UNSET,
    project_name: Union[Unset, str] = UNSET,
    project_description: Union[Unset, str] = UNSET,
    project_tags: Union[Unset, str] = UNSET,
    project_tags_contains: Union[Unset, str] = UNSET,
    project_tags_contains_any: Union[Unset, str] = UNSET,
    is_admin: Union[Unset, bool] = UNSET,
    group_permissions_can_create: Union[Unset, bool] = UNSET,
    group_permissions_can_read: Union[Unset, bool] = UNSET,
    group_permissions_can_update: Union[Unset, bool] = UNSET,
    group_permissions_can_delete: Union[Unset, bool] = UNSET,
    role_permissions_can_create: Union[Unset, bool] = UNSET,
    role_permissions_can_read: Union[Unset, bool] = UNSET,
    role_permissions_can_update: Union[Unset, bool] = UNSET,
    role_permissions_can_delete: Union[Unset, bool] = UNSET,
) -> Optional[AccountProjectAccessList]:
    """Get Account Project Access

     Get project access granted to the current account

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
        ids_only (Union[Unset, bool]): Return list(s) of IDs only
        can_read (Union[Unset, bool]): Return only access for resources you can read
        can_update (Union[Unset, bool]): Return only access for resources you can update
        user_permissions_can_create (Union[Unset, bool]): User membership create permission
        user_permissions_can_read (Union[Unset, bool]): User membership read permission
        user_permissions_can_update (Union[Unset, bool]): User membership update permission
        user_permissions_can_delete (Union[Unset, bool]): User membership delete permission
        device_permissions_can_create (Union[Unset, bool]): Device membership create permissions
        device_permissions_can_read (Union[Unset, bool]): Device membership read permissions
        device_permissions_can_update (Union[Unset, bool]): Device membership update permissions
        device_permissions_can_delete (Union[Unset, bool]): Device membership delete permissions
        project_name (Union[Unset, str]): Return access for projects with a specific name
        project_description (Union[Unset, str]): Return access for projects with a specific
            description
        project_tags (Union[Unset, str]): Return access for projects with specific tags
        project_tags_contains (Union[Unset, str]):
        project_tags_contains_any (Union[Unset, str]):
        is_admin (Union[Unset, bool]): Only return project access with admin access
        group_permissions_can_create (Union[Unset, bool]): Linked groups create permissions
        group_permissions_can_read (Union[Unset, bool]): Linked groups read permissions
        group_permissions_can_update (Union[Unset, bool]): Linked groups update permissions
        group_permissions_can_delete (Union[Unset, bool]): Linked groups delete permissions
        role_permissions_can_create (Union[Unset, bool]): Role membership CRUD permissions
        role_permissions_can_read (Union[Unset, bool]): Role membership CRUD permissions
        role_permissions_can_update (Union[Unset, bool]): Role membership CRUD permissions
        role_permissions_can_delete (Union[Unset, bool]): Role membership CRUD permissions

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountProjectAccessList
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
            ids_only=ids_only,
            can_read=can_read,
            can_update=can_update,
            user_permissions_can_create=user_permissions_can_create,
            user_permissions_can_read=user_permissions_can_read,
            user_permissions_can_update=user_permissions_can_update,
            user_permissions_can_delete=user_permissions_can_delete,
            device_permissions_can_create=device_permissions_can_create,
            device_permissions_can_read=device_permissions_can_read,
            device_permissions_can_update=device_permissions_can_update,
            device_permissions_can_delete=device_permissions_can_delete,
            project_name=project_name,
            project_description=project_description,
            project_tags=project_tags,
            project_tags_contains=project_tags_contains,
            project_tags_contains_any=project_tags_contains_any,
            is_admin=is_admin,
            group_permissions_can_create=group_permissions_can_create,
            group_permissions_can_read=group_permissions_can_read,
            group_permissions_can_update=group_permissions_can_update,
            group_permissions_can_delete=group_permissions_can_delete,
            role_permissions_can_create=role_permissions_can_create,
            role_permissions_can_read=role_permissions_can_read,
            role_permissions_can_update=role_permissions_can_update,
            role_permissions_can_delete=role_permissions_can_delete,
        )
    ).parsed
