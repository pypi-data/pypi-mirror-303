from dataclasses import dataclass
from typing import Optional


@dataclass
class UserModel:
    pk: str
    pk_id: str
    username: str
    full_name: str
    profile_pic_url: str
    short_name: Optional[str] = None
