import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_role_access_list import AccountRoleAccessList
from ...models.admin_account_role_access_list import AdminAccountRoleAccessList
from ...models.get_account_role_access_custom_attributes import (
    GetAccountRoleAccessCustomAttributes,
)
from ...models.get_account_role_access_restricted_custom_attributes import (
    GetAccountRoleAccessRestrictedCustomAttributes,
)
from ...models.role_id_list import RoleIdList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    is_active: Union[Unset, None, bool] = UNSET,
    is_delete_protected: Union[Unset, None, bool] = UNSET,
    created_by: Union[Unset, None, str] = UNSET,
    last_updated_by: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    search_fields: Union[Unset, None, str] = UNSET,
    page_count: Union[None, Unset, bool, str] = False,
    object_count: Union[None, Unset, bool, str] = False,
    limit: Union[Unset, None, int] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
    desc: Union[None, Unset, bool, str] = False,
    bust_cache: Union[None, Unset, bool, str] = False,
    created_date: Union[Unset, None, datetime.datetime] = UNSET,
    created_date_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_date_lte: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_date: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_date_gte: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_date_lte: Union[Unset, None, datetime.datetime] = UNSET,
    tags: Union[Unset, None, str] = UNSET,
    tags_contains: Union[Unset, None, str] = UNSET,
    tags_contains_any: Union[Unset, None, str] = UNSET,
    custom_attributes: Union[Unset, None, "GetAccountRoleAccessCustomAttributes"] = UNSET,
    restricted_custom_attributes: Union[
        Unset, None, "GetAccountRoleAccessRestrictedCustomAttributes"
    ] = UNSET,
    ids_only: Union[None, Unset, bool, str] = False,
    can_read: Union[Unset, None, bool] = UNSET,
    can_update: Union[Unset, None, bool] = UNSET,
    user_permissions_can_create: Union[Unset, None, bool] = UNSET,
    user_permissions_can_read: Union[Unset, None, bool] = UNSET,
    user_permissions_can_update: Union[Unset, None, bool] = UNSET,
    user_permissions_can_delete: Union[Unset, None, bool] = UNSET,
    device_permissions_can_create: Union[Unset, None, bool] = UNSET,
    device_permissions_can_read: Union[Unset, None, bool] = UNSET,
    device_permissions_can_update: Union[Unset, None, bool] = UNSET,
    device_permissions_can_delete: Union[Unset, None, bool] = UNSET,
    project_id: Union[Unset, None, str] = UNSET,
    group_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["is_active"] = is_active

    params["is_delete_protected"] = is_delete_protected

    params["created_by"] = created_by

    params["last_updated_by"] = last_updated_by

    params["search"] = search

    params["search_fields"] = search_fields

    json_page_count: Union[None, Unset, bool, str]
    if isinstance(page_count, Unset):
        json_page_count = UNSET
    elif page_count is None:
        json_page_count = None

    else:
        json_page_count = page_count

    params["page_count"] = json_page_count

    json_object_count: Union[None, Unset, bool, str]
    if isinstance(object_count, Unset):
        json_object_count = UNSET
    elif object_count is None:
        json_object_count = None

    else:
        json_object_count = object_count

    params["object_count"] = json_object_count

    params["limit"] = limit

    params["page"] = page

    params["order_by"] = order_by

    json_desc: Union[None, Unset, bool, str]
    if isinstance(desc, Unset):
        json_desc = UNSET
    elif desc is None:
        json_desc = None

    else:
        json_desc = desc

    params["desc"] = json_desc

    json_bust_cache: Union[None, Unset, bool, str]
    if isinstance(bust_cache, Unset):
        json_bust_cache = UNSET
    elif bust_cache is None:
        json_bust_cache = None

    else:
        json_bust_cache = bust_cache

    params["bust_cache"] = json_bust_cache

    json_created_date: Union[Unset, None, str] = UNSET
    if not isinstance(created_date, Unset):
        json_created_date = created_date.isoformat() if created_date else None

    params["created_date"] = json_created_date

    json_created_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(created_date_gte, Unset):
        json_created_date_gte = created_date_gte.isoformat() if created_date_gte else None

    params["created_date.gte"] = json_created_date_gte

    json_created_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(created_date_lte, Unset):
        json_created_date_lte = created_date_lte.isoformat() if created_date_lte else None

    params["created_date.lte"] = json_created_date_lte

    json_last_updated_date: Union[Unset, None, str] = UNSET
    if not isinstance(last_updated_date, Unset):
        json_last_updated_date = last_updated_date.isoformat() if last_updated_date else None

    params["last_updated_date"] = json_last_updated_date

    json_last_updated_date_gte: Union[Unset, None, str] = UNSET
    if not isinstance(last_updated_date_gte, Unset):
        json_last_updated_date_gte = (
            last_updated_date_gte.isoformat() if last_updated_date_gte else None
        )

    params["last_updated_date.gte"] = json_last_updated_date_gte

    json_last_updated_date_lte: Union[Unset, None, str] = UNSET
    if not isinstance(last_updated_date_lte, Unset):
        json_last_updated_date_lte = (
            last_updated_date_lte.isoformat() if last_updated_date_lte else None
        )

    params["last_updated_date.lte"] = json_last_updated_date_lte

    params["tags"] = tags

    params["tags.contains"] = tags_contains

    params["tags.contains_any"] = tags_contains_any

    json_custom_attributes: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(custom_attributes, Unset):
        json_custom_attributes = custom_attributes.to_dict() if custom_attributes else None

    if not isinstance(json_custom_attributes, Unset) and json_custom_attributes is not None:
        params.update(json_custom_attributes)

    json_restricted_custom_attributes: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(restricted_custom_attributes, Unset):
        json_restricted_custom_attributes = (
            restricted_custom_attributes.to_dict() if restricted_custom_attributes else None
        )

    if (
        not isinstance(json_restricted_custom_attributes, Unset)
        and json_restricted_custom_attributes is not None
    ):
        params.update(json_restricted_custom_attributes)

    json_ids_only: Union[None, Unset, bool, str]
    if isinstance(ids_only, Unset):
        json_ids_only = UNSET
    elif ids_only is None:
        json_ids_only = None

    else:
        json_ids_only = ids_only

    params["ids_only"] = json_ids_only

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

    params["project_id"] = project_id

    params["group_id"] = group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v2/account/access/roles",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union["AccountRoleAccessList", "AdminAccountRoleAccessList", "RoleIdList"]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(
            data: object,
        ) -> Union["AccountRoleAccessList", "AdminAccountRoleAccessList", "RoleIdList"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = AdminAccountRoleAccessList.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = AccountRoleAccessList.from_dict(data)

                return response_200_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_2 = RoleIdList.from_dict(data)

            return response_200_type_2

        response_200 = _parse_response_200(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union["AccountRoleAccessList", "AdminAccountRoleAccessList", "RoleIdList"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    is_active: Union[Unset, None, bool] = UNSET,
    is_delete_protected: Union[Unset, None, bool] = UNSET,
    created_by: Union[Unset, None, str] = UNSET,
    last_updated_by: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    search_fields: Union[Unset, None, str] = UNSET,
    page_count: Union[None, Unset, bool, str] = False,
    object_count: Union[None, Unset, bool, str] = False,
    limit: Union[Unset, None, int] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
    desc: Union[None, Unset, bool, str] = False,
    bust_cache: Union[None, Unset, bool, str] = False,
    created_date: Union[Unset, None, datetime.datetime] = UNSET,
    created_date_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_date_lte: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_date: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_date_gte: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_date_lte: Union[Unset, None, datetime.datetime] = UNSET,
    tags: Union[Unset, None, str] = UNSET,
    tags_contains: Union[Unset, None, str] = UNSET,
    tags_contains_any: Union[Unset, None, str] = UNSET,
    custom_attributes: Union[Unset, None, "GetAccountRoleAccessCustomAttributes"] = UNSET,
    restricted_custom_attributes: Union[
        Unset, None, "GetAccountRoleAccessRestrictedCustomAttributes"
    ] = UNSET,
    ids_only: Union[None, Unset, bool, str] = False,
    can_read: Union[Unset, None, bool] = UNSET,
    can_update: Union[Unset, None, bool] = UNSET,
    user_permissions_can_create: Union[Unset, None, bool] = UNSET,
    user_permissions_can_read: Union[Unset, None, bool] = UNSET,
    user_permissions_can_update: Union[Unset, None, bool] = UNSET,
    user_permissions_can_delete: Union[Unset, None, bool] = UNSET,
    device_permissions_can_create: Union[Unset, None, bool] = UNSET,
    device_permissions_can_read: Union[Unset, None, bool] = UNSET,
    device_permissions_can_update: Union[Unset, None, bool] = UNSET,
    device_permissions_can_delete: Union[Unset, None, bool] = UNSET,
    project_id: Union[Unset, None, str] = UNSET,
    group_id: Union[Unset, None, str] = UNSET,
) -> Response[Union["AccountRoleAccessList", "AdminAccountRoleAccessList", "RoleIdList"]]:
    """Get Account Role Access

     Get role access granted to the current account

    Args:
        is_active (Union[Unset, None, bool]):  (Admin only) Whether to only return active devices
        is_delete_protected (Union[Unset, None, bool]): Whether to only return delete-protected
            devices
        created_by (Union[Unset, None, str]): ID of the user who created the device
        last_updated_by (Union[Unset, None, str]): ID of the user who last updated the device
        search (Union[Unset, None, str]): Search term to filter devices by
        search_fields (Union[Unset, None, str]): Comma-delimited list of fields to search in
        page_count (Union[None, Unset, bool, str]): Whether to only return the number of pages
        object_count (Union[None, Unset, bool, str]): Whether to only return the number of
            matching entries
        limit (Union[Unset, None, int]): Maximum number of objects to return
        page (Union[Unset, None, int]): Page number to return
        order_by (Union[Unset, None, str]): Field to order results by
        desc (Union[None, Unset, bool, str]): Whether to order results in descending order
        bust_cache (Union[None, Unset, bool, str]): Whether to bypass the cache and get the latest
            data
        created_date (Union[Unset, None, datetime.datetime]): Created date of items to return
        created_date_gte (Union[Unset, None, datetime.datetime]):
        created_date_lte (Union[Unset, None, datetime.datetime]):
        last_updated_date (Union[Unset, None, datetime.datetime]): Last edited date of items to
            return
        last_updated_date_gte (Union[Unset, None, datetime.datetime]):
        last_updated_date_lte (Union[Unset, None, datetime.datetime]):
        tags (Union[Unset, None, str]): Comma delimited list of tags on this device
        tags_contains (Union[Unset, None, str]):
        tags_contains_any (Union[Unset, None, str]):
        custom_attributes (Union[Unset, None,
            GetAccountRoleAccessCustomAttributes]): Do not set directly, use dot
            operators
        restricted_custom_attributes (Union[Unset, None,
            GetAccountRoleAccessRestrictedCustomAttributes]): Do not set
            directly, use dot operators
        ids_only (Union[None, Unset, bool, str]): Return list(s) of IDs only
        can_read (Union[Unset, None, bool]): Return only access for resources you can read
        can_update (Union[Unset, None, bool]): Return only access for resources you can update
        user_permissions_can_create (Union[Unset, None, bool]): User membership create permission
        user_permissions_can_read (Union[Unset, None, bool]): User membership read permission
        user_permissions_can_update (Union[Unset, None, bool]): User membership update permission
        user_permissions_can_delete (Union[Unset, None, bool]): User membership delete permission
        device_permissions_can_create (Union[Unset, None, bool]): Device membership create
            permissions
        device_permissions_can_read (Union[Unset, None, bool]): Device membership read permissions
        device_permissions_can_update (Union[Unset, None, bool]): Device membership update
            permissions
        device_permissions_can_delete (Union[Unset, None, bool]): Device membership delete
            permissions
        project_id (Union[Unset, None, str]): Only return group access under a specific project
        group_id (Union[Unset, None, str]): Only return role access under a specific group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['AccountRoleAccessList', 'AdminAccountRoleAccessList', 'RoleIdList']]
    """

    kwargs = _get_kwargs(
        is_active=is_active,
        is_delete_protected=is_delete_protected,
        created_by=created_by,
        last_updated_by=last_updated_by,
        search=search,
        search_fields=search_fields,
        page_count=page_count,
        object_count=object_count,
        limit=limit,
        page=page,
        order_by=order_by,
        desc=desc,
        bust_cache=bust_cache,
        created_date=created_date,
        created_date_gte=created_date_gte,
        created_date_lte=created_date_lte,
        last_updated_date=last_updated_date,
        last_updated_date_gte=last_updated_date_gte,
        last_updated_date_lte=last_updated_date_lte,
        tags=tags,
        tags_contains=tags_contains,
        tags_contains_any=tags_contains_any,
        custom_attributes=custom_attributes,
        restricted_custom_attributes=restricted_custom_attributes,
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
        project_id=project_id,
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    is_active: Union[Unset, None, bool] = UNSET,
    is_delete_protected: Union[Unset, None, bool] = UNSET,
    created_by: Union[Unset, None, str] = UNSET,
    last_updated_by: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    search_fields: Union[Unset, None, str] = UNSET,
    page_count: Union[None, Unset, bool, str] = False,
    object_count: Union[None, Unset, bool, str] = False,
    limit: Union[Unset, None, int] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
    desc: Union[None, Unset, bool, str] = False,
    bust_cache: Union[None, Unset, bool, str] = False,
    created_date: Union[Unset, None, datetime.datetime] = UNSET,
    created_date_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_date_lte: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_date: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_date_gte: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_date_lte: Union[Unset, None, datetime.datetime] = UNSET,
    tags: Union[Unset, None, str] = UNSET,
    tags_contains: Union[Unset, None, str] = UNSET,
    tags_contains_any: Union[Unset, None, str] = UNSET,
    custom_attributes: Union[Unset, None, "GetAccountRoleAccessCustomAttributes"] = UNSET,
    restricted_custom_attributes: Union[
        Unset, None, "GetAccountRoleAccessRestrictedCustomAttributes"
    ] = UNSET,
    ids_only: Union[None, Unset, bool, str] = False,
    can_read: Union[Unset, None, bool] = UNSET,
    can_update: Union[Unset, None, bool] = UNSET,
    user_permissions_can_create: Union[Unset, None, bool] = UNSET,
    user_permissions_can_read: Union[Unset, None, bool] = UNSET,
    user_permissions_can_update: Union[Unset, None, bool] = UNSET,
    user_permissions_can_delete: Union[Unset, None, bool] = UNSET,
    device_permissions_can_create: Union[Unset, None, bool] = UNSET,
    device_permissions_can_read: Union[Unset, None, bool] = UNSET,
    device_permissions_can_update: Union[Unset, None, bool] = UNSET,
    device_permissions_can_delete: Union[Unset, None, bool] = UNSET,
    project_id: Union[Unset, None, str] = UNSET,
    group_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union["AccountRoleAccessList", "AdminAccountRoleAccessList", "RoleIdList"]]:
    """Get Account Role Access

     Get role access granted to the current account

    Args:
        is_active (Union[Unset, None, bool]):  (Admin only) Whether to only return active devices
        is_delete_protected (Union[Unset, None, bool]): Whether to only return delete-protected
            devices
        created_by (Union[Unset, None, str]): ID of the user who created the device
        last_updated_by (Union[Unset, None, str]): ID of the user who last updated the device
        search (Union[Unset, None, str]): Search term to filter devices by
        search_fields (Union[Unset, None, str]): Comma-delimited list of fields to search in
        page_count (Union[None, Unset, bool, str]): Whether to only return the number of pages
        object_count (Union[None, Unset, bool, str]): Whether to only return the number of
            matching entries
        limit (Union[Unset, None, int]): Maximum number of objects to return
        page (Union[Unset, None, int]): Page number to return
        order_by (Union[Unset, None, str]): Field to order results by
        desc (Union[None, Unset, bool, str]): Whether to order results in descending order
        bust_cache (Union[None, Unset, bool, str]): Whether to bypass the cache and get the latest
            data
        created_date (Union[Unset, None, datetime.datetime]): Created date of items to return
        created_date_gte (Union[Unset, None, datetime.datetime]):
        created_date_lte (Union[Unset, None, datetime.datetime]):
        last_updated_date (Union[Unset, None, datetime.datetime]): Last edited date of items to
            return
        last_updated_date_gte (Union[Unset, None, datetime.datetime]):
        last_updated_date_lte (Union[Unset, None, datetime.datetime]):
        tags (Union[Unset, None, str]): Comma delimited list of tags on this device
        tags_contains (Union[Unset, None, str]):
        tags_contains_any (Union[Unset, None, str]):
        custom_attributes (Union[Unset, None,
            GetAccountRoleAccessCustomAttributes]): Do not set directly, use dot
            operators
        restricted_custom_attributes (Union[Unset, None,
            GetAccountRoleAccessRestrictedCustomAttributes]): Do not set
            directly, use dot operators
        ids_only (Union[None, Unset, bool, str]): Return list(s) of IDs only
        can_read (Union[Unset, None, bool]): Return only access for resources you can read
        can_update (Union[Unset, None, bool]): Return only access for resources you can update
        user_permissions_can_create (Union[Unset, None, bool]): User membership create permission
        user_permissions_can_read (Union[Unset, None, bool]): User membership read permission
        user_permissions_can_update (Union[Unset, None, bool]): User membership update permission
        user_permissions_can_delete (Union[Unset, None, bool]): User membership delete permission
        device_permissions_can_create (Union[Unset, None, bool]): Device membership create
            permissions
        device_permissions_can_read (Union[Unset, None, bool]): Device membership read permissions
        device_permissions_can_update (Union[Unset, None, bool]): Device membership update
            permissions
        device_permissions_can_delete (Union[Unset, None, bool]): Device membership delete
            permissions
        project_id (Union[Unset, None, str]): Only return group access under a specific project
        group_id (Union[Unset, None, str]): Only return role access under a specific group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['AccountRoleAccessList', 'AdminAccountRoleAccessList', 'RoleIdList']
    """

    return sync_detailed(
        client=client,
        is_active=is_active,
        is_delete_protected=is_delete_protected,
        created_by=created_by,
        last_updated_by=last_updated_by,
        search=search,
        search_fields=search_fields,
        page_count=page_count,
        object_count=object_count,
        limit=limit,
        page=page,
        order_by=order_by,
        desc=desc,
        bust_cache=bust_cache,
        created_date=created_date,
        created_date_gte=created_date_gte,
        created_date_lte=created_date_lte,
        last_updated_date=last_updated_date,
        last_updated_date_gte=last_updated_date_gte,
        last_updated_date_lte=last_updated_date_lte,
        tags=tags,
        tags_contains=tags_contains,
        tags_contains_any=tags_contains_any,
        custom_attributes=custom_attributes,
        restricted_custom_attributes=restricted_custom_attributes,
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
        project_id=project_id,
        group_id=group_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    is_active: Union[Unset, None, bool] = UNSET,
    is_delete_protected: Union[Unset, None, bool] = UNSET,
    created_by: Union[Unset, None, str] = UNSET,
    last_updated_by: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    search_fields: Union[Unset, None, str] = UNSET,
    page_count: Union[None, Unset, bool, str] = False,
    object_count: Union[None, Unset, bool, str] = False,
    limit: Union[Unset, None, int] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
    desc: Union[None, Unset, bool, str] = False,
    bust_cache: Union[None, Unset, bool, str] = False,
    created_date: Union[Unset, None, datetime.datetime] = UNSET,
    created_date_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_date_lte: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_date: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_date_gte: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_date_lte: Union[Unset, None, datetime.datetime] = UNSET,
    tags: Union[Unset, None, str] = UNSET,
    tags_contains: Union[Unset, None, str] = UNSET,
    tags_contains_any: Union[Unset, None, str] = UNSET,
    custom_attributes: Union[Unset, None, "GetAccountRoleAccessCustomAttributes"] = UNSET,
    restricted_custom_attributes: Union[
        Unset, None, "GetAccountRoleAccessRestrictedCustomAttributes"
    ] = UNSET,
    ids_only: Union[None, Unset, bool, str] = False,
    can_read: Union[Unset, None, bool] = UNSET,
    can_update: Union[Unset, None, bool] = UNSET,
    user_permissions_can_create: Union[Unset, None, bool] = UNSET,
    user_permissions_can_read: Union[Unset, None, bool] = UNSET,
    user_permissions_can_update: Union[Unset, None, bool] = UNSET,
    user_permissions_can_delete: Union[Unset, None, bool] = UNSET,
    device_permissions_can_create: Union[Unset, None, bool] = UNSET,
    device_permissions_can_read: Union[Unset, None, bool] = UNSET,
    device_permissions_can_update: Union[Unset, None, bool] = UNSET,
    device_permissions_can_delete: Union[Unset, None, bool] = UNSET,
    project_id: Union[Unset, None, str] = UNSET,
    group_id: Union[Unset, None, str] = UNSET,
) -> Response[Union["AccountRoleAccessList", "AdminAccountRoleAccessList", "RoleIdList"]]:
    """Get Account Role Access

     Get role access granted to the current account

    Args:
        is_active (Union[Unset, None, bool]):  (Admin only) Whether to only return active devices
        is_delete_protected (Union[Unset, None, bool]): Whether to only return delete-protected
            devices
        created_by (Union[Unset, None, str]): ID of the user who created the device
        last_updated_by (Union[Unset, None, str]): ID of the user who last updated the device
        search (Union[Unset, None, str]): Search term to filter devices by
        search_fields (Union[Unset, None, str]): Comma-delimited list of fields to search in
        page_count (Union[None, Unset, bool, str]): Whether to only return the number of pages
        object_count (Union[None, Unset, bool, str]): Whether to only return the number of
            matching entries
        limit (Union[Unset, None, int]): Maximum number of objects to return
        page (Union[Unset, None, int]): Page number to return
        order_by (Union[Unset, None, str]): Field to order results by
        desc (Union[None, Unset, bool, str]): Whether to order results in descending order
        bust_cache (Union[None, Unset, bool, str]): Whether to bypass the cache and get the latest
            data
        created_date (Union[Unset, None, datetime.datetime]): Created date of items to return
        created_date_gte (Union[Unset, None, datetime.datetime]):
        created_date_lte (Union[Unset, None, datetime.datetime]):
        last_updated_date (Union[Unset, None, datetime.datetime]): Last edited date of items to
            return
        last_updated_date_gte (Union[Unset, None, datetime.datetime]):
        last_updated_date_lte (Union[Unset, None, datetime.datetime]):
        tags (Union[Unset, None, str]): Comma delimited list of tags on this device
        tags_contains (Union[Unset, None, str]):
        tags_contains_any (Union[Unset, None, str]):
        custom_attributes (Union[Unset, None,
            GetAccountRoleAccessCustomAttributes]): Do not set directly, use dot
            operators
        restricted_custom_attributes (Union[Unset, None,
            GetAccountRoleAccessRestrictedCustomAttributes]): Do not set
            directly, use dot operators
        ids_only (Union[None, Unset, bool, str]): Return list(s) of IDs only
        can_read (Union[Unset, None, bool]): Return only access for resources you can read
        can_update (Union[Unset, None, bool]): Return only access for resources you can update
        user_permissions_can_create (Union[Unset, None, bool]): User membership create permission
        user_permissions_can_read (Union[Unset, None, bool]): User membership read permission
        user_permissions_can_update (Union[Unset, None, bool]): User membership update permission
        user_permissions_can_delete (Union[Unset, None, bool]): User membership delete permission
        device_permissions_can_create (Union[Unset, None, bool]): Device membership create
            permissions
        device_permissions_can_read (Union[Unset, None, bool]): Device membership read permissions
        device_permissions_can_update (Union[Unset, None, bool]): Device membership update
            permissions
        device_permissions_can_delete (Union[Unset, None, bool]): Device membership delete
            permissions
        project_id (Union[Unset, None, str]): Only return group access under a specific project
        group_id (Union[Unset, None, str]): Only return role access under a specific group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['AccountRoleAccessList', 'AdminAccountRoleAccessList', 'RoleIdList']]
    """

    kwargs = _get_kwargs(
        is_active=is_active,
        is_delete_protected=is_delete_protected,
        created_by=created_by,
        last_updated_by=last_updated_by,
        search=search,
        search_fields=search_fields,
        page_count=page_count,
        object_count=object_count,
        limit=limit,
        page=page,
        order_by=order_by,
        desc=desc,
        bust_cache=bust_cache,
        created_date=created_date,
        created_date_gte=created_date_gte,
        created_date_lte=created_date_lte,
        last_updated_date=last_updated_date,
        last_updated_date_gte=last_updated_date_gte,
        last_updated_date_lte=last_updated_date_lte,
        tags=tags,
        tags_contains=tags_contains,
        tags_contains_any=tags_contains_any,
        custom_attributes=custom_attributes,
        restricted_custom_attributes=restricted_custom_attributes,
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
        project_id=project_id,
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    is_active: Union[Unset, None, bool] = UNSET,
    is_delete_protected: Union[Unset, None, bool] = UNSET,
    created_by: Union[Unset, None, str] = UNSET,
    last_updated_by: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    search_fields: Union[Unset, None, str] = UNSET,
    page_count: Union[None, Unset, bool, str] = False,
    object_count: Union[None, Unset, bool, str] = False,
    limit: Union[Unset, None, int] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
    desc: Union[None, Unset, bool, str] = False,
    bust_cache: Union[None, Unset, bool, str] = False,
    created_date: Union[Unset, None, datetime.datetime] = UNSET,
    created_date_gte: Union[Unset, None, datetime.datetime] = UNSET,
    created_date_lte: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_date: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_date_gte: Union[Unset, None, datetime.datetime] = UNSET,
    last_updated_date_lte: Union[Unset, None, datetime.datetime] = UNSET,
    tags: Union[Unset, None, str] = UNSET,
    tags_contains: Union[Unset, None, str] = UNSET,
    tags_contains_any: Union[Unset, None, str] = UNSET,
    custom_attributes: Union[Unset, None, "GetAccountRoleAccessCustomAttributes"] = UNSET,
    restricted_custom_attributes: Union[
        Unset, None, "GetAccountRoleAccessRestrictedCustomAttributes"
    ] = UNSET,
    ids_only: Union[None, Unset, bool, str] = False,
    can_read: Union[Unset, None, bool] = UNSET,
    can_update: Union[Unset, None, bool] = UNSET,
    user_permissions_can_create: Union[Unset, None, bool] = UNSET,
    user_permissions_can_read: Union[Unset, None, bool] = UNSET,
    user_permissions_can_update: Union[Unset, None, bool] = UNSET,
    user_permissions_can_delete: Union[Unset, None, bool] = UNSET,
    device_permissions_can_create: Union[Unset, None, bool] = UNSET,
    device_permissions_can_read: Union[Unset, None, bool] = UNSET,
    device_permissions_can_update: Union[Unset, None, bool] = UNSET,
    device_permissions_can_delete: Union[Unset, None, bool] = UNSET,
    project_id: Union[Unset, None, str] = UNSET,
    group_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union["AccountRoleAccessList", "AdminAccountRoleAccessList", "RoleIdList"]]:
    """Get Account Role Access

     Get role access granted to the current account

    Args:
        is_active (Union[Unset, None, bool]):  (Admin only) Whether to only return active devices
        is_delete_protected (Union[Unset, None, bool]): Whether to only return delete-protected
            devices
        created_by (Union[Unset, None, str]): ID of the user who created the device
        last_updated_by (Union[Unset, None, str]): ID of the user who last updated the device
        search (Union[Unset, None, str]): Search term to filter devices by
        search_fields (Union[Unset, None, str]): Comma-delimited list of fields to search in
        page_count (Union[None, Unset, bool, str]): Whether to only return the number of pages
        object_count (Union[None, Unset, bool, str]): Whether to only return the number of
            matching entries
        limit (Union[Unset, None, int]): Maximum number of objects to return
        page (Union[Unset, None, int]): Page number to return
        order_by (Union[Unset, None, str]): Field to order results by
        desc (Union[None, Unset, bool, str]): Whether to order results in descending order
        bust_cache (Union[None, Unset, bool, str]): Whether to bypass the cache and get the latest
            data
        created_date (Union[Unset, None, datetime.datetime]): Created date of items to return
        created_date_gte (Union[Unset, None, datetime.datetime]):
        created_date_lte (Union[Unset, None, datetime.datetime]):
        last_updated_date (Union[Unset, None, datetime.datetime]): Last edited date of items to
            return
        last_updated_date_gte (Union[Unset, None, datetime.datetime]):
        last_updated_date_lte (Union[Unset, None, datetime.datetime]):
        tags (Union[Unset, None, str]): Comma delimited list of tags on this device
        tags_contains (Union[Unset, None, str]):
        tags_contains_any (Union[Unset, None, str]):
        custom_attributes (Union[Unset, None,
            GetAccountRoleAccessCustomAttributes]): Do not set directly, use dot
            operators
        restricted_custom_attributes (Union[Unset, None,
            GetAccountRoleAccessRestrictedCustomAttributes]): Do not set
            directly, use dot operators
        ids_only (Union[None, Unset, bool, str]): Return list(s) of IDs only
        can_read (Union[Unset, None, bool]): Return only access for resources you can read
        can_update (Union[Unset, None, bool]): Return only access for resources you can update
        user_permissions_can_create (Union[Unset, None, bool]): User membership create permission
        user_permissions_can_read (Union[Unset, None, bool]): User membership read permission
        user_permissions_can_update (Union[Unset, None, bool]): User membership update permission
        user_permissions_can_delete (Union[Unset, None, bool]): User membership delete permission
        device_permissions_can_create (Union[Unset, None, bool]): Device membership create
            permissions
        device_permissions_can_read (Union[Unset, None, bool]): Device membership read permissions
        device_permissions_can_update (Union[Unset, None, bool]): Device membership update
            permissions
        device_permissions_can_delete (Union[Unset, None, bool]): Device membership delete
            permissions
        project_id (Union[Unset, None, str]): Only return group access under a specific project
        group_id (Union[Unset, None, str]): Only return role access under a specific group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['AccountRoleAccessList', 'AdminAccountRoleAccessList', 'RoleIdList']
    """

    return (
        await asyncio_detailed(
            client=client,
            is_active=is_active,
            is_delete_protected=is_delete_protected,
            created_by=created_by,
            last_updated_by=last_updated_by,
            search=search,
            search_fields=search_fields,
            page_count=page_count,
            object_count=object_count,
            limit=limit,
            page=page,
            order_by=order_by,
            desc=desc,
            bust_cache=bust_cache,
            created_date=created_date,
            created_date_gte=created_date_gte,
            created_date_lte=created_date_lte,
            last_updated_date=last_updated_date,
            last_updated_date_gte=last_updated_date_gte,
            last_updated_date_lte=last_updated_date_lte,
            tags=tags,
            tags_contains=tags_contains,
            tags_contains_any=tags_contains_any,
            custom_attributes=custom_attributes,
            restricted_custom_attributes=restricted_custom_attributes,
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
            project_id=project_id,
            group_id=group_id,
        )
    ).parsed
