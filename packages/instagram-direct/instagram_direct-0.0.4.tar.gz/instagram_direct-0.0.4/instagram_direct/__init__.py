from instagram_direct.direct_api.service.BadgeService import BadgeService
from instagram_direct.direct_api.service.InboxService import InboxService
from instagram_direct.direct_api.service.ThreadService import ThreadService


class InstagramDirect:

    def __init__(self, session_id: str):
        self._session_id = session_id

    @property
    def inbox(self) -> InboxService:
        return InboxService(session_id=self._session_id)

    @property
    def thread(self) -> ThreadService:
        return ThreadService(session_id=self._session_id)

    @property
    def badge(self) -> BadgeService:
        return BadgeService(session_id=self._session_id)
