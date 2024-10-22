from typing import TypedDict, Optional, Any

from instagram_direct.direct_api.type.clip.ClipWrapType import ClipWrapType


class MessageType(TypedDict):
    item_id: str
    message_id: str
    user_id: str
    timestamp: int
    item_type: str
    client_context: str
    show_forward_attribution: bool
    forward_score: Optional[Any]
    is_shh_mode: bool
    otid: str
    is_ae_dual_send: bool
    is_ephemeral_exception: bool
    is_disappearing: bool
    is_superlative: bool
    is_replyable_in_bc: bool
    is_sent_by_viewer: bool
    paid_partnership_info: dict
    uq_seq_id: str
    latest_snooze_state: int
    one_click_upsell: Optional[Any]
    genai_params: dict
    text: Optional[str]
    clip: Optional[ClipWrapType]
    media_share: Optional[dict]
    generic_xma: Optional[list]
