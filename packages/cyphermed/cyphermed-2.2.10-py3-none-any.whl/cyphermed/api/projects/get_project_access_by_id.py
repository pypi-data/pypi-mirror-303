from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_project_access_info import AdminProjectAccessInfo
from ...models.project_access_info import ProjectAccessInfo
from ...types import Response


def _get_kwargs(
    project_id: str,
    grantee_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/projects/{project_id}/access/{grantee_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union["AdminProjectAccessInfo", "ProjectAccessInfo"]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(
            data: object,
        ) -> Union["AdminProjectAccessInfo", "ProjectAccessInfo"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = ProjectAccessInfo.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = AdminProjectAccessInfo.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union["AdminProjectAccessInfo", "ProjectAccessInfo"]]:
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
) -> Response[Union["AdminProjectAccessInfo", "ProjectAccessInfo"]]:
    """Get Project Access By Id

     Get a project access by ID

    Args:
        project_id (str):
        grantee_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['AdminProjectAccessInfo', 'ProjectAccessInfo']]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        grantee_id=grantee_id,
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
) -> Optional[Union["AdminProjectAccessInfo", "ProjectAccessInfo"]]:
    """Get Project Access By Id

     Get a project access by ID

    Args:
        project_id (str):
        grantee_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['AdminProjectAccessInfo', 'ProjectAccessInfo']
    """

    return sync_detailed(
        project_id=project_id,
        grantee_id=grantee_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    grantee_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union["AdminProjectAccessInfo", "ProjectAccessInfo"]]:
    """Get Project Access By Id

     Get a project access by ID

    Args:
        project_id (str):
        grantee_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['AdminProjectAccessInfo', 'ProjectAccessInfo']]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        grantee_id=grantee_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    grantee_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union["AdminProjectAccessInfo", "ProjectAccessInfo"]]:
    """Get Project Access By Id

     Get a project access by ID

    Args:
        project_id (str):
        grantee_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['AdminProjectAccessInfo', 'ProjectAccessInfo']
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            grantee_id=grantee_id,
            client=client,
        )
    ).parsed
