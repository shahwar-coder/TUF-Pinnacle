'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

ABCDE
ABCD
ABC
AB
A

Print the pattern in the function given to you.
'''

class Solution:
    def pattern15(self, n):
        for i in range(n, 0, -1):
            for j in range(1, i+1):
                print(chr(64+j), end='')
            print()


'''
Step-by-step explanation:

1️⃣ Outer loop (n → 1):
   - Controls how many letters per row.
   - Decreases by 1 each row.

2️⃣ Inner loop (1 → i):
   - Prints 'A' to the i-th letter.

3️⃣ chr(64 + j):
   - Converts number to uppercase letter.

Example (n=5):
ABCDE
ABCD
ABC
AB
A
'''
