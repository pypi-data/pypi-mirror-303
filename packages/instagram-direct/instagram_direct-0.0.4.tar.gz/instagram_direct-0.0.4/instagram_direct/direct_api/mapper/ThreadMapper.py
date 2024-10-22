from instagram_direct.direct_api.mapper.MessageMapper import MessageMapper
from instagram_direct.direct_api.mapper.UserMapper import UserMapper
from instagram_direct.direct_api.model.CursorModel import CursorModel
from instagram_direct.direct_api.model.ThreadModel import ThreadModel
from instagram_direct.direct_api.type.thread.ThreadType import ThreadType


class ThreadMapper:

    @staticmethod
    def to_model(data: ThreadType) -> ThreadModel:
        return ThreadModel(
            id=data["thread_id"],
            users=[UserMapper.to_model(user) for user in data["users"]],
            messages=[MessageMapper.to_model(message) for message in data["items"]],
            cursor=CursorModel(
                next=data["next_cursor"],
                prev=data["prev_cursor"]
            )
        )
