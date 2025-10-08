'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

A
BB
CCC
DDDD
EEEEE

Print the pattern in the function given to you.
'''

class Solution:
    def pattern16(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(chr(64+i), end='')
            print()


'''
Step-by-step explanation:

1️⃣ Outer loop (1 → n):
   - Controls number of rows.

2️⃣ Inner loop (1 → i):
   - Prints the i-th letter (A, B, C...) i times.

3️⃣ Formula: chr(64 + i)
   - 1 → 65 → 'A'
   - 2 → 66 → 'B'
   - etc.

Example (n=5):
A
BB
CCC
DDDD
EEEEE
'''
