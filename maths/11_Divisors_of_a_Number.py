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

# Step-by-step execution for n = 36
# ---------------------------------

# We loop i from 1 to int(sqrt(36)) = 6
# and add both i and n // i whenever n % i == 0

# Initial:
#     n = 36
#     divs = {}

# Iteration details:
# ------------------

# i = 1:
#     36 % 1 == 0 → True
#     Add (1, 36 // 1 = 36)
#     divs = {1, 36}

# i = 2:
#     36 % 2 == 0 → True
#     Add (2, 36 // 2 = 18)
#     divs = {1, 2, 18, 36}

# i = 3:
#     36 % 3 == 0 → True
#     Add (3, 36 // 3 = 12)
#     divs = {1, 2, 3, 12, 18, 36}

# i = 4:
#     36 % 4 == 0 → True
#     Add (4, 36 // 4 = 9)
#     divs = {1, 2, 3, 4, 9, 12, 18, 36}

# i = 5:
#     36 % 5 == 1 → False
#     Skip

# i = 6:
#     36 % 6 == 0 → True
#     Add (6, 36 // 6 = 6)
#     (both same, only one added)
#     divs = {1, 2, 3, 4, 6, 9, 12, 18, 36}

# After loop ends:
# ----------------
# Sorted divisors = [1, 2, 3, 4, 6, 9, 12, 18, 36]

# Hence output → [1, 2, 3, 4, 6, 9, 12, 18, 36]


      
# For smaller inputs this is fine as well but above is best.
# class Solution:
#     def divisors(self, n):
#         return [number for number in range(1,n+1) if n%number==0]
