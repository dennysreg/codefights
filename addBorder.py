def addBorder(picture):
  r=[]
  l = len(picture[0])
  r.append('*' +l*'*' +'*')
  for i in range(len(picture)):
    r.append('*'+picture[i]+'*')
  r.append('*'+l*'*'+'*')
  return r