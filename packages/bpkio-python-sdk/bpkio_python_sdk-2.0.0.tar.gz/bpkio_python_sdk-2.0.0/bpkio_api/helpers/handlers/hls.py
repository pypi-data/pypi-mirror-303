from functools import lru_cache
from typing import Dict, List
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

import m3u8
from bpkio_api.exceptions import BroadpeakIoHelperError
from bpkio_api.helpers.codecstrings import CodecStringParser
from bpkio_api.helpers.handlers.generic import ContentHandler
from bpkio_api.helpers.times import seconds_to_timecode
from bpkio_api.models import MediaFormat


class HLSHandler(ContentHandler):
    media_format = MediaFormat.HLS
    content_types = ["application/x-mpegurl", "application/vnd.apple.mpegurl"]

    def __init__(self, url, content: bytes | None = None, **kwargs):
        super().__init__(url, content, **kwargs)
        self._document: m3u8.M3U8 = None

    @property
    def document(self) -> m3u8.M3U8:
        if not self._document:
            try:
                self._document = m3u8.loads(content=self.content.decode(), uri=self.url)
            except Exception as e:
                raise BroadpeakIoHelperError(
                    message="The HLS manifest could not be parsed",
                    original_message=e.args[0],
                )
        return self._document

    def read(self):
        return "Handling HLS file."

    @staticmethod
    def is_supported_content(content):
        return content.decode().startswith("#EXTM3U")

    def appears_supported(self) -> bool:
        return self.is_supported_content(self.content)

    def has_children(self) -> bool:
        if self.document.is_variant:
            return True
        return False

    def get_child(self, index: int, additional_query_params: dict = {}):
        playlists = self.document.playlists + self.document.media

        child_url = playlists[index - 1].absolute_uri
        if additional_query_params:
            child_url = self._add_query_parameters_from_dict(
                child_url, additional_query_params
            )

        try:
            return HLSHandler(
                url=child_url, headers=self.headers,
            )
        except IndexError as e:
            raise BroadpeakIoHelperError(
                message=f"The HLS manifest only has {len(self.document.playlists)} renditions.",
                original_message=e.args[0],
            )

    @staticmethod
    def _add_query_parameters_from_dict(url: str, new_params: dict):
        parsed_url = urlparse(url)

        # Parse the existing query parameters
        query_params = parse_qs(parsed_url.query)

        # Add the new query parameter
        for key, value in new_params.items():
            query_params[key] = value

        # Reconstruct the query string
        new_query = urlencode(query_params, doseq=True)

        # Reconstruct the full URL with the new query string
        new_url = urlunparse(parsed_url._replace(query=new_query))

        return new_url

    @lru_cache()
    def _fetch_sub(self, uri):
        try:
            return m3u8.load(
                uri,
                headers=self.headers,
                verify_ssl=(
                    True if self.verify_ssl is True else False
                ),  # TODO - ability to set exact CERT. See https://github.com/globocom/m3u8?tab=readme-ov-file#using-different-http-clients
            )
        except Exception as e:
            raise BroadpeakIoHelperError(
                message=f"The HLS media playlist could not be parsed: {uri}",
                original_message=e.args[0] if e.args and len(e.args) else str(e),
            )

    def protocol_version(self):
        """Returns the protocol version of the HLS

        Returns:
            str
        """
        return self.document.version

    def is_live(self):
        """Checks if the HLS is a live stream (ie. without an end)

        Returns:
            bool
        """
        # Check the first sub-playlist
        if len(self.document.playlists):
            sub = self._fetch_sub(self.document.playlists[0].absolute_uri)
            if not sub.is_endlist:  # type: ignore
                return True
            else:
                return False

        else:
            return not self.document.is_endlist

    def get_duration(self):
        """Calculates the duration of the stream (in seconds)

        Returns:
            int
        """
        if self.is_live():
            return -1
        else:
            sub = self._fetch_sub(self.document.playlists[0].absolute_uri)
            return sum([seg.duration for seg in sub.segments])

    def num_segments(self):
        """Calculates the number of segments in the stream

        Returns:
            int
        """
        sub = self._fetch_sub(self.document.playlists[0].absolute_uri)
        return len(sub.segments)

    def container_format(self):
        """Checks the container format of the segments

        Returns:
            str
        """
        if len(self.document.playlists) == 0:
            raise BroadpeakIoHelperError(
                "There seem to be no playlists in this manifest"
            )
        sub = self._fetch_sub(self.document.playlists[0].absolute_uri)

        # We just check if there is a segment map
        if len(sub.segment_map):
            return "ISOBMFF"
        else:
            return "MPEG-TS"

    def has_muxed_audio(self) -> bool:
        """Checks is the audio stream is muxed in with video

        Returns:
            bool
        """
        # TODO - 2 additional use cases:
        #  - video only
        #  - audio only (no video)

        # If there is no media, then must be muxed
        if len(self.document.media) == 0:
            return True

        # Otherwise, if the media doesn't have a URI, then must be muxed
        for media in self.document.media:
            if media.type == "AUDIO":
                if media.uri is None:
                    return True
        return False

    def has_audio_only(self) -> bool:
        for playlist in self.document.playlists:
            # extract info from codecs
            cdc = CodecStringParser.parse_multi_codec_string(
                playlist.stream_info.codecs
            )
            # find any rendition without a video codec
            cdc_v = next((d for d in cdc if d.get("type") == "video"), None)
            if not cdc_v:
                return True
        return False

    def target_duration(self):
        if self.has_children():
            sub = self._fetch_sub(self.document.playlists[0].absolute_uri)
            return sub.target_duration
        else:
            return self.document.target_duration

    def get_update_interval(self):
        return self.target_duration()

    def extract_info(self) -> Dict:
        info = {
            "format": "HLS",
            "version": self.protocol_version(),
            "type": "Live" if self.is_live() else "VOD",
            "container": self.container_format(),
            "audio_only": self.has_audio_only(),
            "target_duration": self.target_duration(),
            "duration": (
                "(live)" if self.is_live() else seconds_to_timecode(self.get_duration())
            ),
            "duration (sec)": (
                "(live)" if self.is_live() else f"{self.get_duration():.3f}"
            ),
            "segments": self.num_segments(),
        }

        return info

    def get_segment_for_url(self, url):
        for segment in self.document.segments:
            if segment.uri == url:
                return segment

    def extract_features(self) -> List[Dict]:
        """Extracts essential information from the HLS manifest"""
        arr = []
        index = 0

        if self.document.is_variant:
            for playlist in self.document.playlists:
                index += 1

                si = playlist.stream_info

                data = dict(
                    index=index,
                    type="variant",
                    uri=playlist.uri,
                    # url=playlist.absolute_uri,
                    codecs=si.codecs,
                )

                # extract info from codecs
                cdc = CodecStringParser.parse_multi_codec_string(si.codecs)
                cdc_v = next((d for d in cdc if d.get("type") == "video"), None)
                cdc_a = next((d for d in cdc if d.get("type") == "audio"), None)

                if cdc_a:
                    data["codeca"] = cdc_a["cc"]
                if cdc_v:
                    data["codecv"] = cdc_v["cc"]
                    data["profilev"] = cdc_v["profile"]
                    data["levelv"] = cdc_v["level"]

                res = (
                    "{} x {}".format(
                        si.resolution[0],
                        si.resolution[1],
                    )
                    if si.resolution
                    else ""
                )
                data["resolution"] = res
                data["bandwidth"] = si.bandwidth

                data["uri_short"] = shorten_url(playlist.uri)

                arr.append(data)

            for media in self.document.media:
                if media.uri:
                    index += 1
                    data = dict(
                        index=index,
                        type="media",
                        uri=media.uri,
                        language=media.language,
                        # url=media.absolute_uri,
                        uri_short=shorten_url(media.uri),
                    )

                    arr.append(data)

        return arr


def shorten_url(uri):
    u = urlparse(uri)
    shortened_url = u.path[-50:]
    if u.query:
        shortened_url += "?..."
    return shortened_url
