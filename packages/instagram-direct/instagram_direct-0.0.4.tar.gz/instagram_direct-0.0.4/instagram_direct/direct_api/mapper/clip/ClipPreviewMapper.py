from instagram_direct.direct_api.model.clip.ClipPreviewModel import ClipPreviewModel


class ClipPreviewMapper:

    @staticmethod
    def to_model(data: dict) -> ClipPreviewModel:
        return ClipPreviewModel(
            url=data["url"],
            width=data["width"],
            height=data["height"],
        )
