from dataclasses import dataclass
from typing import List, Optional

from instagram_direct.direct_api.model.MediaModel import MediaModel


@dataclass
class PrivateMediaShare:
    carousel: List[MediaModel]
