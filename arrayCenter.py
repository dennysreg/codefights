def arrayCenter(a):

    n = len(a)
    suma =  a[0]
    mina = a[0]
    for i in range(1, n):
        suma += a[i]
        mina = min(mina, a[i])

    b = []
    for i in range(n):
        if abs(n * a[i] - suma) < n * mina:
            b.append(a[i])

    return b