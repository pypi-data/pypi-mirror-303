from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Union

from instagram_direct.direct_api.model.clip.ClipModel import ClipModel


@dataclass
class MessageModel:
    item_id: str
    user_id: str
    type: str
    datetime: datetime
    message_id: Optional[str] = None
    content: Optional[Union[str, ClipModel]] = None
