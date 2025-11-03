"""
Count all Digits of a Number

You are given an integer n. You need to return the number of digits in the number.

The number will have no leading zeroes, except when the number is 0 itself.

Examples:

Input: n = 4
Output: 1
Explanation: There is only 1 digit in 4.

Input: n = 14
Output: 2
Explanation: There are 2 digits in 14.

Input: n = 234
Output: 3
"""

class Solution:
    def countDigit(self, n):
        return len(str(abs(n)))


'''Notes
- abs , otherwise negative numbers will return wrong length
- pure math can also be applied as below
'''

import math
class Solution:
    def countDigit(self, n):
        if n==0:
            return 1
        return int(math.log10(abs(n))) + 1
