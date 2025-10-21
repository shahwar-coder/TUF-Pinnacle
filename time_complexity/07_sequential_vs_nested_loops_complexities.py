'''
Q1. What’s the rule for sequential loops in time complexity?
Ans:
- When loops run **one after another**, their complexities **add up**.
- But we only keep the dominant term in Big-O notation.
'''
# Example 1: Sequential loops
for i in range(n):     # O(n)
    pass
for j in range(n):     # O(n)
    pass
# Total = O(n) + O(n) = O(2n) → O(n)



'''
Q2. What’s the rule for nested loops?
Ans:
- When a loop runs **inside another**, their complexities **multiply**.
- Total = product of iteration counts.
'''
# Example 2: Nested loops
for i in range(n):         # Outer → O(n)
    for j in range(n):     # Inner → O(n)
        pass
# Total = O(n × n) = O(n²)



'''
Q3. How do mixed loops combine (some sequential, some nested)?
Ans:
- Apply addition and multiplication rules in order.
- Then keep the **dominant term** (the slowest-growing one).
'''
# Example 3: Mixed case
for i in range(n):         # O(n)
    for j in range(n):     # O(n)
        pass               # → O(n²)
for k in range(n):         # + O(n)
    pass
# Total = O(n² + n) = O(n²)



'''
# One loop
Q3. How do constant loops affect complexity?
Ans:
- Constants are ignored. Loops that run a fixed number of times → O(1).
'''
for i in range(10):  # Constant range
    pass
# Always 10 steps → O(1)



'''
Q4. Quick shorthand
✔ Sequential → add  
✔ Nested → multiply  
✔ Dependent → sum of counts  
✔ Dominant term decides final O()  
✔ Constants vanish (O(1))
'''
