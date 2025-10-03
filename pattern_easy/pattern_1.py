'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

*****
*****
*****
*****
*****
'''

class Solution:
    def pattern1(self, n):
        for _ in range(1,n+1):
            print('*'*n)

# _ instead of i for looping because i will not get used if introduced.
# you might also return the pattern string if not asked to print eg. 

'''
return '\n'.join(['*' * n for _ in range(1, n+1)])
'''
