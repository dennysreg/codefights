Check if the given matrix is lower triangular.

Example

For

matrix = [[1, 0, 0], 
          [4, 0, 0], 
          [0, 3, 3]]
the output should be
isLowerTriangularMatrix(matrix) = true;

For

matrix = [[1, 0, 1], 
          [0, 5, 0], 
          [2, 0, 3]]
the output should be
isLowerTriangularMatrix(matrix) = false.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer matrix

2-dimensional array of integers representing a square matrix.

Guaranteed constraints:
1 ≤ matrix.length ≤ 5,
matrix[i].length = matrix.length,
-1000 ≤ matrix[i][j] ≤ 1000.

[output] boolean

true if matrix is lower triangular matrix, false otherwise.