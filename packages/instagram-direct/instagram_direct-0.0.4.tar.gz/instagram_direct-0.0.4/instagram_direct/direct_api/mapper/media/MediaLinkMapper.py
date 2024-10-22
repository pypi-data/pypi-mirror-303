from instagram_direct.direct_api.model.MediaLinkModel import MediaLinkModel


class MediaLinkMapper:

    @staticmethod
    def to_model(data: dict) -> MediaLinkModel:
        return MediaLinkModel(
            url=data["url"],
            width=data["width"],
            height=data["height"],
        )
