"""Base endpoint for the Luchtmeetnet API."""

from __future__ import annotations

import asyncio
import socket
from typing import TYPE_CHECKING, Mapping

from aiohttp import ClientError, ClientResponseError, ClientSession

from .const import ENDPOINT
from .exceptions import LuchtmeetNetConnectionError

if TYPE_CHECKING:
    from typing_extensions import Self


class HttpRequestClient:
    """Request Client for the LuchtmeetNet API."""

    endpoint = ENDPOINT
    session: ClientSession | None = None
    request_timeout: int = 10

    async def _make_request(
        self, path: str, params: dict[str, str | None] | None = None
    ) -> str:
        """Make request to api and return response."""
        if self.session is None:
            self.session = ClientSession()

        get_params: Mapping[str, str] | None = None
        if params is not None:
            get_params = {k: v for k, v in params.items() if v is not None}

        try:
            async with asyncio.timeout(self.request_timeout):
                url = f"{self.endpoint}/{path}"
                response = await self.session.get(url, params=get_params)
        except TimeoutError as exception:
            msg = "Timeout occurred while connecting to luchtmeetnet.nl"
            raise LuchtmeetNetConnectionError(msg) from exception
        except (
            ClientError,
            ClientResponseError,
            socket.gaierror,
        ) as exception:
            msg = "Error occurred while communicating with luchtmeetnet.nl"
            raise LuchtmeetNetConnectionError(msg) from exception

        if response.status != 200:
            content_type = response.headers.get("Content-Type", "")
            text = await response.text()
            msg = "Unexpected response from luchtmeetnet.nl"
            raise LuchtmeetNetConnectionError(
                msg,
                {"Content-Type": content_type, "response": text},
            )

        return await response.text()

    async def close(self) -> None:
        """Close the session."""
        if self.session is not None:
            await self.session.close()
            self.session = None

    async def __aenter__(self) -> Self:
        """Async enter."""
        return self

    async def __aexit__(self, *_exc_info: object) -> None:
        """Async exit."""
        await self.close()
