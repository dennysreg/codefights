def arrayMaximalDifference(inputArray):
  m=-1
  inputArray= sorted(inputArray)
  for i in range(len(inputArray)):
    for j in range(i+1,len(inputArray)):
      d = inputArray[j] - inputArray[i]
      if d > m:
        m=d
  return m