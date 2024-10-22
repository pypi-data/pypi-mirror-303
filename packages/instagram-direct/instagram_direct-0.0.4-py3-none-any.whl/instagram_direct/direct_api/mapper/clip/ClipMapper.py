from instagram_direct.direct_api.mapper.clip.ClipPreviewMapper import ClipPreviewMapper
from instagram_direct.direct_api.mapper.clip.ClipVideoMapper import ClipVideoMapper
from instagram_direct.direct_api.model.clip.ClipModel import ClipModel
from instagram_direct.direct_api.type.clip.ClipType import ClipType


class ClipMapper:

    @staticmethod
    def to_model(data: ClipType) -> ClipModel:
        description = ""
        if data.get("caption", None) is not None:
            description = data.get("caption", {}).get("text", "")
        return ClipModel(
            code=data["code"],
            duration=data["video_duration"],
            has_audio=data["has_audio"],
            description=description,
            previews=[ClipPreviewMapper.to_model(preview) for preview in data["image_versions2"]["candidates"]],
            videos=[ClipVideoMapper.to_model(video) for video in data["video_versions"]]
        )
