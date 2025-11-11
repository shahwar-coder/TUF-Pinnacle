"""
GCD of Two Numbers

Given two integers n1 and n2, return their Greatest Common Divisor (GCD).
The GCD of two integers is the largest positive integer that divides both numbers.

Input: two integers n1, n2
Output: single integer — their GCD

Examples:
1) Input: n1 = 4, n2 = 6
   Output: 2
   Explanation: divisors of 4 = {1,2,4}, of 6 = {1,2,3,6} → GCD = 2

2) Input: n1 = 9, n2 = 8
   Output: 1
   Explanation: divisors of 9 = {1,3,9}, of 8 = {1,2,4,8} → GCD = 1
"""

class Solution:
    def GCD(self, n1, n2):
        larger_number=max([n1,n2])
        for i in range(larger_number,0,-1):
            if n1%i==0 and n2%i==0:
                return i
