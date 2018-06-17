def isSumOfConsecutive2(n):
  c=0
  for i in range(1,n):
    s=i
    tmp=n    
    while tmp>0:      
      tmp-=s
      s+=1
    if tmp==0:
      c+=1
  return c