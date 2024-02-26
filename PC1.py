def egypt(n, d):
    """
    >>> egypt(3, 4)
    '1/2 + 1/4'
    >>> egypt(11, 12)
    '1/2 + 1/3 + 1/12'
    """
    result = ""
    while (n > 0):
        p = 2
        while ((n * p) < d):  
            p += 1

        if result:
            result += " + "
        
        result += f"1/{p}"
        n =(n * p) - d
        d = n * p
        
        common_divisor = gcd(n, d)
        n = int(n / common_divisor)
        d = int(d / common_divisor)

    return result


def gcd(a, b):
    """
    Compute the greatest common divisor of a and b.

    >>> gcd(3, 4)
    1
    >>> gcd(60, 48)
    12
    """
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)


print(egypt(3, 4))
print(egypt(11, 12))
