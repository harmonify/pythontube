from __future__ import annotations

from typing import List

from pytube import Stream, StreamQuery


def get_video_stream(streams: StreamQuery, is_data_saver: bool) -> Stream:
    # Using Filters on the myVideoStream Object
    if is_data_saver:
        options: List[Stream] = [
            streams.filter(file_extension="mp4",
                           resolution="720p", fps=60, abr="128kbps"),
            streams.filter(file_extension="mp4",
                           resolution="720p", abr="128kbps"),
            streams.filter(file_extension="mp4", resolution="720p"),
            streams.filter(file_extension="mp4", abr="128kbps"),
            streams.filter(file_extension="mp4"),
        ]
        for option in options:
            mp4_stream = option
            if mp4_stream:
                break
    else:
        mp4_stream = streams.get_highest_resolution()
    return mp4_stream
