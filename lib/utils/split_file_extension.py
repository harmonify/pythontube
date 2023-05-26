from __future__ import annotations

def split_file_extension(file_path: str):
    file_path_ext = file_path.split(".")
    file_path, file_ext = ".".join(file_path_ext[:-1]), file_path_ext[-1]
    return file_path, file_ext
