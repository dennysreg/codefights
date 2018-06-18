def fractionDivision(a, b):

    def gcdEuclid(a, b):
        if a == 0:
            return b
        return gcdEuclid(a % b, b)

    c = [a[0] * b[1], a[1] * b[0]]
    gcd = gcdEuclid(c[0], c[1])

    c[0] /= gcd
    c[1] /= gcd

    return c
