from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.success import Success
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: str,
    path: str,
    *,
    cascade: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["cascade"] = cascade

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/v2/groups/{group_id}/files/{path}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Success]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Success.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Success]:
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
) -> Response[Success]:
    """Delete Files Data

     Delete a file

    Args:
        group_id (str):
        path (str):
        cascade (Union[Unset, bool]): If true, delete all files in the directory

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Success]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        path=path,
        cascade=cascade,
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
) -> Optional[Success]:
    """Delete Files Data

     Delete a file

    Args:
        group_id (str):
        path (str):
        cascade (Union[Unset, bool]): If true, delete all files in the directory

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Success
    """

    return sync_detailed(
        group_id=group_id,
        path=path,
        client=client,
        cascade=cascade,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
    cascade: Union[Unset, bool] = UNSET,
) -> Response[Success]:
    """Delete Files Data

     Delete a file

    Args:
        group_id (str):
        path (str):
        cascade (Union[Unset, bool]): If true, delete all files in the directory

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Success]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        path=path,
        cascade=cascade,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
    cascade: Union[Unset, bool] = UNSET,
) -> Optional[Success]:
    """Delete Files Data

     Delete a file

    Args:
        group_id (str):
        path (str):
        cascade (Union[Unset, bool]): If true, delete all files in the directory

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Success
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            path=path,
            client=client,
            cascade=cascade,
        )
    ).parsed
