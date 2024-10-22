from typing import Optional

from instagram_direct.direct_api.mapper.media.MediaLinkMapper import MediaLinkMapper
from instagram_direct.direct_api.mapper.media.MediaMapper import MediaMapper
from instagram_direct.direct_api.mapper.MusicMapper import MusicMapper
from instagram_direct.direct_api.mapper.UserMapper import UserMapper
from instagram_direct.direct_api.model.MediaModel import MediaModel
from instagram_direct.direct_api.model.MediaShareModel import MediaShareModel


class MediaShareMapper:

    @staticmethod
    def to_model(data: dict) -> MediaShareModel:
        carousel_media: Optional[list] = data.get("carousel_media", None)
        carousel = []
        if carousel_media is not None:
            carousel = [MediaMapper.to_model(media) for media in carousel_media]
        media: Optional[dict] = data.get("image_versions2", None)
        if carousel_media is None and media is not None:
            carousel.append(MediaModel(
                id=data["id"],
                taken_at=data["taken_at"],
                original_width=data["original_width"],
                original_height=data["original_height"],
                preview=None,
                versions=[MediaLinkMapper.to_model(version) for version in media["candidates"]]
            ))
        music_metadata = data.get("music_metadata", {})
        music_info: Optional[dict] = music_metadata.get("music_info", None)
        audio = None
        if music_info is not None:
            audio = MusicMapper.to_model(music_info)
        caption = data.get("caption", {})
        return MediaShareModel(
            id=data["id"],
            pk=data["pk"],
            taken_at=data["taken_at"],
            code=data["code"],
            like_count=data["like_count"],
            autor=UserMapper.to_model(data["owner"]),
            carousel=carousel,
            audio=audio,
            description=caption.get("text", None)
        )
