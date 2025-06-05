from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import hashlib
import base64

note = b"Your files are encrypted. Pay tribute or perish."
salt = get_random_bytes(16)
password = b"SuperSecretMasterPass"
key = PBKDF2(password, salt, dkLen=32, count=100_000)

cipher = AES.new(key, AES.MODE_GCM)
ciphertext, tag = cipher.encrypt_and_digest(note)

with open("ransom_encrypted.bin", "wb") as f:
    f.write(salt + cipher.nonce + tag + ciphertext)

print("[+] AES Encrypted note dropped.")
