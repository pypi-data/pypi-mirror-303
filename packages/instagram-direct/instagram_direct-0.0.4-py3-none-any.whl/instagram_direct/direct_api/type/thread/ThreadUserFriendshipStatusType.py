from typing import TypedDict


class ThreadUserFriendshipStatusType(TypedDict):
    following: bool
    is_bestie: bool
    is_feed_favorite: bool
    is_restricted: bool
    outgoing_request: bool
    incoming_request: bool
    muting: bool
    blocking: bool
    is_messaging_pseudo_blocking: bool
    is_private: bool
    is_viewer_unconnected: bool
    reachability_status: int
