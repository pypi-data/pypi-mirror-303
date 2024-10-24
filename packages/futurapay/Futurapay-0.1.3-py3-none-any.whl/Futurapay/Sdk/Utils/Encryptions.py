import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64
import os
import json


class Encryptions:
    @staticmethod
    def make(merchant_key: str, api_key: str, site_id: str, payload: dict):
        # Generate a key using MD5 hashing
        key= hashlib.md5((merchant_key + api_key + site_id).encode()).hexdigest()
        payload= json.dumps(payload)
        apiKey=base64.b64encode(api_key.encode("utf-8")).decode("utf-8")
        data = Encryptions.encrypt_data(payload, key)
        return {"data": data, "key": apiKey }

    @staticmethod
    def encrypt_data(data, key):
        # Convert key to bytes
        key = key.encode("utf-8")


        # Generate a random 16-byte IV
        iv = os.urandom(16)

        # Pad the data
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data.encode("utf-8")) + padder.finalize()

        # Create AES cipher
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        # Encrypt the data
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

        # Encode the IV and encrypted data as base64
        encrypted_data_base64 = base64.b64encode(iv + encrypted_data).decode("utf-8")
   
        return encrypted_data_base64
