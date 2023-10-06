def gcd(a , b):
    return a if b == 0 else gcd(b, a % b)


def extended_euclid(a, b, g):
    if b == 0:
        return (g//a, 0)
    x1, y1 = extended_euclid(b, a % b, g)
    q = a // b
    return (y1, x1 - y1 * q)

extended_euclid(722, 2357, 1)

    
    

    

