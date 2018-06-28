Given an array of integers inputArray, find the contiguous subarray which has the maximum sum. Return that sum.

Example

For inputArray = [-1, 7, -2, 3, 4, 0, 1, -1], the output should be
maxSubarray(inputArray) = 13.
It is the sum of the subarray [7, -2, 3, 4, 0, 1] and no other contiguous subarray has a larger sum.

For inputArray = [-1, -2, -5, -1], the output should be
maxSubarray(inputArray) = 0.
The contiguous subarray with the largest sum is [], because all others will have negative sum.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

Guaranteed constraints:
1 ≤ inputArray.length ≤ 10,
-10 ≤ inputArray[i] ≤ 10.

[output] integer