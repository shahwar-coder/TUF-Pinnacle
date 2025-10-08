'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15

Print the pattern in the function given to you.
'''

class Solution:
    def pattern13(self, n):
        counter=1
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(counter, end=' ')
                counter+=1
            print()


'''
Step-by-step explanation:

1️⃣ Initialize counter = 1

2️⃣ For each row i = 1 → n:
    - Print i numbers starting from current counter.
    - Increment counter after each print.

3️⃣ After each row, print() to move to the next line.

Example for n=5:
Row 1: 1
Row 2: 2 3
Row 3: 4 5 6
Row 4: 7 8 9 10
Row 5: 11 12 13 14 15
'''
