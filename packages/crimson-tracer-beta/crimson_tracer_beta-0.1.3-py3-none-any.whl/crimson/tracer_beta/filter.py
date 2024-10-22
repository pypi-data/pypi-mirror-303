from types import FrameType


def frame_filter(frame: FrameType) -> bool:
    exclude = ["python3", "site-packages"]
    for exclude_key in exclude:
        if frame.f_code.co_filename.find(exclude_key) != -1:
            return False
    return True
