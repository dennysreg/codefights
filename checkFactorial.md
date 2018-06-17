Given an integer n, check if n = k! for some non-negative integer k.

Example

For n = 120, the output should be
checkFactorial(n) = true.

Here 120 = 5!.

For n = 25, the output should be
checkFactorial(n) = false.

Here 4! = 24 < 25 < 120 = 5!.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A positive integer.

Guaranteed constraints:
1 = n = 5 · 10^5.

[output] boolean

true if such k that n = k! exists, false otherwise.