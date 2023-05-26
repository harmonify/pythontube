from __future__ import annotations

import os

from moviepy.editor import AudioFileClip

from ..utils import split_file_extension


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
