import json
import base64
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def main(data):
    private_key = None
    with open('private_key.pem', 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None
        )
    if not private_key:
        raise Exception('Private key is not present')

    encryption_padding = padding.PKCS1v15()
    key1 = private_key.decrypt(base64.b64decode(data.get('key1')), encryption_padding)
    key2 = private_key.decrypt(base64.b64decode(data.get('key2')), encryption_padding)
    iv = private_key.decrypt(base64.b64decode(data.get('iv')), encryption_padding)

    key = key1.decode('utf-8') + key2.decode('utf-8')
    hashed_key = hashlib.sha256(key.encode('utf-8'))
    key_bytes = hashed_key.digest()

    cipher = Cipher(algorithms.AES(key.encode('utf-8')), modes.CBC(iv))
    decryptor = cipher.decryptor()

    doc = data.get('doc')
    decoded_doc = base64.b64decode(doc.encode('utf-8'))
    result = decryptor.update(decoded_doc) + decryptor.finalize()

    with open('decrypted.pdf', 'wb') as of:
        of.write(result)


if __name__ == '__main__':
    with open('./encrypted', 'r') as f:
        data = json.load(f)
        main(data)
