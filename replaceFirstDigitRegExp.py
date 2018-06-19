def replaceFirstDigitRegExp(input):
  i=0
  while i <len(input) and input[i].isdigit()==False:
    i+=1
  return input[:i]+'#'+input[i+1:]