def checkEqualFrequency(inputArray):
  d={}
  for c in inputArray:
    d[c] = 1 if c not in d else d[c]+1
  
  return len(set(d.values()))==1