from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_role_access_info import AdminRoleAccessInfo
from ...models.role_access_info import RoleAccessInfo
from ...types import Response


def _get_kwargs(
    role_id: str,
    account_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/roles/{role_id}/access/{account_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union["AdminRoleAccessInfo", "RoleAccessInfo"]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(data: object) -> Union["AdminRoleAccessInfo", "RoleAccessInfo"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = RoleAccessInfo.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = AdminRoleAccessInfo.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union["AdminRoleAccessInfo", "RoleAccessInfo"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    role_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union["AdminRoleAccessInfo", "RoleAccessInfo"]]:
    """Get Role Access By Id

     Get a role access by ID

    Args:
        role_id (str):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['AdminRoleAccessInfo', 'RoleAccessInfo']]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    role_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union["AdminRoleAccessInfo", "RoleAccessInfo"]]:
    """Get Role Access By Id

     Get a role access by ID

    Args:
        role_id (str):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['AdminRoleAccessInfo', 'RoleAccessInfo']
    """

    return sync_detailed(
        role_id=role_id,
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    role_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union["AdminRoleAccessInfo", "RoleAccessInfo"]]:
    """Get Role Access By Id

     Get a role access by ID

    Args:
        role_id (str):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['AdminRoleAccessInfo', 'RoleAccessInfo']]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    role_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union["AdminRoleAccessInfo", "RoleAccessInfo"]]:
    """Get Role Access By Id

     Get a role access by ID

    Args:
        role_id (str):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['AdminRoleAccessInfo', 'RoleAccessInfo']
    """

    return (
        await asyncio_detailed(
            role_id=role_id,
            account_id=account_id,
            client=client,
        )
    ).parsed
