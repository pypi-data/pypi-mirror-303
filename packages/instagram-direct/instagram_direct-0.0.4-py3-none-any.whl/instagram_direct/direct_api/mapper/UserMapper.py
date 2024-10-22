from instagram_direct.direct_api.model.UserModel import UserModel
from instagram_direct.direct_api.type.UserType import UserType


class UserMapper:

    @staticmethod
    def to_model(data: UserType) -> UserModel:
        return UserModel(
            pk=data["pk"],
            pk_id=data["pk_id"],
            username=data["username"],
            full_name=data["full_name"],
            short_name=data.get("short_name", None),
            profile_pic_url=data["profile_pic_url"]
        )
