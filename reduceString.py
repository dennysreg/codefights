def reduceString(inputString):
  if inputString=="":
    return ""
  if inputString[0]==inputString[-1]:
    return reduceString(inputString[1:-1])
  else:
    return inputString
  