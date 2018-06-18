def decipher(cipher):
  r=[]
  i=0
  while i < len(cipher):
    d=0
    if cipher[i] =='1':
      d = int(cipher[i:i+3])
      i+=3
    else:
      d = int(cipher[i:i+2])
      i+=2
    r.append(chr(d))
    
  return "".join(r)