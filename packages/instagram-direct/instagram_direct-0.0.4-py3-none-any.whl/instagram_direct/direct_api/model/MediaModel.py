from dataclasses import dataclass
from typing import List, Optional

from instagram_direct.direct_api.model.MediaLinkModel import MediaLinkModel


@dataclass
class MediaModel:
    id: str
    versions: List[MediaLinkModel]
    original_width: int
    original_height: int
    taken_at: Optional[int] = None
    preview: Optional[str] = None
