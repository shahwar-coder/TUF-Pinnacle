'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

*****
*   *
*   *
*   *
*****

Print the pattern in the function given to you.
'''

class Solution:
    def pattern21(self, n):
        for i in range(1, n+1):
            if i==1 or i==n:
                print('*'*n)
            else:
                print('*' + ' '*(n-2) + '*')



'''
Step-by-step explanation:

1️⃣ Loop over each row (1 → n)
2️⃣ For first and last row:
       print('*' * n)
3️⃣ For middle rows:
       print('*' + ' ' * (n - 2) + '*')
4️⃣ Works for any n ≥ 2

Example (n=5):
*****
*   *
*   *
*   *
*****
'''
