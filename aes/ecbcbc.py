import requests


def decrypt(ct):
    return bytes.fromhex(
        requests.get(f"https://aes.cryptohack.org/ecbcbcwtf/decrypt/{ct}/").json()[
            "plaintext"
        ]
    )


def decode_up_to_valid_bytes(byte_string, encoding="utf-8"):
    for i in range(len(byte_string), 0, -1):
        try:
            return byte_string[:i].decode(encoding)
        except UnicodeDecodeError:
            continue
    return ""


ct = "8b21005c70ef40f4accfc863dd9533e3e4273b8a163c5855006d2babe3e0cc5ca5d2944347e29318eaf500024a3d469f"
iv = bytes.fromhex(ct[:32])
block1 = decrypt(ct[32:64])
flag1 = bytes(a ^ b for a, b in zip(iv, block1))
# print(flag1.decode())

block2 = decrypt(ct[64:96])
flag2 = bytes(a ^ b for a, b in zip(bytes.fromhex(ct[32:64]), block2))
print(flag1.decode() + decode_up_to_valid_bytes(flag2))
