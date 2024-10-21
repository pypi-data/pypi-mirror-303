def blur_phone(phone):
    """blur phone number"""
    if not phone or len(phone) < 11:
        return phone
    return phone[:3] + "****" + phone[7:]


def abbreviate(text, max_len=2, marker="..."):
    """slice text to max_len and add marker if text is too long"""
    return text[0:max_len] + marker if len(text) > max_len else text


def ensure_str(v: bytes | str):
    """convert bytes to str"""
    return v.decode() if isinstance(v, bytes) else v


def ensure_bytes(v: bytes | str):
    """convert str to bytes"""
    return v.encode() if isinstance(v, str) else v


def safe_int(v: str | int, default: int | None = None) -> int | None:
    try:
        return int(v)
    except (ValueError, TypeError, OverflowError):
        return default
