def numberOfTriangles(sticks):
    res = 0
    for i in range(len(sticks)):
        k = i + 2
        for j in range(i + 1, len(sticks)):
            while k < len(sticks)  and sticks[i]+sticks[j] > sticks[k]  :
                k += 1
            res += k - j - 1
    return res
