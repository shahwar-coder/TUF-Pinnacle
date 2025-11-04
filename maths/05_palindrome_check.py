"""
💡 Problem: Palindrome Number  

You are given an integer `n`.  
You need to check whether the number is a **palindrome number** or not.  

Return **True** if it’s a palindrome number, otherwise return **False**.

A **palindrome number** is a number that reads the same both **left to right** and **right to left**.
---
### Examples:

Input: n = 121  
Output: True  
Explanation:  
When read from left to right → 121  
When read from right to left → 121  

Input: n = 123  
Output: False  
Explanation:  
When read from left to right → 123  
When read from right to left → 321
"""

class Solution:
    def isPalindrome(self, n):
        if n<0:
            return False
        if n==0:
            return True
        return str(n)==str(n)[::-1]
