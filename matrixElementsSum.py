def matrixElementsSum(matrix):
  s=0
  for c in range(len(matrix[0])):    
    for r in range(len(matrix)):
      if matrix[r][c]==0:
        break
      s+=matrix[r][c]
  return s