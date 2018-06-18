def primeFactors2(n):
    factors = []
    divisor = 2

    while n > 0:
        if n % divisor == 0:
            factors.append(divisor)
        while n % divisor == 0:
            n /= divisor
        divisor += 1

    return factors