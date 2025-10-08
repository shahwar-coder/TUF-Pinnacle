'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

*
**
***
****
*****
****
***
**
*

Print the pattern in the function given to you.
'''

class Solution:
    def pattern10(self, n):
        for i in range(1, n+1):
            print('*'*i)
        for i in range(n-1,0,-1):
            print('*'*i)


'''
Step-by-step explanation:

1️⃣ Outer loop 1 → n:
    - Prints increasing stars (1 to n).

2️⃣ Outer loop n−1 → 1:
    - Prints decreasing stars (n−1 to 1).

3️⃣ Combined pattern for n=5:
*
**
***
****
*****
****
***
**
*

The two loops mirror each other perfectly, forming an up-then-down star shape.
'''
