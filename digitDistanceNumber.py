def digitDistanceNumber(n):
  s=str(n)
  r=[]
  for i in range(1,len(s)):
    r.append(str(abs(int(s[i])-int(s[i-1]))))
  return int("".join(r))