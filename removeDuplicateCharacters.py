def removeDuplicateCharacters(str):
  d={}
  r =[]
  for c in str:
    if c not in d:
      d[c]=1
    else:
      d[c]+=1
  for c in str:
    if d[c]==1:
      r.appe
  return "".join(r)