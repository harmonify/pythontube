from __future__ import annotations

from pytube import Stream, StreamQuery


def get_audio_only_stream(streams: StreamQuery, is_data_saver: bool) -> Stream:
    MINIMUM_ABR="128kbps"

    if is_data_saver:
        # Filtering only audio streams
        audio_only_streams = streams.filter(
            only_audio=True, abr=MINIMUM_ABR) or streams.filter(only_audio=True)
        audio_stream = audio_only_streams.first()
    else:
        audio_stream = streams.get_audio_only()
    return audio_stream
