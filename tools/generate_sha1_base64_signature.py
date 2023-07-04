import hashlib
import base64
import sys

# Get the filename from the first command-line argument
filename = sys.argv[1]

with open(filename, 'rb') as f:
    h = hashlib.sha1()
    h.update(f.read())
    hash_sha1 = h.digest()

encoded_base64 = base64.b64encode(hash_sha1)

print(encoded_base64.decode())
