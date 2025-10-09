'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

Print the pattern in the function given to you.
'''

class Solution:
    def pattern19(self, n):
        for i in range(0, n):
            left='*'*(n-i)
            spaces=' '*(i*2)
            right='*'*(n-i)
            print(left + spaces + right)
        for i in range(n-1, -1, -1):
            left='*'*(n-i)
            spaces=' '*(i*2)
            right='*'*(n-i)
            print(left + spaces + right)
