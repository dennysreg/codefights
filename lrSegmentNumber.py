def lrSegmentNumber(l, r):
  s=[]
  for i in range(l,r+1):
    s.append(str(i))    
  return int("".join(s))