from __future__ import annotations

from datetime import datetime

from config import Config
from pytube import Stream

from ..utils import split_file_extension


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
