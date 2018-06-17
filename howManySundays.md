We need a function that calculates the number of Sundays after a specific day for a given period.

Example

For n = 9 and startDay = "Saturday", the output should be
howManySundays(n, startDay) = 2;
For n = 7 and startDay = "Sunday", the output should be
howManySundays(n, startDay) = 1.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
3 ≤ n ≤ 25.

[input] string startDay

A string representing some day of the week.

[output] integer

Number of Sundays during the next n days given that startDay is the day of the week today.