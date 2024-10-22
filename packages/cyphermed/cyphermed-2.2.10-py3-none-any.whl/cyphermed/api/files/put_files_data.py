from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.files_url_for_path import FilesUrlForPath
from ...models.put_files_body import PutFilesBody
from ...models.success import Success
from ...types import Response


def _get_kwargs(
    group_id: str,
    path: str,
    *,
    body: PutFilesBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/v2/groups/{group_id}/files/{path}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union["FilesUrlForPath", "Success"]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(data: object) -> Union["FilesUrlForPath", "Success"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = FilesUrlForPath.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = Success.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union["FilesUrlForPath", "Success"]]:
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
    body: PutFilesBody,
) -> Response[Union["FilesUrlForPath", "Success"]]:
    """Put Files Data

     Create a pre-signed file upload URL

    Args:
        group_id (str):
        path (str):
        body (PutFilesBody): Which File fields to include in PUT request bodies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['FilesUrlForPath', 'Success']]
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
    body: PutFilesBody,
) -> Optional[Union["FilesUrlForPath", "Success"]]:
    """Put Files Data

     Create a pre-signed file upload URL

    Args:
        group_id (str):
        path (str):
        body (PutFilesBody): Which File fields to include in PUT request bodies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['FilesUrlForPath', 'Success']
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
    body: PutFilesBody,
) -> Response[Union["FilesUrlForPath", "Success"]]:
    """Put Files Data

     Create a pre-signed file upload URL

    Args:
        group_id (str):
        path (str):
        body (PutFilesBody): Which File fields to include in PUT request bodies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['FilesUrlForPath', 'Success']]
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
    body: PutFilesBody,
) -> Optional[Union["FilesUrlForPath", "Success"]]:
    """Put Files Data

     Create a pre-signed file upload URL

    Args:
        group_id (str):
        path (str):
        body (PutFilesBody): Which File fields to include in PUT request bodies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['FilesUrlForPath', 'Success']
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            path=path,
            client=client,
            body=body,
        )
    ).parsed
