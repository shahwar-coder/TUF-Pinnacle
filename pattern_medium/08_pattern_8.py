'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

*********
 *******
  *****
   ***
    *

Print the pattern in the function given to you.
'''

class Solution:
    def pattern8(self, n):
        for i in range(n, 0, -1):
            print(' '*(n-i) + '*'*(2*i-1))


'''
Step-by-step explanation:

1️⃣ The loop runs backward from n → 1.
   - This naturally decreases the number of stars per row.

2️⃣ Leading spaces:
    ' ' * (n - i)
    - Starts from 0, increases each line to shift pattern rightward.

3️⃣ Stars:
    '*' * (2 * i - 1)
    - Starts at (2*n - 1) stars, decreases by 2 each line.

4️⃣ Combine and print:
    print(spaces + stars)

Example for n=5:
i=5 → 0 spaces + 9 stars → *********
i=4 → 1 space  + 7 stars →  *******
i=3 → 2 spaces + 5 stars →   *****
i=2 → 3 spaces + 3 stars →    ***
i=1 → 4 spaces + 1 star  →     *
'''
