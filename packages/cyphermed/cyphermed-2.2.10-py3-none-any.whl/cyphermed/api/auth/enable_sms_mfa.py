from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.enable_sms_mfa_form_params import EnableSmsMfaFormParams
from ...models.sms_mfa_added import SmsMfaAdded
from ...types import Response


def _get_kwargs(
    *,
    body: EnableSmsMfaFormParams,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/v2/auth/mfa/sms",
    }

    _body = body.to_dict()

    _kwargs["data"] = _body
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


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
    body: EnableSmsMfaFormParams,
) -> Response[SmsMfaAdded]:
    """Enable Sms Mfa

     Register and verify MFA device using a generated TOTP code

    Args:
        body (EnableSmsMfaFormParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SmsMfaAdded]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: EnableSmsMfaFormParams,
) -> Optional[SmsMfaAdded]:
    """Enable Sms Mfa

     Register and verify MFA device using a generated TOTP code

    Args:
        body (EnableSmsMfaFormParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SmsMfaAdded
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: EnableSmsMfaFormParams,
) -> Response[SmsMfaAdded]:
    """Enable Sms Mfa

     Register and verify MFA device using a generated TOTP code

    Args:
        body (EnableSmsMfaFormParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SmsMfaAdded]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: EnableSmsMfaFormParams,
) -> Optional[SmsMfaAdded]:
    """Enable Sms Mfa

     Register and verify MFA device using a generated TOTP code

    Args:
        body (EnableSmsMfaFormParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SmsMfaAdded
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
