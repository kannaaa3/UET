<!-- # Secret Key Cryptography -->
<!---->
<!-- # Public Key Cryptosystem -->
<!---->
<!-- # Hybrid -->
<!---->
<!-- Dùng khóa công khai trao đổi khóa rồi dùng khóa bí mật trao đổi thông tin. Do khóa bí mật có performance tốt hơn. -->
<!---->
<!-- ## Block Cipher -->
<!---->
<!-- ## Stream Cipher -->
<!---->
<!-- ## Mesage Integrity  -->
<!-- ## Message  -->
<!-- ## Availability -->


A **cryptosystem.** is a five-tuple (P, C, K, E, D) where:

- P: a finite set of all possible plaintexts
- C: a finite set of all possible ciphertexts
- K: the *keyspace*, a finite set of possible keys
- E: Encryption rule
- D: Decryption rule

## Caesar Cipher, Substitution
## Affine
- With 2 numbers `a` (coprime with 26) and `b`, we obtain another method for encryption: `e(x) = ax + b`

There exists a char x which is inverse modulo of a mod 26. `d(x) = a^(-1) (y-b) mod 26`

Key set consists of all pair (a, b).

## Vigenere
Applied on every group of m characters. A key K consists of `m` keys.
