"""
Simple implementation of ElGamal Digital Signature Scheme.
Based on DoPL's Lecture.
"""

from Cryptodome.PublicKey.ElGamal import *
from Cryptodome.Util.number import getPrime
# from Cryptodome.Hash import SHA256

from Cryptodome.Util.number import inverse

from random import randint

p = getPrime(256)
alpha = 2  # Primitive root alpha

"""
Generate private key a.
"""
a = randint(0, p-1)  # alpha is priv_key


class Key:
    private_key = None
    public_key = (None, None, None)

    def __init__(self,  p: int, alpha: int, a: int) -> None:
        self.private_key = a
        beta = pow(alpha, a, p)
        self.public_key = (p, alpha, beta)


def stringToInt(message, mod):
    h = 0
    for c in message:
        h = ((h * 26) + ord(c) - ord('a')) % mod
    return h


def sendMessage(message, key: Key):
    # hashMessage = SHA256.new(message)  # Or replace with anything if you want
    # hashMessage = int(sha256(message).hexdigest(), 16)
    a = key.private_key
    p, alpha, beta = key.public_key

    hashMessage = stringToInt(message, p)
    print(hashMessage)

    k = randint(0, p-1)
    _k = inverse(k, p-1)

    gamma = pow(alpha, k, p)
    sigma = (hashMessage - a * gamma) * _k % (p-1)
    signature = (gamma, sigma)

    print(signature)
    return signature


def verifyMessage(message, signature, otherPK):
    p, alpha, beta = otherPK
    gamma, sigma = signature
    hashMessage = stringToInt(message, p)
    a = pow(beta, gamma, p) * pow(gamma, sigma, p) % p
    b = pow(alpha, hashMessage, p)

    if (a == b):
        print("The message is authentic ehehehe.")
        return True

    print("The message is not authentic ahuhuhu.")
    return False


if __name__ == "__main__":
    message = 'Mai yeu thay Do'
    key = Key(p=127, alpha=467, a=2)
    print(key.public_key)
    sendMessage(message, key)
    verifyMessage(message, (58, 29), key.public_key)
