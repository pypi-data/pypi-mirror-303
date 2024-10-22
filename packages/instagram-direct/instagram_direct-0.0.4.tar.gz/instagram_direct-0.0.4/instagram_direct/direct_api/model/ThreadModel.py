from dataclasses import dataclass
from typing import List

from instagram_direct.direct_api.model.CursorModel import CursorModel
from instagram_direct.direct_api.model.MessageModel import MessageModel
from instagram_direct.direct_api.model.UserModel import UserModel


@dataclass
class ThreadModel:
    id: str
    users: List[UserModel]
    messages: List[MessageModel]
    cursor: CursorModel
