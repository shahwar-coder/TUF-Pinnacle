'''
Q1. What is the purpose of Complexity Analysis?
Ans:
- To measure how efficiently an algorithm uses **time** and **memory** as input size grows.
- It helps compare and choose the best algorithm for a problem.
'''
# Example:
# Algorithm A takes 0.01s for 1000 inputs.
# Algorithm B takes 0.01s for 10,000 inputs.
# → B scales better (lower time complexity).



'''
Q2. What’s the difference between time and space complexity?
Ans:
- Time Complexity → how the number of operations grows with input size (n).  
- Space Complexity → how much additional memory is needed.
'''
# Example: Using extra list → more space
nums = [1, 2, 3, 4]
squares = [x**2 for x in nums]  # O(n) time, O(n) space



'''
Q3. What is Big O notation used for?
Ans:
- To describe the **upper bound** of an algorithm’s growth rate.
- It ignores constants and focuses on long-term scaling behavior.
'''
# If an algorithm runs in 3n + 2 steps, we write O(n),
# since constants don’t affect growth trend for large n.



'''
Q4. What is the general order of growth from fastest to slowest?
Ans:
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
'''
# O(1): Accessing list[i]
# O(log n): Binary search
# O(n): Linear search
# O(n log n): Merge sort
# O(n²): Bubble sort
# O(2ⁿ): Recursive subset generation
# O(n!): Traveling salesman problem



'''
Q5. Why is Big O considered an “asymptotic” measure?
Ans:
- It focuses on growth **as n → ∞** (large inputs),
  ignoring small-scale effects and constants.
'''
# Example: O(n)
for i in range(1000):  # constants ignored
    pass



'''
Q6. Quick shorthand
✔ Time = speed, Space = memory  
✔ Big O = upper bound  
✔ Focuses on scalability  
✔ Ignores constants and small variations  
✔ Helps pick efficient algorithms
'''


