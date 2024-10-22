from dataclasses import dataclass
from typing import Optional


@dataclass
class MusicArtistModel:
    id: str
    username: str
    display_artist: str
    full_name: Optional[str] = None
    is_verified: Optional[bool] = None
    profile_pic_url: Optional[str] = None
