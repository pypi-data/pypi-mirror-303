import base64
import hashlib
from knifes.strings import ensure_bytes


def md5(data: bytes | str) -> str:
    return hashlib.md5(ensure_bytes(data)).hexdigest()


def b64encode(data: bytes | str) -> str:
    return base64.b64encode(ensure_bytes(data)).decode()


def b64decode(data: bytes | str) -> str:
    return base64.b64decode(ensure_bytes(data)).decode()


def b32encode(data: bytes | str) -> str:
    return base64.b32encode(ensure_bytes(data)).decode()


def b32decode(data: bytes | str) -> str:
    return base64.b32decode(ensure_bytes(data)).decode()
