
def leastFactorial(n):
    f=1
    r=[]
    for i in range(1,100):
        f*=i
        r.append(f)
    start = n
    i=0
    while i < len(r):
        if r[i]>=n:
            return r[i-1]        
        i+=1