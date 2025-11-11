"""
Check for Prime Number

You are given an integer n.
You need to check whether the number is prime or not.

Return True if it is a prime number, otherwise return False.

Definition:
------------
A prime number is a number that has no divisors 
except 1 and itself.

Examples:
----------
Input: n = 5
Output: True
Explanation: The only divisors of 5 are 1 and 5.
Hence, 5 is a prime number.

Input: n = 8
Output: False
Explanation: The divisors of 8 are 1, 2, 4, and 8.
Thus, 8 is not a prime number.
"""

# Optimal
class Solution:
    def isPrime(self, n):
        if n<=1:
            return False
            
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True


# Key Idea:
# ----------
# This is an optimal solution to check if a number is prime.

# Why it works:
# -------------
# - To check if n is prime, we only need to test divisibility 
#   up to √n (square root of n), not till n itself.

# - If a number n is composite, it must have a divisor 'i'
#   such that (i * j = n) and one of the two factors is ≤ √n.

# - So, if no number in range [2, √n] divides n evenly,
#   then n has no divisors other than 1 and itself → hence prime.

# Connection with Divisors:
# --------------------------
# This concept is the same as we used for finding divisors of 36.
# There too, we only iterated up to √36 = 6.
# Beyond that point, divisors start repeating as pairs.

# Thus, this √n bound is a powerful optimization 
# used in both divisor and prime number problems.

# Complexity:
# -----------
# Time Complexity: O(√n)
# Space Complexity: O(1)


"""
Dry Run: Prime check for n = 36
--------------------------------

We use the optimized algorithm that tests divisibility for i in [2, int(sqrt(n))].
If any i divides n (n % i == 0) we conclude n is NOT prime and return False.
If no such i is found, n is prime and we return True.

Initial:
    n = 36
    sqrt_bound = int(36**0.5) = 6
    We will test i = 2, 3, 4, 5, 6

Step-by-step iterations:
------------------------

i = 2:
    Check: 36 % 2 == 0 ?
    Evaluation: 36 % 2 == 0 -> True
    Meaning: 2 * 18 = 36, so 2 is a divisor of 36.
    Action: Because we found a divisor in [2, sqrt(n)], we can immediately conclude:
            36 is NOT prime → return False
    (No further i need to be checked; algorithm stops early.)

-- If we continued purely for illustration (we do NOT in the algorithm):

i = 3:
    36 % 3 == 0 -> True  (3 * 12 = 36)

i = 4:
    36 % 4 == 0 -> True  (4 * 9 = 36)

i = 5:
    36 % 5 == 1 -> False

i = 6:
    36 % 6 == 0 -> True  (6 * 6 = 36, square root case)

Conclusion:
-----------
- The algorithm finds divisor 2 at the very first check (i = 2), so it returns False quickly.
- Therefore 36 is NOT prime.
- This demonstrates the power of the √n bound: we only needed to test up to 6, and in practice we often stop much earlier when a small divisor exists.

Complexity reminder:
--------------------
- Worst-case time complexity: O(√n) (when n is prime or has no small factors)
- Best-case (like here): O(1) if a small divisor is found immediately
"""



