def telephoneGame(messages):
  s=messages[0]
  for i in range(1,len(messages)):
    if messages[i]!=s:
      return i
  return -1