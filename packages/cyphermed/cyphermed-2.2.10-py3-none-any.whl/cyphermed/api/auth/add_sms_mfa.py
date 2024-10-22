from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_sms_mfa_form_params import AddSmsMfaFormParams
from ...models.sms_mfa_added import SmsMfaAdded
from ...types import Response


def _get_kwargs(
    form_data: AddSmsMfaFormParams,
) -> Dict[str, Any]:
    pass

    return {
        "method": "put",
        "url": "/v2/auth/mfa/sms",
        "data": form_data.to_dict(),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SmsMfaAdded]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SmsMfaAdded.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SmsMfaAdded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: AddSmsMfaFormParams,
) -> Response[SmsMfaAdded]:
    """Add Sms Mfa

     Register and verify MFA device using a generated TOTP code

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SmsMfaAdded]
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
    form_data: AddSmsMfaFormParams,
) -> Optional[SmsMfaAdded]:
    """Add Sms Mfa

     Register and verify MFA device using a generated TOTP code

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SmsMfaAdded
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    form_data: AddSmsMfaFormParams,
) -> Response[SmsMfaAdded]:
    """Add Sms Mfa

     Register and verify MFA device using a generated TOTP code

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SmsMfaAdded]
    """

    kwargs = _get_kwargs(
        form_data=form_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    form_data: AddSmsMfaFormParams,
) -> Optional[SmsMfaAdded]:
    """Add Sms Mfa

     Register and verify MFA device using a generated TOTP code

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SmsMfaAdded
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
        )
    ).parsed
