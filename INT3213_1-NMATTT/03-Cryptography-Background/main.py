
"""
Implementation of the algorithms.
"""


def euclid_gcd(a: int, b: int) -> int:
    """
    Find gcd of 2 numbers using Euclide Algorithm.
    Input: 2 integer `a` and `b`
    Ouput: `gcd(a,b)`
    """
    if a == 0 or b == 0:
        return a + b
    return euclid_gcd(b, a % b)


def extended_euclid_invMod(a: int, b: int, g: int):
    if b == 0:
        return (g//a, 0)
    x1, y1 = extended_euclid_invMod(b, a % b, g)
    q = a // b
    return (y1, x1 - y1 * q)


def chinese_remainder_theorem():
    return


"""
Using library.
"""
