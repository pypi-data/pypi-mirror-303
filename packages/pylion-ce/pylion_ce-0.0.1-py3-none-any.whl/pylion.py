import argparse
import base64
import hashlib
from clear import clear
from cryptography.hazmat.primitives.asymmetric import ed25519

def pylion():
    hits = []

    clear()

    parser = argparse.ArgumentParser()
    parser.add_argument("-filename", type = str, help = "What do you want to name the output file?")
    parser.add_argument("-links", type = int, help = "How many links do you want to generate?", default = 1)
    args = parser.parse_args()
    
    for link in range(args.links):
        public = ed25519.Ed25519PrivateKey.generate().sign(b"")[:32]
        checksum = hashlib.sha3_256(b".onion checksum" + public + b"\x03").digest()[:2]
        result = "http://" + base64.b32encode(public + checksum + b"\x03").decode().lower() + ".onion"
        hits.append(result)

    hits = list(dict.fromkeys(hits[:]))
    hits.sort()

    if args.filename:
        with open(args.filename, "a") as file:
            for hit in hits:
                file.write(f"{hit}\n")
                print(hit)

    else:
        for hit in hits:
            print(hit)

if __name__ == "__main__":
    pylion()
