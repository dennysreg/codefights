def isLowerTriangularMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j]:
                return False
    return True
