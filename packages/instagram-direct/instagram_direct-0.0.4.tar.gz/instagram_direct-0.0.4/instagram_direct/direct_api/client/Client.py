from typing import Optional, Final

import aiohttp

from instagram_direct.direct_api.client import BASE_URL
from instagram_direct.exception.InstagramException import InstagramException
from instagram_direct.exception.InstagramRateLimitException import InstagramRateLimitException


class Client:

    _HEADERS: Final[dict] = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36",
        "x-ig-app-id": "1217981644879628"
    }

    def __init__(self, session_id: str):
        self._cookies = {
            "sessionid": session_id
        }

    async def get(self, endpoint: str, params: Optional[dict] = None) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    url=BASE_URL + endpoint,
                    params=params,
                    cookies=self._cookies,
                    headers=self._HEADERS,
                    ssl=False
            ) as response:
                if response.status == 200:
                    return await response.json()
                elif response.status == 429:
                    raise InstagramRateLimitException(f"{response.headers=}, {response=}")
                elif response.status == 400:
                    content = None
                    if response.headers["Content-Type"] == "application/json":
                        content = await response.text()
                    raise InstagramException(f"{response.headers=}, {response=}, {content=}")
                else:
                    raise Exception(f"{response=}, {response.headers=}")

    def post(self): ...
