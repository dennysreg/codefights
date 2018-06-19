n=200
criba = [1]*n
criba[0] = criba[1] = 1

for i in range(2,n):
    if criba[i]:
        for j in range(2*i,n,i):
            criba[i]=0

def leastCommonPrimeDivisor(a, b):
    for i in range(2,len(criba)):
        if a%i==0 and b%i==0:
            return i
    return -1