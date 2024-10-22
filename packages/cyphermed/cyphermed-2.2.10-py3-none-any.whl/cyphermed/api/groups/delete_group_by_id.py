from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.success import Success
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: str,
    *,
    permanent: Union[Unset, bool] = UNSET,
    force: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["permanent"] = permanent

    params["force"] = force

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/v2/groups/{group_id}",
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
    *,
    client: AuthenticatedClient,
    permanent: Union[Unset, bool] = UNSET,
    force: Union[Unset, bool] = UNSET,
) -> Response[Success]:
    """Delete Group By Id

     Delete a group by ID

    Args:
        group_id (str):
        permanent (Union[Unset, bool]): If true, the group will be permanently deleted
        force (Union[Unset, bool]): (Admin only) Delete even if it is protected

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Success]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        permanent=permanent,
        force=force,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    *,
    client: AuthenticatedClient,
    permanent: Union[Unset, bool] = UNSET,
    force: Union[Unset, bool] = UNSET,
) -> Optional[Success]:
    """Delete Group By Id

     Delete a group by ID

    Args:
        group_id (str):
        permanent (Union[Unset, bool]): If true, the group will be permanently deleted
        force (Union[Unset, bool]): (Admin only) Delete even if it is protected

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Success
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        permanent=permanent,
        force=force,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
    permanent: Union[Unset, bool] = UNSET,
    force: Union[Unset, bool] = UNSET,
) -> Response[Success]:
    """Delete Group By Id

     Delete a group by ID

    Args:
        group_id (str):
        permanent (Union[Unset, bool]): If true, the group will be permanently deleted
        force (Union[Unset, bool]): (Admin only) Delete even if it is protected

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Success]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        permanent=permanent,
        force=force,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient,
    permanent: Union[Unset, bool] = UNSET,
    force: Union[Unset, bool] = UNSET,
) -> Optional[Success]:
    """Delete Group By Id

     Delete a group by ID

    Args:
        group_id (str):
        permanent (Union[Unset, bool]): If true, the group will be permanently deleted
        force (Union[Unset, bool]): (Admin only) Delete even if it is protected

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Success
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            permanent=permanent,
            force=force,
        )
    ).parsed
