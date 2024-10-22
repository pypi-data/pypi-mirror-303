from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.success import Success
from ...models.upload_data_body import UploadDataBody
from ...types import Response


def _get_kwargs(
    group_id: str,
    path: str,
    *,
    body: UploadDataBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/v2/groups/{group_id}/data/{path}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: UploadDataBody,
) -> Response[Success]:
    """Put Json Data

     Post data by group ID and path

    Args:
        group_id (str):
        path (str):
        body (UploadDataBody): PUT/PATCH group data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Success]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        path=path,
        body=body,
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
    body: UploadDataBody,
) -> Optional[Success]:
    """Put Json Data

     Post data by group ID and path

    Args:
        group_id (str):
        path (str):
        body (UploadDataBody): PUT/PATCH group data

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
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
    body: UploadDataBody,
) -> Response[Success]:
    """Put Json Data

     Post data by group ID and path

    Args:
        group_id (str):
        path (str):
        body (UploadDataBody): PUT/PATCH group data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Success]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        path=path,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
    body: UploadDataBody,
) -> Optional[Success]:
    """Put Json Data

     Post data by group ID and path

    Args:
        group_id (str):
        path (str):
        body (UploadDataBody): PUT/PATCH group data

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
            body=body,
        )
    ).parsed
