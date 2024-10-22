from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_project_access_body import CreateProjectAccessBody
from ...models.success import Success
from ...types import Response


def _get_kwargs(
    project_id: str,
    grantee_id: str,
    *,
    body: CreateProjectAccessBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/v2/projects/{project_id}/access/{grantee_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Success]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Success.from_dict(response.json())

        return response_201
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
    project_id: str,
    grantee_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateProjectAccessBody,
) -> Response[Success]:
    """Create Project Access

     Add access for a project

    Args:
        project_id (str):
        grantee_id (str):
        body (CreateProjectAccessBody): Which ProjectAccess fields to include in PATCH request
            bodies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Success]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        grantee_id=grantee_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    grantee_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateProjectAccessBody,
) -> Optional[Success]:
    """Create Project Access

     Add access for a project

    Args:
        project_id (str):
        grantee_id (str):
        body (CreateProjectAccessBody): Which ProjectAccess fields to include in PATCH request
            bodies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Success
    """

    return sync_detailed(
        project_id=project_id,
        grantee_id=grantee_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    grantee_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateProjectAccessBody,
) -> Response[Success]:
    """Create Project Access

     Add access for a project

    Args:
        project_id (str):
        grantee_id (str):
        body (CreateProjectAccessBody): Which ProjectAccess fields to include in PATCH request
            bodies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Success]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        grantee_id=grantee_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    grantee_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateProjectAccessBody,
) -> Optional[Success]:
    """Create Project Access

     Add access for a project

    Args:
        project_id (str):
        grantee_id (str):
        body (CreateProjectAccessBody): Which ProjectAccess fields to include in PATCH request
            bodies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Success
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            grantee_id=grantee_id,
            client=client,
            body=body,
        )
    ).parsed
