def commonCharacterCount(s1, s2):
  a1=[0]*26
  a2=[0]*26
  for c in s1:
    a1[ord(c)-97]+=1
  for c in s2:
    a2[ord(c)-97]+=1
  c=0
  for i in range(26):
    c+=min(a1[i],a2[i])
  return c