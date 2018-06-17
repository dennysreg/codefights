def checkFactorial(n):
    divisor = 2
    while n != 1:
        if n % divisor == 0:
            n /= divisor
        else:
            return  False 
        divisor += 1
    return True
