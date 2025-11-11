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

'''
Key Idea:
- The GCD of two numbers doesn’t change if the larger number is replaced 
  by its remainder when divided by the smaller.
- Formula: gcd(a, b) = gcd(b, a % b)
- Continue until the remainder becomes 0.
- Works regardless of which number (n1 or n2) is larger.
'''

# n1 = 4, n2 = 6

# Step 1: gcd(6, 4)
# Step 2: gcd(4, 6 % 4) = gcd(4, 2)
# Step 3: gcd(2, 4 % 2) = gcd(2, 0)
# → GCD = 2



# n1 = 48, n2 = 18

# Step 1: gcd(48, 18)
# Step 2: gcd(18, 48 % 18) = gcd(18, 12)
# Step 3: gcd(12, 18 % 12) = gcd(12, 6)
# Step 4: gcd(6, 12 % 6) = gcd(6, 0)
# → GCD = 6




# n1 = 9, n2 = 8

# Step 1: gcd(9, 8)
# Step 2: gcd(8, 9 % 8) = gcd(8, 1)
# Step 3: gcd(1, 8 % 1) = gcd(1, 0)
# → GCD = 1


"""
GCD of Two Numbers

Given two integers n1 and n2, find their Greatest Common Divisor (GCD).
The GCD is the largest positive integer that divides both numbers without a remainder.

Input: two integers n1, n2
Output: single integer — the GCD of n1 and n2

Examples:
1) Input: n1 = 4, n2 = 6
   Output: 2
   Explanation: divisors of 4 = {1,2,4}, of 6 = {1,2,3,6} → GCD = 2

2) Input: n1 = 9, n2 = 8
   Output: 1
   Explanation: divisors of 9 = {1,3,9}, of 8 = {1,2,4,8} → GCD = 1
"""

'''
Key Idea:
- The GCD of two numbers doesn’t change if the larger number is replaced 
  by its remainder when divided by the smaller.
- Formula: gcd(a, b) = gcd(b, a % b)
- Continue until the remainder becomes 0.
- Works regardless of which number (n1 or n2) is larger.
'''

# Example 1
# n1 = 4, n2 = 6
# Step 1: gcd(6, 4)
# Step 2: gcd(4, 6 % 4) = gcd(4, 2)
# Step 3: gcd(2, 4 % 2) = gcd(2, 0)
# → GCD = 2

# Example 2
# n1 = 48, n2 = 18
# Step 1: gcd(48, 18)
# Step 2: gcd(18, 48 % 18) = gcd(18, 12)
# Step 3: gcd(12, 18 % 12) = gcd(12, 6)
# Step 4: gcd(6, 12 % 6) = gcd(6, 0)
# → GCD = 6

# Example 3
# n1 = 9, n2 = 8
# Step 1: gcd(9, 8)
# Step 2: gcd(8, 9 % 8) = gcd(8, 1)
# Step 3: gcd(1, 8 % 1) = gcd(1, 0)
# → GCD = 1


class Solution:
    def GCD(self, n1, n2):
        """
        Compute the Greatest Common Divisor (GCD) using
        the Euclidean algorithm. Handles zeros and negatives.
        """
        n1, n2 = abs(n1), abs(n2)

        # Edge cases: if one number is 0, return the other
        if n1 == 0:
            return n2
        if n2 == 0:
            return n1

        # Euclidean Algorithm (order doesn't matter)
        while n2 != 0:
            n1, n2 = n2, n1 % n2
        return n1

