def isInformationConsistent(evidences):
  for c in range(len(evidences[0])):
    s=set()
    for r in range(len(evidences)):
      if evidences[r][c]!=0:
        s.add(evidences[r][c])
    if len(s)!=0 and len(s)!=1:
      return False
  return Ture
      