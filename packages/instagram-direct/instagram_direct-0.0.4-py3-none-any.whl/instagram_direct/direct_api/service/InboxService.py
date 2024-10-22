from typing import List

from instagram_direct.direct_api.client.Client import Client
from instagram_direct.direct_api.mapper.ThreadMapper import ThreadMapper
from instagram_direct.direct_api.model.ThreadModel import ThreadModel
from instagram_direct.direct_api.type.response.InboxResponse import InboxResponse


class InboxService:

    def __init__(self, session_id: str):
        self._client = Client(session_id)

    async def all(self, limit: int = 10) -> List[ThreadModel]:
        # TODO Add limit support
        response_json = await self._client.get("/inbox/", params={"limit": limit})
        data = InboxResponse(**response_json)
        inbox_dict = data["inbox"]
        inbox_threads_list = inbox_dict["threads"]
        return [ThreadMapper.to_model(thread) for thread in inbox_threads_list]

    async def all_pending(self, limit: int = 10) -> List[ThreadModel]:
        # TODO Add limit support
        response_json = await self._client.get("/pending_inbox/", params={"limit": limit})
        data = InboxResponse(**response_json)
        inbox_dict = data["inbox"]
        inbox_threads_list = inbox_dict["threads"]
        return [ThreadMapper.to_model(thread) for thread in inbox_threads_list]
