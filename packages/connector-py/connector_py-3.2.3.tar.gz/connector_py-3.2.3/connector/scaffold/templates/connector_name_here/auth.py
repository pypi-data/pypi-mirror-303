import httpx


class Auth(httpx.Auth):
    """Authorization schema for {name} API."""

    def __init__(self, access_token: str) -> None:
        self._access_token = access_token

    def auth_flow(self, request: httpx.Request):
        request.headers["Authorization"] = f"Bearer {{self._access_token}}"
        yield request
