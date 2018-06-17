def evenNumbersBeforeFixed(sequence, fixedElement):
  i=0
  c=0
  while i < len(sequence) and sequence[i]!=fixedElement:
    print (sequence[i])
    if sequence[i]%2==0:
      c+=1    
    i+=1
  if i < len(sequence) and sequence[i]==fixedElement:
    return c
  return c if sequence[i-1] == fixedElement else -1