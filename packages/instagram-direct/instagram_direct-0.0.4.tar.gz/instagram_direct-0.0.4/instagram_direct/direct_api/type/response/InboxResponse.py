from typing import TypedDict

from instagram_direct.direct_api.type.InboxType import InboxType
from instagram_direct.direct_api.type.ViewerType import ViewerType


class InboxResponse(TypedDict):
    viewer: ViewerType
    inbox: InboxType
    seq_id: str
    snapshot_at_ms: int
    pending_requests_total: int
    has_pending_top_requests: bool
    status: str
