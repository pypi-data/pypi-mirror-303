from dataclasses import dataclass
from typing import List, Optional

from instagram_direct.direct_api.model.clip.ClipPreviewModel import ClipPreviewModel
from instagram_direct.direct_api.model.clip.ClipVideoModel import ClipVideoModel


@dataclass
class ClipModel:
    code: str
    duration: float
    has_audio: bool
    description: Optional[str]
    previews: List[ClipPreviewModel]
    videos: List[ClipVideoModel]
