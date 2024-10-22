from typing import TypedDict


class ViewerType(TypedDict):
    id: str
    pk: str
    pk_id: str
    full_name: str
    is_private: bool
    fbid_v2: str
    allowed_commenter_type: str
    reel_auto_archive: str
    has_onboarded_to_text_post_app: bool
    third_party_downloads_enabled: int
    strong_id__: str
    is_using_unified_inbox_for_direct: bool
    profile_pic_id: str
    profile_pic_url: str
    is_verified: bool
    username: str
    has_anonymous_profile_picture: bool
    all_media_count: int
    account_badges: list
    interop_messaging_user_fbid: str
    biz_user_inbox_state: int
    wa_addressable: bool
    wa_eligibility: int
    has_encrypted_backup: bool
