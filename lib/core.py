from __future__ import annotations

import os
from datetime import datetime
from typing import List

from moviepy.editor import AudioFileClip
from pytube import Stream, StreamQuery

from .config import Config
from .utils import split_file_extension


def get_video_stream(streams: StreamQuery, is_data_saver: bool) -> Stream:
    # Using Filters on the myVideoStream Object
    if is_data_saver:
        options: List[StreamQuery] = [
            streams.filter(file_extension="mp4",
                           resolution="720p", fps=60, abr="128kbps"),
            streams.filter(file_extension="mp4",
                           resolution="720p", abr="128kbps"),
            streams.filter(file_extension="mp4", resolution="720p"),
            streams.filter(file_extension="mp4", abr="128kbps"),
            streams.filter(file_extension="mp4"),
        ]
        for option in options:
            mp4_stream = option.first()
            if mp4_stream:
                break
    else:
        mp4_stream = streams.get_highest_resolution()
    return mp4_stream


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


def download_stream(stream: Stream, config: Config, timeout: int):
    # create file name
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    file_path, file_ext = split_file_extension(stream.default_filename)
    file_path = f"{file_path}_{timestamp}.{file_ext}"
    # download
    print('@@@ Download starting!')
    return stream.download(config.data["output_dir_path"],
                           filename=file_path,
                           timeout=timeout)


def convert_mp4_to_mp3(file_path: str, output_file_path: str = None):
    AUDIO_FILE_EXT = "mp3"

    if output_file_path:
        audio_file_path = output_file_path
    else:
        video_file_path, video_file_ext = split_file_extension(
            file_path)
        audio_file_path = f"{video_file_path}.{AUDIO_FILE_EXT}"

    audio_file_clip = AudioFileClip(file_path)

    print("@@@ Converting mp4 to mp3...\n")
    audio_file_clip.write_audiofile(audio_file_path)
    audio_file_clip.close()

    print("@@@ Removing original mp4 file...")
    os.remove(file_path)
    print("Done")
