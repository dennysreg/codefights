def crossingSum(matrix, a, b):
  s=0
  for i in range(len(matrix)):
    s+=matrix[i][b]
  s+=sum(matrix[a])
  s-=matrix[a][b]
  return s