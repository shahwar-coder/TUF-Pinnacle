"""
Divisors of a Number

You are given an integer n.
You need to find all the divisors of n and return them 
as a list (or array) in sorted order.

Definition:
------------
A number which completely divides another number (i.e., leaves remainder 0)
is called its divisor.

Examples:
----------
Input: n = 6
Output: [1, 2, 3, 6]
Explanation: The divisors of 6 are 1, 2, 3, and 6.

Input: n = 8
Output: [1, 2, 4, 8]
Explanation: The divisors of 8 are 1, 2, 4, and 8.
"""

# Optimal Solution (Get Pairs Approach)
import math
class Solution:
    def divisors(self, n):
        if n<0:
            return []
        result = set()
        for i in range(1,int(math.sqrt(n))+1):
            if n%i==0:
                result.add(i)
                result.add(n//i)
        return sorted(result)

      
# For smaller inputs this is fine as well but above is best.
# class Solution:
#     def divisors(self, n):
#         return [number for number in range(1,n+1) if n%number==0]
