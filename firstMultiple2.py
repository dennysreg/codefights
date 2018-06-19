def firstMultiple2(divisors, start):
  while True:    
    for d in divisors:
      if start%d==0:
        return start    
    start+=1