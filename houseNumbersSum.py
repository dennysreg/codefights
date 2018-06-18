def houseNumbersSum(inputArray):
  i=0
  s=0
  while i < len(inputArray) and inputArray[i]!=0:
    s+=inputArray[i]
    i+=1
  return s
