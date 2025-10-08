'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

    * 
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *

Print the pattern in the function given to you.
'''

class Solution:
    def pattern9(self, n):
        for i in range(1, n+1):
            print(' '*(n-i) + '*'*(2*i-1))
        for i in range(n, 0, -1):
            print(' '*(n-i) + '*'*(2*i-1))
          

'''
Step-by-step explanation:

1️⃣ Upper half:
   - Loop i = 1 → n
   - Spaces: (n - i)
   - Stars: (2 * i - 1)

2️⃣ Lower half:
   - Loop i = n → 1
   - Same formulas reused.

3️⃣ Example for n=5:
   Upper half:
       *        (4 spaces, 1 star)
      ***       (3 spaces, 3 stars)
     *****      (2 spaces, 5 stars)
    *******     (1 space, 7 stars)
   *********    (0 spaces, 9 stars)

   Lower half (mirror):
   *********
    *******
     *****
      ***
       *

4️⃣ Print each line by concatenating spaces and stars:
   print(' '*(n-i) + '*'*(2*i-1))
'''


