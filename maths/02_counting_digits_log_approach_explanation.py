import math
class Solution:
    def countDigit(self, n):
        if n==0:
            return 1
        return int(math.log10(abs(n))) + 1


'''
Q1. Why do we check `if n == 0` at the start?
Ans:
Because `log10(0)` is undefined in math.
We handle zero separately and return 1, since 0 has exactly one digit.
'''



'''
Q2. Why do we take `abs(n)` before using `log10()`?
Ans:
`math.log10()` works only for positive numbers.
Taking `abs(n)` lets it handle negative numbers correctly.
'''



'''
Q3. How does the logarithmic formula give the number of digits?
Ans:
For any number `n`,  
`floor(log10(n)) + 1` gives the count of digits.  
Example: `log10(999) ≈ 2.99`, floor is 2 → digits = 2 + 1 = 3.
'''



'''
Q4. What is the time complexity of this method?
Ans:
O(1) — constant time.  
It uses a mathematical formula instead of loops, so speed doesn’t depend on the number size.
'''



'''
Q5. How does this compare to counting digits with a loop or string method?
Ans:
- Loop method: repeatedly divide by 10 → O(log₁₀n)
- String method: convert to string and count → O(log₁₀n)
- Log method: fastest (O(1)) and cleanest mathematically
'''
