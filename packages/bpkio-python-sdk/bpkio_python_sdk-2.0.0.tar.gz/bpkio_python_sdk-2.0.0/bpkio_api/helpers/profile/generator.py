from fractions import Fraction
from importlib.metadata import version

from .analyser import ErrorMessage, InfoMessage, WarningMessage


class TranscodingProfileGenerator:
    config = dict(preset="veryfast", schema="bkt-v2", framerate=25)

    def __init__(self, schema=1, **kwargs) -> None:
        self.config["schema"] = 1 if schema is None else schema
        for k in kwargs:
            self.config[k] = kwargs[k]

        self.messages = []

    def generate(self, renditions, packaging, name: str = ""):
        if self.config["schema"] == "bkt-v1":
            return self.generate_bkt_v1(renditions, packaging)
        elif self.config["schema"] == "bkt-v2":
            return self.generate_bkt_v2(renditions, packaging, name)
        else:
            raise Exception("Unknown profile version")

    def generate_bkt_v1(self, renditions, packaging):
        common = {
            "codecv": "h264",
            "preset": self.config["preset"],
        }

        video_frame_rate = None
        audio_sample_rate = None

        jobs = []
        for r in renditions:
            if r["type"] == "video":
                video_frame_rate = r["framerate"]
                jobs.append(
                    {
                        "level": str(r["level"]),
                        # -2 seems to ensure that the calculated width is divisible by 2, a constraint of libx264
                        "scale": f"-2:{r['resolution'][1]}",
                        "bitratev": str(r["bitrate"]),
                        "profilev": r["profile"],
                        "frameratev": str(r["framerate"]) if r["framerate"] else "",
                    }
                )

            if r["type"] == "audio":
                audio_sample_rate = 48000
                audio_spec = {
                    "codeca": "aac",
                    "frameratea": "48000",
                    "bitratea": str(r["bitrate"]),
                    "loudnorm": "I=-23:TP=-1",
                }

                # if r.get("muxed") is True:
                #     common.update(audio_spec)

                # else:
                #     jobs.append(audio_spec)

                common.update(audio_spec)

        target_segment_duration = packaging.get("segment_duration", 4)
        if float(target_segment_duration) == int(target_segment_duration):
            target_segment_duration = int(target_segment_duration)

        # Validate the segment duration size
        muxed_audio = packaging.get("muxed_audio")
        container = packaging.get("container")
        if (container == "MPEG-TS" and not muxed_audio) or container == "ISOBMFF":
            self.messages.append(
                WarningMessage(
                    "Since audio renditions are separate from video, you should ensure that your segment size is compatible between audio rate and video frame rate"
                )
            )

        if video_frame_rate:
            if float(video_frame_rate) == int(video_frame_rate):
                video_frame_rate = int(video_frame_rate)

            # check if frame rate is an integer
            if not isinstance(video_frame_rate, int):
                self.messages.append(
                    WarningMessage(
                        "Using fractional frame rates is not recommended, as it prevents perfect alignment of audio and video segments"
                    )
                )
            else:
                min_gop_size = self.calculate_min_gop_size(
                    video_frame_rate, audio_sample_rate
                )
                (
                    selected_duration,
                    candidate_durations,
                ) = self.calculate_recommended_durations(
                    video_frame_rate, min_gop_size, target_segment_duration
                )
                if not any(
                    d for d in candidate_durations if d[0] == target_segment_duration
                ):
                    dur_strings = "\n - " + "\n - ".join(
                        [
                            f'"{s}" (= {g} frames = {d:.3f}s)'
                            for g, d, s in candidate_durations
                        ]
                    )
                    self.messages.append(
                        InfoMessage(
                            f"The target segment duration (of {target_segment_duration}s) will cause audio and video segments to not align perfectly, which could cause issues during manifest manipulation.\n"
                            f"For this video frame rate and audio sample rate, it is recommended to create video segments with a GOP multiple of {min_gop_size}.\n"
                            f'I have therefore selected "{selected_duration[2]}" (ie. {selected_duration[1]:.3f}s)\n'
                            f"Other compatible segment durations are: {dur_strings}"
                        )
                    )
                    target_segment_duration = selected_duration[2]

                    common["gop_size"] = str(selected_duration[0])
                    common["keyint_min"] = str(selected_duration[0])

        packaging_options = {}
        packaging_options["--hls.client_manifest_version="] = str(
            packaging.get("version", "3") or "3"
        )
        packaging_options["--hls.minimum_fragment_length="] = str(
            target_segment_duration
        )
        if not packaging.get("audio_only"):
            packaging_options["--hls.no_audio_only"] = ""

        if packaging.get("container") == "ISOBMFF":
            packaging_options["--hls.fmp4"] = ""
        else:
            if not packaging.get("muxed_audio"):
                packaging_options["--hls.no_multiplex"] = ""

        profile = {
            "packaging": packaging_options,
            "servicetype": "offline_transcoding",
            "transcoding": {
                "jobs": jobs,
                "common": common,
            },
        }

        return profile

    def generate_bkt_v2(self, renditions, packaging, name):
        # TODO - gop size explicit
        # TODO - extract audio bitrate
        # TODO - extract audio sample rate
        # TODO - allow multiple (compatible) framerates
        # TODO - FIX - no gop size calculation with non-int framerates (see bkt-v1 version)
        # TODO - audio only

        video_renditions = [r for r in renditions if r["type"] == "video"]
        audio_renditions = [r for r in renditions if r["type"] == "audio"]
        video_ladder = {}
        audio_ladder = {}

        audio_sample_rate = 48000

        # Determine segment duration
        target_segment_duration = packaging.get("segment_duration", 4)
        if float(target_segment_duration) == int(target_segment_duration):
            target_segment_duration = int(target_segment_duration)

        if len(video_renditions):
            # Determine frame rate
            video_frame_rate = renditions[0]["framerate"]
            if isinstance(video_frame_rate, str):
                video_frame_rate = eval(video_frame_rate)

            if video_frame_rate is None:
                video_frame_rate = self.config.get("framerate")
                self.messages.append(
                    WarningMessage(
                        f"Default video framerate of {video_frame_rate} was selected, since it could not be detected in the source"
                    )
                )

            # Check if there is a common frame rate
            is_common_frame_rate = all(
                [r["framerate"] == video_frame_rate for r in video_renditions]
            )
            if not is_common_frame_rate:
                self.messages.append(
                    WarningMessage(
                        "The video frame rates are different for different renditions. The output of this tool may not be correct."
                    )
                )
            video_frame_rate_fraction = _to_fraction(video_frame_rate)
            framerate_repr = {
                "num": video_frame_rate_fraction.numerator,
                "den": video_frame_rate_fraction.denominator,
            }
            # check if frame rate is an integer
            if video_frame_rate_fraction.denominator > 1:
                self.messages.append(
                    WarningMessage(
                        "Using fractional frame rates is not recommended, as it prevents perfect alignment of audio and video segments"
                    )
                )

            # Calculate specs related to frame rate
            if video_frame_rate_fraction.denominator == 1 and packaging.get('muxed_audio') is False:
                min_gop_size = self.calculate_min_gop_size(
                    video_frame_rate, audio_sample_rate
                )
                (
                    selected_duration,
                    candidate_durations,
                ) = self.calculate_recommended_durations(
                    video_frame_rate, min_gop_size, target_segment_duration
                )
                if not any(
                    d for d in candidate_durations if d[0] == target_segment_duration
                ):
                    # find the index of that selected duration in the candidates
                    idx = next(
                        (
                            i
                            for i, t in enumerate(candidate_durations)
                            if t[0] == selected_duration[0]
                        ),
                        None,
                    )
                    dur_strings = "\n - " + "\n - ".join(
                        [
                            f'"{s}" (= {g} frames = {d:.3f}s)'
                            for g, d, s in candidate_durations[idx - 1 : idx + 2]
                        ]
                    )
                    self.messages.append(
                        InfoMessage(
                            f"The target segment duration (of {target_segment_duration}s) will cause audio and video segments to not align perfectly, which could cause issues during manifest manipulation.\n"
                            f"For this video frame rate and audio sample rate, it is recommended to create video segments with a GOP with a size multiple of {min_gop_size} frames.\n"
                            f'I have therefore selected "{selected_duration[2]}" (ie. {selected_duration[1]:.3f}s)\n'
                            f"Other nearby segment durations are: {dur_strings}"
                        )
                    )
                    target_segment_duration = selected_duration[2]
            else:
                selected_duration = None

            # Video rungs
            video_ladder = {
                "common": {
                    "preset": self.config["preset"].upper(),
                    "framerate": framerate_repr,
                }
            }
            if selected_duration:
                video_ladder["common"]["gop_size"] = selected_duration[0]
                video_ladder["common"]["keyint_min"] = selected_duration[0]

            for i, r in enumerate(video_renditions):
                height = _make_even(r["resolution"][1])
                rung = {
                    "_codec_info": f"{r['codec']} {r['profile']} {r['level']}",
                    "codec_string": r["codecstring"],
                    # -2 ensures that the calculated width (preserving aspect ratio) is divisible by 2, a constraint of h264
                    "scale": {"width": -2, "height": height},
                    "bitrate": r["bitrate"],
                }

                # if is_common_frame_rate:
                #     video_ladder["common"]["framerate"] = framerate_repr
                # else:
                #     rung["framerate"] = framerate_repr

                video_ladder[f"video_{i}"] = rung

        # Audio rungs
        audio_ladder = {
            "common": {"sampling_rate": 48000, "loudnorm": {"i": -23, "tp": -1}}
        }

        for i, r in enumerate(audio_renditions):
            audio_ladder[f"audio_{i}"] = {
                "_codec_info": f"{r['codec']} {r['mode']}",
                "codec_string": r["codecstring"],
                "bitrate": r["bitrate"],
            }

        # Packaging options

        # Validate the segment duration size
        muxed_audio = packaging.get("muxed_audio")
        container = packaging.get("container")
        if (container == "MPEG-TS" and not muxed_audio) or container == "ISOBMFF":
            self.messages.append(
                WarningMessage(
                    "Since audio renditions are separate from video, you should ensure that your segment size is compatible between audio rate and video frame rate"
                )
            )

        packaging_options = {}
        packaging_options["hls_client_manifest_version"] = (
            packaging.get("version", 3) or 3
        )
        target_segment_duration_fraction = _to_fraction(target_segment_duration)
        packaging_options["hls_minimum_fragment_length"] = {
            "num": target_segment_duration_fraction.numerator,
            "den": target_segment_duration_fraction.denominator,
        }

        advanced_packaging_options = {}
        packaging_options["advanced"] = advanced_packaging_options
        if not packaging.get("audio_only"):
            advanced_packaging_options["--hls.no_audio_only"] = ""

        if packaging.get("container") == "ISOBMFF":
            advanced_packaging_options["--hls.fmp4"] = ""
        else:
            if not packaging.get("muxed_audio"):
                advanced_packaging_options["--hls.no_multiplex"] = ""

        profile = {
            "version": "02.00.00",
            "name": name,
            "type": "OFFLINE_TRANSCODING",
            "audios": audio_ladder,
            "videos": video_ladder,
            "packaging": packaging_options,
            "_generator": "bpkio-python-sdk/" + version("bpkio-python-sdk"),
        }

        return profile

    def calculate_min_gop_size(self, frame_rate, sample_rate, frames_per_packet=1024):
        # Function to calculate the greatest common divisor (gcd)
        def gcd(n, m):
            while m:
                n, m = m, n % m
            return n

        gop_size = (
            frame_rate
            * frames_per_packet
            / gcd(frame_rate * frames_per_packet, sample_rate)
        )
        return int(gop_size)

    def calculate_recommended_durations(self, frame_rate, gop_size, target_duration):
        candidate_durations = []
        dur = 0
        i = 1
        selected_duration = None
        while dur < 12:
            dur = int(gop_size * i) / frame_rate
            t = (gop_size * i, dur, f"{int(gop_size * i)}/{int(frame_rate)}")
            candidate_durations.append(t)

            if dur <= target_duration:
                selected_duration = t

            i += 1
        return (
            selected_duration,
            candidate_durations,
        )


def _to_fraction(s):
    if isinstance(s, str) and "/" in s:
        num, denom = s.split("/")
        return Fraction(int(float(num)), int(float(denom)))
    else:
        return Fraction(str(s))


def _make_even(n):
    return n if n % 2 == 0 else n - 1
