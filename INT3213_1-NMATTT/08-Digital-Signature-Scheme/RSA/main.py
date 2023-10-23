from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256

from Cryptodome import Random

# NOTE: A probabilistic digital signature scheme based on RSA.
from Cryptodome.Signature import pss

key = RSA.import_key(open('priv_key.pem').read())
signer = pss.new(key)


def genKey():
    """
    Generate new RSA key.
    Privated key is stored in `"priv_key.pem"`.
    Corresponding public key is stored in `"public_key.pem"`.
    """
    key = RSA.generate(2048)
    f = open('priv_key.pem', 'wb')
    f.write(key.export_key(format='PEM'))
    f.close()
    f = open('public_key.pem', 'wb')
    f.write(key.public_key().export_key(format='PEM'))
    f.close()


def sendMessage(message):
    hashMessage = SHA256.new(message)  # Or replace with RSA if you want
    signature = signer.sign(hashMessage)
    return (message, signature)


def verifyMessage(message, signature, otherPK):
    hashMessage = SHA256.new(message)
    verifier = pss.new(otherPK)
    try:
        verifier.verify(hashMessage, signature)
        print("The message is authentic ehehehe.")
    except (ValueError, TypeError):
        print("The message is not authentic ahuhuhu.")


if __name__ == "__main__":
    message = 'Mai yeu thay Do va RSA!!!!'

    msg = sendMessage(message.encode())
    print("Message : ", msg[0].decode(), '\n', "Signature : ", msg[1].hex(), sep='')
