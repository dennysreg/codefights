def arraySumAdjacentDifference(inputArray):
  s=0
  for i in range(1,len(inputArray)):
    s+=abs(inputArray[i-1]-inputArray[i])
  return s
