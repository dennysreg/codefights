def arrayMode(sequence):
  d={}
  for c in sequence:
    d[c] = 1 if c not in d else d[c]+1
  return sorted(d,key=d.get,reverse=True)[0]  