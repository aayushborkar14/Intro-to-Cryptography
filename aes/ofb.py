import requests
from Crypto.Util.strxor import strxor

ct = requests.get("https://aes.cryptohack.org/symmetry/encrypt_flag/").json()[
    "ciphertext"
]
iv = bytes.fromhex(ct[:32])
flag_len = len(ct) // 2 - 16
payload = (b"\x00" * flag_len).hex()
block_output = bytes.fromhex(
    requests.get(
        f"https://aes.cryptohack.org/symmetry/encrypt/{payload}/{iv.hex()}/"
    ).json()["ciphertext"]
)
print(strxor(block_output, bytes.fromhex(ct[32:])).decode())
