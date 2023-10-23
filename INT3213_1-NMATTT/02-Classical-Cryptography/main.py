from sympy.crypto.crypto import *


"""
Helper function.
"""


def strToKeyMap(s):
    assert len(s) == 26
    d = dict()
    for i in range(26):
        d[chr(ord('a') + i)] = s[i]
    return d


"""
Classic Cryptosystems with SymPy library.
"""


def caesar_cipher(plaintext, key=7):
    cipher = encipher_shift(plaintext, key)
    plaintext = decipher_shift(cipher, key)

    print(f"Caesar Cipher with key = {key}:", cipher)

    return (plaintext, cipher)


def substitution_cipher(plaintext, key="WUTSDPLCKXZFEIAHQYBRVJGNMO"):
    mapping = strToKeyMap(key)
    cipher = encipher_substitution(plaintext, mapping)

    print(f"Substitution Cipher with key = {key}:", cipher)

    return (plaintext, cipher)


def affine_cipher(plaintext, key=(7, 1)):
    cipher = encipher_affine(plaintext, key)
    plaintext = decipher_affine(cipher, key)

    print(f"Affine Cipher with key = {key}:", cipher)

    return (plaintext, cipher)


def vigenere_cipher(plaintext, key="encruypt"):
    cipher = encipher_vigenere(plaintext, key)
    plaintext = decipher_vigenere(plaintext, key)

    print(f"Vigenere Cipher with key = \'{key}\':", cipher)

    return (plaintext, cipher)


def hill_cipher(plaintext, key=Matrix([[11, 3], [8, 7]])):
    cipher = encipher_hill(plaintext, key)
    plaintext = decipher_hill(cipher, key)

    print(f"Hill Cipher with key = {key}:", cipher)

    return (plaintext, cipher)


if __name__ == "__main__":
    """
    Demo
    """

    plaintext = "HAYSONGNHUNHUNGDOAHOA"
    print("Plaintext:", plaintext)
    print("Encrypting using default key...\n")

    caesar_cipher(plaintext)
    substitution_cipher(plaintext)
    affine_cipher(plaintext)
    vigenere_cipher(plaintext)
    hill_cipher(plaintext)
