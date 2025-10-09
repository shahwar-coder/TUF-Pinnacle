'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

E 
D E 
C D E 
B C D E 
A B C D E

Print the pattern in the function given to you.
'''

class Solution:
    def pattern18(self, n):
        for i in range(1, n+1):
            for j in range(i, 0, -1):
                print(chr(64+(n-j+1)), end=' ')
            print()


'''
Step-by-step explanation:

1️⃣ For each row i (1 → n):
   - Start from the letter corresponding to (n - i + 1).
   - End at the letter 'E' (for n = 5).

2️⃣ Inner loop prints letters from chr(64 + start) to chr(64 + n).

Example (n=5):
Row 1 → E
Row 2 → D E
Row 3 → C D E
Row 4 → B C D E
Row 5 → A B C D E
'''
