"""
AES/CBC/PKCS7Padding(PKCS5Padding) encrypt and decrypt
"""

import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


iv = bytes(16)  # iv is empty 16 bytes data


def encrypt(data: str | bytes, key: str):
    """encrypt data with AES/CBC/PKCS7Padding"""

    if isinstance(data, str):
        data = data.encode()

    encryptor = Cipher(algorithms.AES(key.encode()), modes.CBC(iv), backend=default_backend()).encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()  # type: ignore
    padded_data = padder.update(data) + padder.finalize()
    cipher_text = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b32encode(cipher_text).decode()


def decrypt(data: str | bytes, key: str):
    """decrypt data with AES/CBC/PKCS7Padding"""

    if isinstance(data, str):
        data = data.encode()

    decryptor = Cipher(algorithms.AES(key.encode()), modes.CBC(iv), backend=default_backend()).decryptor()
    decrypted_data = decryptor.update(base64.b32decode(data)) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()  # type: ignore # PKCS7解填充
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    return unpadded_data.decode()
