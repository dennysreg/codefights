def createAnagram(s, t):
    change = 0
    for i in range(0,len(s)):
        change += abs(s.count(s[i])-t.count(s[i]))//s.count(s[i])
        
    return change
