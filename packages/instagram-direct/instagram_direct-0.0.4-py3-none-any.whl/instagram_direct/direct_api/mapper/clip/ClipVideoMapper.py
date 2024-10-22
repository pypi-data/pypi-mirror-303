from instagram_direct.direct_api.model.clip.ClipVideoModel import ClipVideoModel
from instagram_direct.direct_api.type.clip.VideoVersionType import VideoVersionType


class ClipVideoMapper:

    @staticmethod
    def to_model(data: VideoVersionType) -> ClipVideoModel:
        return ClipVideoModel(
            id=data["id"],
            height=data["height"],
            width=data["width"],
            url=data["url"]
        )
