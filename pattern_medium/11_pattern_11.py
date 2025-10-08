'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1

Print the pattern in the function given to you.
'''

class Solution:
    def pattern11(self, n):
        accumulated_string=''
        for i in range(1, n+1):
            if i%2==1: #odd
                accumulated_string = '1 ' + accumulated_string
                print(accumulated_string)
            else:
                accumulated_string = '0 ' + accumulated_string
                print(accumulated_string)
