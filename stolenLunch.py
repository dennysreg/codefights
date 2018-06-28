def stolenLunch(note):
  a={}
  b={}
  for i in range(10):
    letra = chr(ord('a')+i) 
    a[str(i)] = letra
    b[letra] = str(i)
  
  r=[]
  for c in note:
    if c in a:
      r.append(a[c])
    elif c in b:
      r.append(b[c])
    else:
      r.append(c)
  return "".join(r)