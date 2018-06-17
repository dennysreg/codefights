def sumdigits(n):
  s=0
  while n:
    s+=n%10
    n//=10
  return s
def compara(a,b):
  sa=sumdigits(a)
  sb=sumdigits(b)
  if sa < sb :
    return -1
  elif sa==sb:
    return a -b
  return 1
def digitalSumSort(a):
  return sorted(a,cmp=compara)