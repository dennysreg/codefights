def differentDigitsNumberSearch(inputArray):

  for n in inputArray:
    s=str(n)
    if len(set(s))==len(s):
      return n
  return -1