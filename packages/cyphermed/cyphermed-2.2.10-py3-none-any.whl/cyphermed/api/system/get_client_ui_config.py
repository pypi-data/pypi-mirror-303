from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_interface_info import ClientInterfaceInfo
from ...types import Response


def _get_kwargs(
    client_id_or_alias: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/ui/{client_id_or_alias}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ClientInterfaceInfo]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ClientInterfaceInfo.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ClientInterfaceInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_id_or_alias: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ClientInterfaceInfo]:
    """Get Client Ui Config

     Get client configuration for a given client ID

    Args:
        client_id_or_alias (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClientInterfaceInfo]
    """

    kwargs = _get_kwargs(
        client_id_or_alias=client_id_or_alias,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    client_id_or_alias: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ClientInterfaceInfo]:
    """Get Client Ui Config

     Get client configuration for a given client ID

    Args:
        client_id_or_alias (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClientInterfaceInfo
    """

    return sync_detailed(
        client_id_or_alias=client_id_or_alias,
        client=client,
    ).parsed


async def asyncio_detailed(
    client_id_or_alias: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ClientInterfaceInfo]:
    """Get Client Ui Config

     Get client configuration for a given client ID

    Args:
        client_id_or_alias (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClientInterfaceInfo]
    """

    kwargs = _get_kwargs(
        client_id_or_alias=client_id_or_alias,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    client_id_or_alias: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ClientInterfaceInfo]:
    """Get Client Ui Config

     Get client configuration for a given client ID

    Args:
        client_id_or_alias (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClientInterfaceInfo
    """

    return (
        await asyncio_detailed(
            client_id_or_alias=client_id_or_alias,
            client=client,
        )
    ).parsed
