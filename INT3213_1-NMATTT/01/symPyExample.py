from sympy.crypto.crypto import *


def strToKeyMap(s):
    """
    Return a dictionary for Substitution Cipher from a string.
    """
    assert len(s) == 26
    d = dict()
    for i in range(26):
        d[chr(ord('a') + i)] = s[i]
    return d

if __name__ == "__main__":
    print("# Caesar Cipher:")
    plaintext = "\"HENGAPNHAUVAOCHIEUTHUBAY\""
    k = 7
    cipher = encipher_shift(plaintext, k)
    print("cipher  =", cipher)
    print("decrypt =", decipher_shift(cipher, k))

    print("# Substitution Cipher:")
    k = strToKeyMap("WUTSDPLCKXZFEIAHQYBRVJGNMO")
    cipher = encipher_substitution(plaintext, k)
    print("cipher  =", cipher)

    print("# Affine Cipher:")
    plaintext =  "THISCRYPTOSYSTEMISNOTSECURE"
    k = (7, 1)
    cipher = encipher_affine(plaintext, k)
    print("cipher  =", cipher)
    print("decrypt =", decipher_affine(cipher, k))

    print("# Vigenere Cipher:")
    plaintext =  "THISCRYPTOSYSTEMISNOTSECURE"
    k = "encrypt"
    cipher = encipher_vigenere(plaintext, k)
    print("cipher  =", cipher)
    print("decrypt =", decipher_vigenere(cipher, k))

    print("# Hill Cipher:")
    plaintext = "HENGAPNHAUVAOCHIEUTHUBAY"
    k = Matrix([[11, 3], [8, 7]]) # Columns
    cipher = encipher_hill(plaintext, k)
    print("cipher  =", cipher)
    print("decrypt =", decipher_hill(cipher, k))
