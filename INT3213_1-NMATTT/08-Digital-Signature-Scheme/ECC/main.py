"""
Digital Signature Scheme using SHA256 Hash Algorithm and
Elliptic Curve to Sign.
"""

from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import ECC  # , RSA
from Cryptodome.Signature import DSS

key = ECC.import_key(open('./example_priv.pem').read())
signer = DSS.new(key, 'fips-186-3')


def genKey(fn, key):
    """
    Generate ECC key for Digital Signature.
    Privated key is stored in `"example_priv.pem"`.
    Corresponding public key is stored in `"example_public.pem"`.
    """
    # ECC for Digital Signature
    key = ECC.generate(curve='NIST P-256')
    f = open('example_priv.pem', 'wt')
    f.write(key.export_key(format='PEM'))
    f.close()
    f = open('example_public.pem', 'wt')
    f.write(key.public_key().export_key(format='PEM'))
    f.close()


def sendMessage(message):
    hashMessage = SHA256.new(message)  # Or replace with RSA if you want
    signature = signer.sign(hashMessage)
    return (message, signature)


def verifyMessage(message, signature, otherPK):
    hashMessage = SHA256.new(message)
    verifier = DSS.new(otherPK, 'fips-186-3')
    try:
        verifier.verify(hashMessage, signature)
        print("The message is authentic ehehehe.")
    except ValueError:
        print("The message is not authentic ahuhuhu.")


if __name__ == "__main__":
    message = 'Mai yeu thay Do va Elliptic Curve!!!!'

    msg = sendMessage(message.encode())
    print("Message : ", msg[0].decode(), '\n', "Signature : ", msg[1].hex(), sep='')
