from typing import TypedDict


class ClipCaptionType(TypedDict):
    bit_flags: int
    created_at: int
    created_at_utc: int
    did_report_as_spam: bool
    is_ranked_comment: bool
    pk: str
    share_enabled: bool
    content_type: str
    media_id: str
    status: str
    type: int
    user_id: str
    strong_id__: str
    text: str
