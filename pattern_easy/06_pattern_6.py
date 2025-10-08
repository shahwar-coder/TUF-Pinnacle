'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

12345
1234
123
12
1

Print the pattern in the function given to you.
'''

class Solution:
    def pattern6(self, n):
        for i in range(1, n+1):
            for j in range(1, n-i+2):
                print(j, end='')
            print()


'''
Step-by-step explanation:

1. Outer loop controls rows (i = 1 → n).
2. Inner loop prints numbers 1 through (n − i + 1).
   Example:
     For i=1 → prints 1..5
     For i=2 → prints 1..4
     …
3. end='' keeps numbers on the same line.
4. print() after inner loop moves to the next row.

Result for n=5:
12345
1234
123
12
1
'''
