from dataclasses import dataclass

from instagram_direct.direct_api.model.audio.MusicArtistModel import MusicArtistModel


@dataclass
class MusicModel:
    id: str
    is_explicit: bool
    title: str
    subtitle: str
    download: dict
    audio_asset_id: str
    audio_cluster_id: str
    cover_url: str
    duration: int
    artist: MusicArtistModel
