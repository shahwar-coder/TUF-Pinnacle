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

1️⃣ Upper half loop (1 → n)
   - Spaces: (n - i)
   - Stars:  (2 * i - 1)
   - Forms a growing pyramid.

2️⃣ Lower half loop (n → 1)
   - Same logic in reverse.
   - Forms the inverted reflection.

3️⃣ For n = 5:
   Upper half:     Lower half:
       *            *********
      ***             *******
     *****              *****
    *******              ***
   *********              *

4️⃣ Combining both gives a perfect diamond.
'''



