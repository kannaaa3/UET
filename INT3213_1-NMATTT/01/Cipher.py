from secretpy import Affine, Vigenere
import numpy as np
from numpy.linalg import inv
from math import gcd

import string

class Cipher:
    """
    Not working for both lowercase and uppercase yet.
    """
    def __init__(self) -> None:
        pass

    def id(self, c):
        return ord(c) - ord('a')

    def encrypt(self):
        pass

    def decrypt(self):
        pass

class ShiftCipher(Cipher):
    k = 0
    def __init__(self, k = 0) -> None:
        """
        Create a cipher box that shift every character by `k`.
        By default, k = 0.
        """
        self.k = k
        return

    def shift(self, c, k = 0):
        return chr((ord(c) - ord('a') + k) % 26 + ord('a'))

    def encrypt(self, plain: str, k = None) -> str:
        if (k == None):
            k = self.k

        cipher = [self.shift(c, k) for c in plain]
        cipher = ''.join(cipher)

        return cipher

    def decrypt(self, cipher: str, k = None) -> str:
        if (k == None):
            k = self.k

        plain = [self.shift(c, -k) for c in cipher]
        plain = ''.join(plain)

        return plain 

class Substitution(Cipher):
    """
    Given a key of the permutation.
    """
    def __init__(self) -> None:
        self.key = self.strToKey(key_str)
        self.key_inv = self.invKey(self.key)

    def strToKey(self, s):
        assert len(s) == 26
        d = dict()
        for i in range(26):
            d[chr(ord('a') + i)] = s[i]
        return d
    
    def strToInvKey(self, s):
        return self.invKey(self.strToKey(s))

    def invKey(self, d):
        d_inv = {v : k for k, v in d.items()}
        return d_inv

    def encrypt(self, plain, key = None):
        """
        Encrypt a string with or without a key string provided.
        By default, the key during initialization is used.
        """
        key = self.key if key == None else self.strToKey(key)

        cipher = [key[c] for c in plain]
        cipher = ''.join(cipher)

        return cipher
    
    def decrypt(self, cipher, key = None):
        """
        Decrypt a string with or without a key string provided.
        By default, the key during initialization is used.
        """
        key_iv = self.key_inv if key == None else self.strToInvKey(key)

        plain = [key_iv[c] for c in cipher]
        plain = ''.join(plain)

        return plain

class Hill(Cipher):
    def __intit__(self, _K: np.ndarray):
        self.K = _K

    def encrypt(self, plaintex):
        plaintex = np.array(plaintex)
        cipher = np.matmul(plaintex, K)
        return

    def decrypt(self, ciphertext):
        ciphertext = np.array(ciphertext)
        plain = np.matmul(ciphertext, inv(K))
        return

    def update_key(self):
        return

if __name__ == "__main__":
    cs = ShiftCipher()
    print(cs.encrypt("wewillmeet", 7))
