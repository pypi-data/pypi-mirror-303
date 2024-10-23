from typing import Literal

import aiohttp


class BaseService:
    def __init__(self, access_token: str) -> None:
        self.base_url = 'https://api.collinear.ai'
        self.access_token = access_token

    def set_access_token(self, access_token: str):
        """
        Sets the access token for the entire SDK.
        """
        self.access_token = access_token
        return self

    def get_headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

    async def send_request(self, url: str, method: Literal["POST", "GET", "PUT", "DELETE", "PATCH"] = "GET",
                           data: dict = None) -> dict:
        full_url = f"{self.base_url}{url}"
        async with aiohttp.ClientSession() as session:
            async with session.request(
                    method=method,
                    url=full_url,
                    headers=self.get_headers(),
                    json=data
            ) as response:
                try:
                    response_data = await response.json()
                    return response_data
                except Exception as e:
                    print(f"Failed to parse JSON response: {e}")
                    return {}
