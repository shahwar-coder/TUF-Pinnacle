'''
🧮 Problem: Find the Largest Digit in a Number

You are given an integer n.
Your task is to find and return the largest digit present in the number.

Examples:

Input: n = 25
Output: 5
Explanation: The digits are 2 and 5. The largest digit is 5.

Input: n = 99
Output: 9
Explanation: Both digits are 9, so the largest digit is 9.
'''

class Solution:
    def largestDigit(self, n):
        return max(map(int, str(abs(n))))


# Arithmetic Version.
# def largestDigit(self, n):
#     n = abs(n)
#     largest = 0
#     while n > 0:
#         largest = max(largest, n % 10)
#         n //= 10
#     return largest
