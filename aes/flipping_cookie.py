from Crypto.Util.strxor import strxor

cookie = "ab0a1aad7ea445d404156a640cad5ea49f36a6228003d806e51a8d7e120ee0682dac8e361e933ef7676b58b1136cbaab"
iv = bytes.fromhex(cookie[:32])
iv2 = strxor(strxor(b"admin=False;", iv[:12]), b"admin=True;;").hex() + iv[12:].hex()
cookie2 = cookie[32:]

print(cookie2)
print(iv2)
