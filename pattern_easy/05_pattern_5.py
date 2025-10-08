'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

*****
****
***
**
*

Print the pattern in the function given to you.
'''

class Solution:
    def pattern5(self, n):
        print('\n'.join(['*'*(n-i+1) for i in range(1, n+1)]))


'''
Step-by-step breakdown:

1. Loop i from 1 to n:
   - For each i, print (n - i + 1) stars.

2. When i = 1 → n - 1 + 1 = n stars
   When i = n → n - n + 1 = 1 star

3. Use list comprehension to generate all lines:
   ['*' * (n - i + 1) for i in range(1, n + 1)]

4. Join them with newline ('\n') for final multi-line output.

Final Output (n=5):
*****
****
***
**
*
'''
