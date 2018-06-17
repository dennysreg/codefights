def smallestMultiple(left, right):
  start = right+1
  while True:
    c=0
    for i in range(left,right+1):
      if start%i!=0:
        break
      else:
        c+=1
    if c==right-left+1:
      return start
    start+=1
  
  
    