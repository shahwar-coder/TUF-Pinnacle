'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

1
22
333
4444
55555

Print the pattern in the function given to you.
'''

class Solution:
    def pattern4(self, n):
        print('\n'.join([str(i)*i for i in range(1, n+1)]))
      

'''
Step-by-step explanation:

1. range(1, n + 1):
   → generates numbers from 1 to n (inclusive)

2. str(i) * i:
   → creates a string where digit i is repeated i times
   Example: i=3 → '3'*3 = '333'

3. The list becomes: ['1', '22', '333', ..., 'nn...n']

4. '\n'.join([...]):
   → joins all strings with newline, forming the final pattern

5. print(...) displays the entire block
'''
