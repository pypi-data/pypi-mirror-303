import requests
from bpkio_api.defaults import USER_AGENT_FOR_HANDLERS
from bpkio_api.exceptions import BroadpeakIoHelperError
from bpkio_api.models import MediaFormat
from loguru import logger

# Imports not used in the file, but necessary to ensure all handlers are loaded
from .dash import DASHHandler
from .generic import ContentHandler
from .hls import HLSHandler
from .jpeg import JPEGHandler
from .mp4 import MP4Handler
from .png import PNGHandler
from .vast import VASTHandler
from .vmap import VMAPHandler
from .xml import XMLHandler

# Registry for subclasses
_registry = {}


# Timeout for HEAD
timeout = 2


def all_subclasses(cls):
    return set(cls.__subclasses__()).union(
        [s for c in cls.__subclasses__() for s in all_subclasses(c)]
    )


for handler_cls in all_subclasses(ContentHandler):
    if hasattr(handler_cls, "media_format"):
        _registry[handler_cls.media_format] = handler_cls
    if hasattr(handler_cls, "content_types"):
        for content_type in handler_cls.content_types:
            _registry[content_type] = handler_cls
    if hasattr(handler_cls, "file_extensions"):
        for extension in handler_cls.file_extensions:
            _registry[extension] = handler_cls


def create_handler(
    url,
    get_full_content=False,
    from_url_only=False,
    user_agent=None,
    explicit_headers=[],
):
    url = url.strip()
    headers = {"User-Agent": user_agent or USER_AGENT_FOR_HANDLERS}

    if explicit_headers:
        for additional_header in explicit_headers:
            try:
                key, value = additional_header.split("=", 1)
            except ValueError:
                key, value = additional_header.split(":", 1)
            headers[key] = value.strip()

    try:
        content_type = ""
        if not from_url_only:
            try:
                response = requests.head(
                    url,
                    allow_redirects=True,
                    headers=headers,
                    timeout=timeout,
                    verify=ContentHandler.verify_ssl,
                )
                content_type = response.headers.get("content-type")
            except requests.exceptions.Timeout:
                logger.debug(f"HTTP HEAD takes more than {timeout} seconds, skipping.")
                content_type = "Unknown"

        # search extension
        media_format = MediaFormat.guess_from_url(url)

        handler_cls = _registry.get(content_type) or _registry.get(media_format)

        content = None
        if handler_cls is None:
            if from_url_only:
                raise ValueError(
                    "No information available in the URL to determine content type: "
                    f"{content_type} / {media_format}"
                )

            content = ContentHandler.fetch_content_with_size_limit(
                url=url,
                size_limit=200 * 1024,
                headers=headers,
                enforce_limit=(not get_full_content),
                timeout=timeout,
            )

            # Fallback: analyze content if handler is not found by content-type
            # or file extension
            if content:
                for handler in all_subclasses(ContentHandler):
                    if handler.is_supported_content(content):
                        handler_cls = handler
                        break

        if handler_cls is None:
            raise ValueError(
                "Could not determine content type from content-type, file extension, or content of URL: "
                f"- TYPE: {content_type} \n- FORMAT: {media_format} \n- CONTENT: {content}"
            )

        return handler_cls(url, content, headers=headers)

    except Exception as e:
        raise BroadpeakIoHelperError(
            message=f"Unable to determine a usable handler for url {url}",
            original_message=(
                e.args[0] if len(e.args) else getattr(e, "description", None)
            ),
        )
