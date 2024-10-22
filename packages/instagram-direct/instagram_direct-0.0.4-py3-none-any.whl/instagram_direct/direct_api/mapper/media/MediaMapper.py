from instagram_direct.direct_api.mapper.media.MediaLinkMapper import MediaLinkMapper
from instagram_direct.direct_api.model.MediaModel import MediaModel


class MediaMapper:

    @staticmethod
    def to_model(data: dict) -> MediaModel:
        return MediaModel(
            id=data["id"],
            taken_at=data["taken_at"],
            original_width=data["original_width"],
            original_height=data["original_height"],
            preview=data["preview"],
            versions=[MediaLinkMapper.to_model(version) for version in data["image_versions2"]["candidates"]]
        )
