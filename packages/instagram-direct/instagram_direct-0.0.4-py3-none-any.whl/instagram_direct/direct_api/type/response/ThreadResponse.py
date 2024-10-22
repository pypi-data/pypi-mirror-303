from typing import TypedDict

from instagram_direct.direct_api.type.thread.ThreadType import ThreadType


class ThreadResponse(TypedDict):
    thread: ThreadType
    status: str
