def reverseOnDiagonals(matrix):
    l= len(matrix)
    for i in range(len(matrix)/2):
        tmp = matrix[i][i]
        matrix[i][i] = matrix[l-i-1][l-i-1]
        matrix[l-i-1][l-i-1] = tmp

        tmp = matrix[i][l-i-1]
        matrix[i][l-i-1] = matrix[l-i-1][i]
        matrix[l-i-1][i] = tmp
    return matrix