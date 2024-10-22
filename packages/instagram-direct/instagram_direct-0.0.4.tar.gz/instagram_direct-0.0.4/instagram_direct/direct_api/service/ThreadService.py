from typing import Optional

from instagram_direct.direct_api.client.Client import Client
from instagram_direct.direct_api.mapper.ThreadMapper import ThreadMapper
from instagram_direct.direct_api.model.ThreadModel import ThreadModel
from instagram_direct.direct_api.type.response.ThreadResponse import ThreadResponse


class ThreadService:

    def __init__(self, session_id: str):
        self._client = Client(session_id)

    async def get(self, thread_id: str, cursor: Optional[str] = None, limit: int = 20) -> ThreadModel:
        params = {
            "limit": limit
        }
        if cursor is not None:
            params.update({
                "cursor": cursor
            })
        response_json = await self._client.get(f"/threads/{thread_id}/", params=params)
        data = ThreadResponse(**response_json)
        return ThreadMapper.to_model(data["thread"])

    def mute(self, thread_id: str): ...

    def unmute(self, thread_id: str): ...

    def leave(self, thread_id: str): ...

    def hide(self, thread_id: str): ...

    def move(self, thread_id: str): ...
