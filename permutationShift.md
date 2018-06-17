Define the permutation element shift as the difference between the element's value and its index. For example, for permutation [1, 0, 2, 3] of array [0, 1, 2, 3] shifts for the respective elements are [1, -1, 0, 0].

Define the permutation shift as the difference between the maximal and the minimal element shifts among all of the permutation elements.

Given a permutation of integers from 0 to n - 1 for some integer n, find its shift.

Example

For permutation = [1, 0, 2, 3], the output should be
permutationShift(permutation) = 2.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer permutation

Array of integers containing each integer from 0 to n - 1, inclusive, exactly once (where n is the array length).

Guaranteed constraints:
1 ≤ permutation.length ≤ 10,

[output] integer