#!/usr/bin/env python
"""A simple program for making a blockchain."""
import Crypto.Hash.SHA256
import Crypto.PublicKey.ECC
import Crypto.Signature.DSS


def sign(message):
    """Sign."""
    digest = Crypto.Hash.SHA256.new(message)
    private_key = Crypto.PublicKey.ECC.import_key(open("keys/ECC_Private_key.pem").read())
    signer = Crypto.Signature.DSS.new(private_key, "fips-186-3")
    sig = signer.sign(digest)
    print("Signed message: " + str(message) + "with signature: " + str(sig))
    return sig


def verify(message, signature):
    """Verify."""
    key = Crypto.PublicKey.ECC.import_key(open("keys/ECC_Public_key.pem").read())
    sha_hash = Crypto.Hash.SHA256.new(message)
    try:
        Crypto.Signature.DSS.new(key, "fips-186-3").verify(sha_hash, signature)
        print("The signature is valid.")
        return True
    except (ValueError, TypeError):
        print("The signature is not valid.")
        return False


def generate_keys():
    """Generate keys."""
    private_key = Crypto.PublicKey.ECC.generate(curve="P-256")
    file = open("keys/ECC_Private_key.pem", "wt")
    file.write(private_key.export_key(format="PEM"))
    file.close()
    pub_key = private_key.public_key()
    file = open("keys/ECC_Public_key.pem", "wt")
    file.write(pub_key.export_key(format="PEM"))
    file.close()
