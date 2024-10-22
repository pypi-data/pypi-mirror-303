from typing import TypedDict, Optional, Any


class ThreadPublicChatMetadataType(TypedDict):
    is_public: bool
    is_pinnable_to_viewer_profile: bool
    is_pinned_to_viewer_profile: bool
    is_added_to_inbox: bool
    is_subscribed_collaborator: bool
    channel_end_source: Optional[Any]
    is_comments_enabled: bool
    hidden_emojis: Optional[Any]
    channel_end_timestamp: int
    is_xposting_eligible: bool
    is_linked_account_eligible_for_xposting: bool
    xposting_available_channel_count: int
