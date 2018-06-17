def oddNumbersBeforeZero(sequence):
  c=0
  i=0
  while i<len(sequence) and sequence[i]!=0:
    if sequence[i]%2!=0:
      c+=1
    i+=1
  return c