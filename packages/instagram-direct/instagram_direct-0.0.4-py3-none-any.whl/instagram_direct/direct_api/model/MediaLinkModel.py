from dataclasses import dataclass


@dataclass
class MediaLinkModel:
    url: str
    height: int
    width: int
