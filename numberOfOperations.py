def numberOfOperations(a, b):

    if a < b:
        a, b = b, a
    if b % a != 0:
        return 0
    return 1 + numberOfOperations(a / b, b)
