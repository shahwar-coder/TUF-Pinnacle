'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

*
**
***
****
*****

Print the pattern in the function given to you.
'''

class Solution:
    def pattern2(self, n):
        print('\n'.join(['*'*i for i in range(1,n+1)]))
      

'''
Step-by-step explanation:

1. Use a list comprehension to build each line:
   '*'*i  → gives i stars on row i

2. range(1, n+1):
   ensures we generate lines from 1 to n

3. '\n'.join([...]):
   joins the list of star-strings into one string with newlines

4. print(...):
   prints the entire pattern at once

Example for n = 3:
   ['*', '**', '***'] → joined → "*\n**\n***"
'''
