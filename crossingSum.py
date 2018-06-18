def crossingSum(matrix, a, b):
  s=0
  for i in range(len(matrix[0])):
    s+=matrix[a][i]
  for i in range(len(matrix)):
    s+=matrix[i][b]
  s-=matrix[a][b]
  return s