def hangman(word, letters):
    f=0
    t=0
    for c in letters:
        if f >=6:
            return False
        x = word.count(c)
        if x ==0:
            f+=1
        else:
            t+=x
    return t==len(word)
        
            
