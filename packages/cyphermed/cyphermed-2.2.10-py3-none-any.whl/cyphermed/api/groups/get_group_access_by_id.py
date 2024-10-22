from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_group_access_info import AdminGroupAccessInfo
from ...models.group_access_info import GroupAccessInfo
from ...types import Response


def _get_kwargs(
    group_id: str,
    grantee_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/groups/{group_id}/access/{grantee_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union["AdminGroupAccessInfo", "GroupAccessInfo"]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(data: object) -> Union["AdminGroupAccessInfo", "GroupAccessInfo"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = GroupAccessInfo.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = AdminGroupAccessInfo.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union["AdminGroupAccessInfo", "GroupAccessInfo"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    grantee_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union["AdminGroupAccessInfo", "GroupAccessInfo"]]:
    """Get Group Access By Id

     Get a group access by ID

    Args:
        group_id (str):
        grantee_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['AdminGroupAccessInfo', 'GroupAccessInfo']]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        grantee_id=grantee_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    grantee_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union["AdminGroupAccessInfo", "GroupAccessInfo"]]:
    """Get Group Access By Id

     Get a group access by ID

    Args:
        group_id (str):
        grantee_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['AdminGroupAccessInfo', 'GroupAccessInfo']
    """

    return sync_detailed(
        group_id=group_id,
        grantee_id=grantee_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    grantee_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union["AdminGroupAccessInfo", "GroupAccessInfo"]]:
    """Get Group Access By Id

     Get a group access by ID

    Args:
        group_id (str):
        grantee_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['AdminGroupAccessInfo', 'GroupAccessInfo']]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        grantee_id=grantee_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    grantee_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union["AdminGroupAccessInfo", "GroupAccessInfo"]]:
    """Get Group Access By Id

     Get a group access by ID

    Args:
        group_id (str):
        grantee_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['AdminGroupAccessInfo', 'GroupAccessInfo']
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            grantee_id=grantee_id,
            client=client,
        )
    ).parsed
