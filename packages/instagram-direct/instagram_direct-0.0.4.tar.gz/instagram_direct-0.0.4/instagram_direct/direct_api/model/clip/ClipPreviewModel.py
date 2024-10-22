from dataclasses import dataclass


@dataclass
class ClipPreviewModel:
    url: str
    height: int
    width: int
