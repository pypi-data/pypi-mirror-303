from dataclasses import dataclass
from typing import List, Optional

from instagram_direct.direct_api.model.MediaModel import MediaModel
from instagram_direct.direct_api.model.UserModel import UserModel
from instagram_direct.direct_api.model.audio.MusicModel import MusicModel


@dataclass
class MediaShareModel:
    id: str
    pk: str
    taken_at: int
    code: str
    autor: UserModel
    like_count: int
    carousel: List[MediaModel]
    description: Optional[str] = None
    audio: Optional[MusicModel] = None
