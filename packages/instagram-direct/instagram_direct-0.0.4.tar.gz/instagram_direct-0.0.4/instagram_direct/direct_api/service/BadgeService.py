from instagram_direct.direct_api.client.Client import Client
from instagram_direct.direct_api.type.response.BadgeResponse import BadgeResponse


class BadgeService:

    def __init__(self, session_id: str):
        self._client = Client(session_id)

    async def unread_count(self) -> int:
        response_json = await self._client.get("/get_badge_count/")
        badge_response = BadgeResponse(**response_json)
        return badge_response["badge_count"]
