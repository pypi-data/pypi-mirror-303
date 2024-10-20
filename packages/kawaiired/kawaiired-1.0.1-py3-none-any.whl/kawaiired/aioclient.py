import random
from types import TracebackType

import httpx

from kawaiired.exceptions import APIException
from kawaiired.utils import BASE_URL, EndpointType, GifType, Stats


class KawaiiAioClient:
    """Wrapper Async Client for the kawaii.red API."""

    def __init__(self, token: str, base_url: str = BASE_URL) -> None:
        """
        Initialize the client.

        Args:
            token (str): The token to use for the API.
            base_url (str): The base URL to use for the API.
        """
        self.token = token
        self.base_url = base_url
        self.session = httpx.AsyncClient(headers={"token": self.token})

    async def __aexit__(self, exc_type: type[Exception], exc_val: Exception, exc_tb: TracebackType) -> None:
        await self.close()

    async def close(self) -> None:
        """Close the client session."""
        if self.session is not None:
            await self.session.aclose()

    async def _request(self, endpoint: EndpointType, category: str) -> str | None:
        """
        Make a request to the API and return the response.

        Args:
            endpoint (EndpointType): The endpoint to make the request to.
            category (str): The category to make the request to.

        Returns:
            Optional[str]: The response from the API, or None if not found.

        Raises:
            APIException: If the request fails.
        """
        url = f"{self.base_url}/{endpoint}/{category}"
        try:
            response = await self.session.get(url)
            response.raise_for_status()
            if response.json().get("error"):
                raise APIException(
                    401,
                    "Unauthorized",
                    response.json().get("error"),
                )
            return response.json().get("response")
        except httpx.HTTPStatusError as e:
            raise APIException(e.response.status_code, e.response.reason_phrase, e.response.text) from e

    async def get(self, endpoint: EndpointType, category: str) -> str | None:
        """
        Get a response from the API.

        Args:
            endpoint (EndpointType): The endpoint to make the request to.
            category (str): The category to make the request to.

        Returns:
            Optional[str]: The response from the API, or None if not found.
        """
        return await self._request(endpoint, category)

    async def gif(self, category: GifType) -> str | None:
        """
        Get a GIF from the API.

        Args:
            category (str): The category to make the request to.

        Returns:
            Optional[str]: The GIF URL, or None if not found.
        """
        return await self._request("gif", category)

    async def image(self, category: str) -> str | None:
        """
        Get an image from the API.

        Args:
            category (str): The category to make the request to.

        Returns:
            Optional[str]: The image URL, or None if not found.
        """
        raise NotImplementedError("This endpoint is not implemented yet.")

    async def text(self, category: str) -> str | None:
        """
        Get text from the API.

        Args:
            category (str): The category to make the request to.

        Returns:
            Optional[str]: The text response, or None if not found.
        """
        raise NotImplementedError("This endpoint is not implemented yet.")

    async def endpoints(self, endpoint: EndpointType) -> list[str] | None:
        """
        Get the endpoints from the API.

        Returns:
            Optional[list[str]]: The endpoints from the API, or None if not found.
        """
        return await self._request(endpoint, "endpoints")

    async def random(self, endpoint: EndpointType) -> str | None:
        """
        Get a random item from the API.

        Returns:
            Optional[str]: The random item from the API, or None if not found.
        """
        categorie = random.choice(await self.endpoints(endpoint))
        return await self._request(endpoint, categorie)

    async def stats(self) -> Stats | None:
        """
        Get the stats from the API.

        Returns:
            Optional[Stats]: The stats from the API, or None if not found.
        """
        if self.token == "anonymous":  # noqa: S105
            raise APIException(403, "Forbidden", "Stats are not available for anonymous users.")

        endpoints = await self._request("stats", "endpoints")
        if not endpoints:
            return None

        stats = {"endpoints": endpoints}
        stats.update({endpoint: await self._request("stats", endpoint) for endpoint in endpoints})

        return Stats(**stats)
