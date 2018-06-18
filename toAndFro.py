def toAndFro(a, b, t):

    length = abs(b - a)
    t %=  length*2
    if t <= length:
        return a + (b - a) / abs(b - a) * t
    else:
        t -= length
        return b + (a - b) / abs(a - b) * t
