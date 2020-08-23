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
    h = Crypto.Hash.SHA256.new(message)
    try:
        Crypto.Signature.DSS.new(key, "fips-186-3").verify(h, signature)
        print("The signature is valid.")
        return True
    except (ValueError, TypeError):
        print("The signature is not valid.")
        return False


def generate_keys():
    """Generate keys."""
    private_key = Crypto.PublicKey.ECC.generate(curve="P-256")
    f = open("keys/ECC_Private_key.pem", "wt")
    f.write(private_key.export_key(format="PEM"))
    f.close()
    pub_key = private_key.public_key()
    g = open("keys/ECC_Public_key.pem", "wt")
    g.write(pub_key.export_key(format="PEM"))
    g.close()
