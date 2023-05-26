from __future__ import annotations

def format_second(seconds: int) -> str:
    # Calculate hours, minutes, and seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Format into HH:mm:ss
    formatted_length = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    return formatted_length
