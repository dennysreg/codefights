Given a certain array, find out if it's a permutation of numbers from 1 to a given integer.

Example

For n = 4 and inputArray = [1, 3, 2, 4], the output should be
isPermutation(n, inputArray) = true;
For n = 3 and inputArray = [2, 3, 2], the output should be
isPermutation(n, inputArray) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 10.

[input] array.integer inputArray

Array of integers of length n.

Guaranteed constraints:
inputArray.length = n,
-1000 ≤ inputArray[i] ≤ 1000.

[output] boolean

true if inputArray represents a permutation of integers from 1 to n, false otherwise.