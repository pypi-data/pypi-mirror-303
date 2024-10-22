from typing import TypedDict, Optional


class ThreadNudgeType(TypedDict):
    create_time: Optional[str]
    nudge_type: int
