def squareDigitsSequence(a0):
    r = set()
    r.add(a0)
    i=1
    while True:
        s=0
        while a0:
            s += (a0%10)**2
            a0//=10
        
        a0 = s
        
        i+=1
    
        