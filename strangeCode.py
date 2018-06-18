def strangeCode(s, e):
    r=[]
    
    while s < e-1:
        s+=1
        e-=1
        if len(r)==0 or r[-1]=='b':
            r.append('a')
        else:
            r.append('b')
    return "".join(r)