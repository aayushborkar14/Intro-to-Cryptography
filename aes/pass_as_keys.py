import hashlib
from Crypto.Cipher import AES
import requests


def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


with open("words") as f:
    words = [w.strip() for w in f.readlines()]
for keyword in words:
    KEY = hashlib.md5(keyword.encode()).digest()
    ciphertext = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"
    FLAG = bytes.fromhex(decrypt(ciphertext, KEY.hex())["plaintext"])
    if b"crypto" in FLAG:
        print(FLAG)
        break
