'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

A
AB
ABC
ABCD
ABCDE

Print the pattern in the function given to you.
'''

class Solution:
    def pattern14(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(chr(64+j), end='')
            print()



'''
Step-by-step explanation:

1️⃣ Outer loop (1 → n):
   - Controls number of rows.

2️⃣ Inner loop (1 → i):
   - Prints letters from 'A' to 'A' + i - 1.

3️⃣ Formula: chr(64 + j)
   - Since chr(65) = 'A', chr(66) = 'B', and so on.

4️⃣ Output for n=5:
A
AB
ABC
ABCD
ABCDE
'''
