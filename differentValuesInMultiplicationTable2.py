def differentValuesInMultiplicationTable2(n, m):
  s=set()
  for i in range(1,n+1):
    for j in range(1,m+1):
      s.add(i*j)
  return len(s)