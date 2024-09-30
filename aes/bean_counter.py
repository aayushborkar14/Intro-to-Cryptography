import requests
from Crypto.Util.strxor import strxor

enc = bytes.fromhex(
    requests.get("https://aes.cryptohack.org/bean_counter/encrypt/").json()["encrypted"]
)
png_header = b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52"
keystream = strxor(enc[:16], png_header)

with open("bean_flag.png", "wb") as f:
    for i in range(0, len(enc), 16):
        block = enc[i : i + 16]
        f.write(strxor(block, keystream[: len(block)]))
