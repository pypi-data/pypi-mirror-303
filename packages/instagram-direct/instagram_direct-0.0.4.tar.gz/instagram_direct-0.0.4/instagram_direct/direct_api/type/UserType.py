from typing import TypedDict, Optional, Any

from instagram_direct.direct_api.type.thread.ThreadUserFriendshipStatusType import ThreadUserFriendshipStatusType


class UserType(TypedDict):
    pk: str
    pk_id: str
    full_name: str
    username: str
    short_name: str
    profile_pic_url: str
    profile_pic_id: str
    has_anonymous_profile_picture: bool
    is_verified: bool
    interop_messaging_user_fbid: int
    fbid_v2: str
    has_ig_profile: bool
    interop_user_type: int
    is_using_unified_inbox_for_direct: bool
    is_eligible_for_rp_safety_notice: bool
    is_eligible_for_igd_stacks: bool
    is_private: bool
    is_creator_agent_enabled: bool
    has_highlight_reels: bool
    biz_user_inbox_state: int
    wa_eligibility: int
    wa_addressable: bool
    account_badges: list
    friendship_status: ThreadUserFriendshipStatusType
    is_shared_account: bool
    ai_agent_can_participate_in_audio_call: Optional[Any]
    ai_agent_can_participate_in_video_call: Optional[Any]
    strong_id__: str
