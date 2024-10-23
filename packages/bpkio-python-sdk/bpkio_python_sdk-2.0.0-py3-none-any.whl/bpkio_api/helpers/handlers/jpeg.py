from bpkio_api.models import MediaFormat

from .generic import ContentHandler


class JPEGHandler(ContentHandler):
    media_format = MediaFormat.JPEG
    content_types = ["image/jpeg"]

    def __init__(self, url, content, **kwargs):
        self.url = url
        self.content = content

    def read(self):
        return "Handling JPEG file."

    @staticmethod
    def is_supported_content(content):
        # TODO - add handling by trying to open the image
        return False
