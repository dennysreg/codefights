def findPath(matrix):
  #busca el 1
  def getpos():
    pos= (0,0)
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
        if matrix[i][j]==1:
          return (i,j)
            
  q = [getpos()]
  v = []
  while len(q) > 0:
    (f,c) = q.pop()
    v.append((f,c))
    for (i,j) in [(-1,0),(0,1),(1,0),(0,-1)]:
      _f = f + i
      _c = c + j
      if (_f,_c) not in v and _f >=0 and _f < len(matrix) and _c >=0 and _c <len(matrix[0]):
        if matrix[_f][_c] == matrix[f][c]+1:          
          q.append((_f,_c))  
  return len(v)==len(matrix)*len(matrix[0])