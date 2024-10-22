from typing import TypedDict, List

from instagram_direct.direct_api.type.CursorType import CursorType
from instagram_direct.direct_api.type.thread.ThreadType import ThreadType


class InboxType(TypedDict):
    threads: List[ThreadType]
    has_older: bool
    unseen_count: int
    unseen_count_ts: int
    prev_cursor: CursorType
    next_cursor: CursorType
    pinned_threads: list
    blended_inbox_enabled: bool
