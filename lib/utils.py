from __future__ import annotations

def format_second(seconds: int) -> str:
    # Calculate hours, minutes, and seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Format into HH:mm:ss
    formatted_length = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    return formatted_length

def split_file_extension(file_path: str):
    file_path_ext = file_path.split(".")
    file_path, file_ext = ".".join(file_path_ext[:-1]), file_path_ext[-1]
    return file_path, file_ext
