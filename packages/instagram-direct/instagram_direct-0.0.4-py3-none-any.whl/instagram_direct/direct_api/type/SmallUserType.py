from typing import TypedDict


class SmallUserType(TypedDict):
    pk: str
    pk_id: str
    full_name: str
    username: str
    profile_pic_url: str
    profile_pic_id: str
    is_private: bool
    is_verified: bool
    is_unpublished: bool
    strong_id__: str
    fbid_v2: str
