'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

    *
   ***
  *****
 *******
*********

Print the pattern in the function given to you.
'''

class Solution:
    def pattern7(self, n):
        for i in range(1, n+1):
            print(' '*(n-i) + '*'*(2*i-1))


'''
Step-by-step explanation:

1️⃣ For each row i (1 to n):
    - Leading spaces: " " * (n - i)
      → Centers the stars by reducing space each line.
    - Stars: "*" * (2 * i - 1)
      → Increases by 2 each row (1, 3, 5, 7...).

2️⃣ Combine and print:
    print(spaces + stars)

Example for n=5:
Row 1 → '    *'
Row 2 → '   ***'
Row 3 → '  *****'
Row 4 → ' *******'
Row 5 → '*********'
'''
