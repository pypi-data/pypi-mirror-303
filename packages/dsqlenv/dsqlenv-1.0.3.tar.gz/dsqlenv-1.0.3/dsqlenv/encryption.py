# encryption.py
from Crypto.Cipher import AES
import base64

class AESEncryptor:
    def __init__(self, key):
        self.key = self._pad_key(key)

    def _pad_key(self, key):
        return key.ljust(32)[:32]

    def _pad(self, data):
        padding_length = 16 - len(data) % 16
        return data + (chr(padding_length) * padding_length)

    def _unpad(self, data):
        padding_length = ord(data[-1])
        return data[:-padding_length]

    def encrypt(self, data):
        cipher = AES.new(self.key.encode('utf-8'), AES.MODE_ECB)
        padded_data = self._pad(data)
        encrypted = cipher.encrypt(padded_data.encode('utf-8'))
        return base64.b64encode(encrypted).decode('utf-8')

    def decrypt(self, encrypted_data):
        cipher = AES.new(self.key.encode('utf-8'), AES.MODE_ECB)
        decrypted_data = cipher.decrypt(base64.b64decode(encrypted_data))
        return self._unpad(decrypted_data.decode('utf-8'))
