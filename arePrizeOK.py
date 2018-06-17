def arePrizesOK(first, second, third):
    if first < second:
        return False
    if  second < third :
        return False
    return True