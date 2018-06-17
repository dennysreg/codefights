def firstMultiple(divisors, start):
  while True:
    c=0
    for d in divisors:
      if start%d==0:
        c+=1
    if c == len(divisors):
      return start
    start+=1