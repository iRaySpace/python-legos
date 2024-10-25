import base64
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def main():
    key = ""
    hashed_key = hashlib.sha256(key.encode('utf-8'))
    key_bytes = hashed_key.digest()

    iv = ""
    decoded_iv = base64.b64decode(iv.encode('utf-8'))

    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(decoded_iv))
    decryptor = cipher.decryptor()

    doc = ""
    decoded_doc = base64.b64decode(doc.encode('utf-8'))
    result = decryptor.update(decoded_doc) + decryptor.finalize()
    print(result)


if __name__ == '__main__':
    main()
