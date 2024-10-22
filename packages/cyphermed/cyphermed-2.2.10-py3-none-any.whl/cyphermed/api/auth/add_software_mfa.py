from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_software_mfa_form_params import AddSoftwareMfaFormParams
from ...models.software_mfa_added import SoftwareMfaAdded
from ...types import Response


def _get_kwargs(
    form_data: AddSoftwareMfaFormParams,
) -> Dict[str, Any]:
    pass

    return {
        "method": "put",
        "url": "/v2/auth/mfa/software",
        "data": form_data.to_dict(),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SoftwareMfaAdded]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SoftwareMfaAdded.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SoftwareMfaAdded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: AddSoftwareMfaFormParams,
) -> Response[SoftwareMfaAdded]:
    """Add Software Mfa

     Register and verify MFA device using a generated TOTP code

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SoftwareMfaAdded]
    """

    kwargs = _get_kwargs(
        form_data=form_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    form_data: AddSoftwareMfaFormParams,
) -> Optional[SoftwareMfaAdded]:
    """Add Software Mfa

     Register and verify MFA device using a generated TOTP code

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SoftwareMfaAdded
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    form_data: AddSoftwareMfaFormParams,
) -> Response[SoftwareMfaAdded]:
    """Add Software Mfa

     Register and verify MFA device using a generated TOTP code

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SoftwareMfaAdded]
    """

    kwargs = _get_kwargs(
        form_data=form_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    form_data: AddSoftwareMfaFormParams,
) -> Optional[SoftwareMfaAdded]:
    """Add Software Mfa

     Register and verify MFA device using a generated TOTP code

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SoftwareMfaAdded
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
        )
    ).parsed
