

from random import Random

import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def encrypt(raw, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    # return (iv + cipher.encrypt(raw))
    return base64.b64encode(iv + cipher.encrypt(raw))
def decrypt1(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))
ext="jpg"
id="2"
key="hellloooooooooo"
# with open("1." + ext, "rb") as imageFile:
#     stri = base64.b64encode(imageFile.read()).decode('utf-8')
#     enc1 = encrypt(stri,key ).decode('utf-8')
#
#     fh = open("" + str(id) + "." + ext, "wb")
#     fh.write(base64.b64decode(enc1))
#     fh.close()
#
#
# with open(str(id) + "." + ext, "rb") as imageFile:
#             stri = base64.b64encode(imageFile.read()).decode('utf-8')
#
#
#             dec2 = decrypt1(stri, key).decode('utf-8')
#
#
#             fh1 = open("3."+ext, "wb")
#             fh1.write(base64.b64decode(dec2))
#             fh1.close()