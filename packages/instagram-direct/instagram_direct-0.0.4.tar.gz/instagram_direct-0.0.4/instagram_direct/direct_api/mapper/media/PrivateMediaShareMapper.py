from instagram_direct.direct_api.model.MediaLinkModel import MediaLinkModel
from instagram_direct.direct_api.model.MediaModel import MediaModel
from instagram_direct.direct_api.model.PrivateMediaShare import PrivateMediaShare


class PrivateMediaShareMapper:

    @staticmethod
    def to_model(data: list) -> PrivateMediaShare:
        """
        :param data: `generic_xma` as root
        """
        carousel = []
        for item in data:
            preview_url_info = item["preview_url_info"]
            carousel.append(MediaModel(
                id=item["preview_media_fbid"],
                original_height=item["original_image_height"],
                original_width=item["original_image_width"],
                versions=[MediaLinkModel(
                    url=preview_url_info["url"],
                    width=preview_url_info["width"],
                    height=preview_url_info["height"]
                )]
            ))
        return PrivateMediaShare(
            carousel=carousel
        )
