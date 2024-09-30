from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests


def encrypt(plaintext):
    return requests.get(
        "https://aes.cryptohack.org/ecb_oracle/encrypt/" + plaintext.encode().hex()
    ).json()["ciphertext"]


flag = "crypto{"
chars = "abcdefghijklmnopqrstuvwxyz0123456789_}ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    if len(flag) >= 15:
        break
    payload = "1" * (16 - len(flag) - 1)
    expected = encrypt(payload)
    for c in chars:
        payload_w_flag = payload + flag + c
        ct = encrypt(payload_w_flag)
        if expected[:32] == ct[:32]:
            flag += c
            print(flag)
            break

flag = "crypto{p3n6u1n5"

while True:
    if len(flag) >= 31 or flag[-1] == "}":
        break
    payload = "1" * (32 - len(flag) - 1)
    expected = encrypt(payload)
    for c in chars:
        payload_w_flag = payload + flag + c
        ct = encrypt(payload_w_flag)
        if expected[32:64] == ct[32:64]:
            flag += c
            print(flag)
            break
