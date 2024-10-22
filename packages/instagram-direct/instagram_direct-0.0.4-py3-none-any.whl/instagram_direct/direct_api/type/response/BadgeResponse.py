from typing import TypedDict


class BadgeResponse(TypedDict):
    user_id: str
    badge_count: int
    seq_id: str
    badge_count_at_ms: int
    status: str
