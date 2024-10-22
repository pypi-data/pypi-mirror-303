from dataclasses import dataclass


@dataclass
class ClipVideoModel:
    id: str
    height: int
    width: int
    url: str
