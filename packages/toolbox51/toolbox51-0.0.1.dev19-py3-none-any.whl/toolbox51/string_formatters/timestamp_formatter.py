__all__ = ["timestamp_formatter"]

import functools

def timestamp_message(timestamp: float, message: str):
    return f"{timestamp} | {message}"
def timestamp_formatter(timestamp: float):
    return functools.partial(timestamp_message, timestamp)