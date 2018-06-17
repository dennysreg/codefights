def isInfiniteProcess(a, b):
  if a==b:
    return False
  return not(b > a and abs(b - a) %2 ==0)