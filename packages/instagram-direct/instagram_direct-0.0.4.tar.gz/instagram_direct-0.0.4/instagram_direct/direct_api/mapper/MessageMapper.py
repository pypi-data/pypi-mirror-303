from datetime import datetime

from instagram_direct.direct_api.mapper.media.MediaShareMapper import MediaShareMapper
from instagram_direct.direct_api.mapper.clip.ClipMapper import ClipMapper
from instagram_direct.direct_api.mapper.media.PrivateMediaShareMapper import PrivateMediaShareMapper
from instagram_direct.direct_api.model.MessageModel import MessageModel
from instagram_direct.direct_api.type.message.MessageType import MessageType


class MessageMapper:

    @staticmethod
    def to_model(data: MessageType) -> MessageModel:
        item_type = data["item_type"]
        content = None
        if data.get("clip", None) is not None:
            content = ClipMapper.to_model(data["clip"]["clip"])
        if data.get("text", None) is not None:
            content = data["text"]
        if item_type == "media_share":
            content = MediaShareMapper.to_model(data["media_share"])
        if item_type == "generic_xma":
            content = PrivateMediaShareMapper.to_model(data["generic_xma"])
        # TODO add `media` type support
        return MessageModel(
            item_id=data["item_id"],
            message_id=data.get("message_id", None),
            user_id=data["user_id"],
            type=data["item_type"],
            datetime=datetime.fromtimestamp(int(data["timestamp"])/1000000),
            content=content
        )
