def summaryProficiency(a, n, m):
  r=[]
  for p in a:
    if len(r)<n and p >= m:
      r.append(p)
  return sum(r)