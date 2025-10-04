'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

1
12
123
1234
12345

Print the pattern in the function given to you.
'''

class Solution:
    def pattern3(self, n):
        for i in range(1,n+1):
            for j in range(1, i+1):
                print(j, end='')
            print()


'''
Step-by-step explanation:

1. Outer loop from i = 1 to n:
   - Controls how many rows to print.

2. Inner loop from j = 1 to i:
   - Prints numbers from 1 to current row number.

3. end='' prevents newline after each number.
   - print() after inner loop moves to the next line.

Example:
For i = 3:
   Inner loop prints: 1 2 3 → output: "123"
'''
