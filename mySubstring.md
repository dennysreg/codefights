Implement an algorithm that can output the substring of the given string within specified bounds.

Example

For inputString = "abcde", l = 2 and r = 3, the output should be
mySubstring(inputString, l, r) = "cd".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

Guaranteed constraints:
1 ≤ inputString.length ≤ 10.

[input] integer l

A positive integer representing the left bound of the substring.

Guaranteed constraints:
0 ≤ l ≤ r.

[input] integer r

A positive integer representing the right bound of the substring.

Guaranteed constraints:
l ≤ r < inputString.length.

[output] string

substring of inputString from the lth character up to the rth, inclusive.