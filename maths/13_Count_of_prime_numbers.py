"""
Count of Prime Numbers till N

You are given an integer n.
You need to find out the number of prime numbers in the range [1, n] (inclusive).

Return the count of prime numbers in this range.

Definition:
------------
A prime number is a number which has no divisors 
except 1 and itself.

Examples:
----------
Input: n = 6
Output: 3
Explanation: Prime numbers in the range [1, 6] are 2, 3, and 5.

Input: n = 10
Output: 4
Explanation: Prime numbers in the range [1, 10] are 2, 3, 5, and 7.
"""

class Solution:
    def primeUptoN(self, n):
        """
        Sieve of Erastothenes
        """
        boolean_blocks = [True]*(n+1)
        boolean_blocks[0]=boolean_blocks[1]=False
        for i in range(2, int(n**0.5)+1):
            if boolean_blocks[i]:
                for multiple in range(i*i, n+1, i):
                    boolean_blocks[multiple]=False
        return sum(boolean_blocks)

# 🔹 Quick Notes — Sieve of Eratosthenes
# ---------------------------------------
# 1️⃣ Think of N boxes labeled 0 to N.
#     Each box says "True" → means "I’m prime!"
#
# 2️⃣ 0 and 1 are never prime → mark them False.
#
# 3️⃣ Start from 2, the first prime.
#     For every prime number i,
#     cross out (mark False) all its multiples: i*i, i*i+i, i*i+2i, ...
#
# 4️⃣ Why start from i*i?
#     Because smaller multiples (like 2*i, 3*i) were already
#     crossed out by smaller primes.
#
# 5️⃣ Stop at √N — beyond that, all composites are already marked.
#
# 6️⃣ In the end, boxes still marked True are primes.
#     Counting them gives how many primes exist up to N.
#
# ⚙️ Complexity:
# Time → O(n log log n)
# Space → O(n)
