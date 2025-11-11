"""
LCM of Two Numbers

You are given two integers n1 and n2.
You need to find the Lowest Common Multiple (LCM) of the two given numbers.

Return the LCM of the two numbers.

Definition:
------------
The Lowest Common Multiple (LCM) of two integers is the 
lowest positive integer that is divisible by both the integers.

Examples:
----------
Input: n1 = 4, n2 = 6
Output: 12
Explanation: 4 * 3 = 12, 6 * 2 = 12
12 is the lowest integer that is divisible by both 4 and 6.

Input: n1 = 3, n2 = 5
Output: 15
Explanation: 3 * 5 = 15, 5 * 3 = 15
15 is the lowest integer that is divisible by both 3 and 5.

Input: n1 = 4, n2 = 12
Output: 12
Explanation: 12 is the lowest integer that is divisible by both 4 and 12.
"""

# Key Idea: LCM using GCD

# - The Least Common Multiple (LCM) of two integers a and b 
#   is the smallest positive integer that is divisible by both.

# - There’s a fundamental relationship between LCM and GCD:

#       LCM(a, b) × GCD(a, b) = a × b

# - So, we can compute LCM efficiently as:

#       LCM(a, b) = abs(a * b) // GCD(a, b)

# - This approach is fast because GCD can be found efficiently 
#   using the Euclidean Algorithm with O(log(min(a, b))) time.

# Example:
#     a = 12, b = 18
#     GCD = 6
#     LCM = (12 * 18) / 6 = 36


class Solution:
    def GCD(self, n1, n2):
        """
        Finding GCD as part of finding LCM
        """
        while n2!=0:
            n1, n2 = n2, n1%n2
        return n1

    def LCM(self, n1, n2):
        """
        Finding Lowest Common Multiple
        """
        if n1==0:
            return 0
        if n2==0:
            return 0
        return abs(n1*n2) // self.GCD(n1, n2)

# ✅ GCD uses Euclidean algorithm — very fast (O(log min(a,b))).
# The Euclidean method repeatedly replaces (a, b) with (b, a % b) until the remainder becomes 0.
# log min(a, b) means it grows very slowly — proportional to the logarithm of the smaller number.
# So instead of checking all numbers up to min(a, b) (which would take linear time O(min(a, b))), 
      # the Euclidean algorithm only takes around a few divisions — even for very large inputs.
