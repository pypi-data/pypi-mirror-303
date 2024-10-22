from typing import Optional

from instagram_direct.direct_api.model.audio.MusicArtistModel import MusicArtistModel
from instagram_direct.direct_api.model.audio.MusicModel import MusicModel


class MusicMapper:

    @staticmethod
    def to_model(music_info: dict) -> MusicModel:
        """

        :param music_info: in json 'music_info' as root
        :return:
        """
        music_consumption_info = music_info.get("music_consumption_info", {})
        data = music_info["music_asset_info"]
        download_links = {}
        for name in ["fast_start_progressive_download_url", "fast_start_progressive_download_url", "progressive_download_url", "reactive_audio_download_url", "web_30s_preview_download_url"]:
            founded = MusicMapper._find_download_link(data, name)
            if founded is not None:
                download_links.update(founded)

        return MusicModel(
            id=data["id"],
            is_explicit=data["is_explicit"],
            title=data["title"],
            subtitle=data["subtitle"],
            duration=data["duration_in_ms"],
            audio_asset_id=data["audio_asset_id"],
            audio_cluster_id=data["audio_cluster_id"],
            cover_url=data["cover_artwork_uri"],
            download=download_links,
            artist=MusicMapper.artist_to_model(data, music_consumption_info)
        )

    @staticmethod
    def artist_to_model(music_asset_info: dict, music_consumption_info: dict) -> MusicArtistModel:
        ig_artist = music_consumption_info.get("ig_artist")
        if ig_artist is None:
            ig_artist = {}
        return MusicArtistModel(
            id=music_asset_info["artist_id"],
            username=music_asset_info["ig_username"],
            display_artist=music_asset_info["display_artist"],
            full_name=ig_artist.get("full_name", None),
            is_verified=ig_artist.get("is_verified", None),
            profile_pic_url=ig_artist.get("profile_pic_url", None)
        )

    @staticmethod
    def _find_download_link(data: dict, name: str) -> Optional[dict]:
        if data.get(name, None) is not None:
            return {name: data[name]}
