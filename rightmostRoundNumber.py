def rightmostRoundNumber(inputArray):
  k=-1
  for i in range(len(inputArray)):
    if inputArray[i]%10==0:
      k=i      
  return k