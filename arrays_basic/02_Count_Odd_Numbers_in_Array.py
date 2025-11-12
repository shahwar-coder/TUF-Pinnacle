'''
Count Odd Numbers in Array
'''

class Solution:
    def countOdd(self, arr, n):
        return sum(1 for i in arr if i%2==1)


# ALSO WORKS, (adding of Trues)
# def countOdd(self, arr):
#     return sum(i % 2 for i in arr)
