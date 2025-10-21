'''
Q1. What is Space Complexity?
Ans:
- It measures how much memory an algorithm uses as input size grows.
- Includes both **input storage** and **temporary (auxiliary) storage**.
'''
# Example:
# Reading a list of n elements → needs O(n) space just to store input.



'''
Q2. What is the difference between Input Space and Auxiliary Space?
Ans:
- **Input Space:** memory used to store the given input data.
- **Auxiliary Space:** extra memory allocated by the algorithm (temporary data, recursion stack, etc.)
'''
def square(arr):
    result = [x*x for x in arr]
    return result

# Input space: O(n) for arr
# Auxiliary space: O(n) for result
# Total = O(n) + O(n) = O(n)



'''
Q3. Why do we usually focus on auxiliary space?
Ans:
- Input space is *fixed* by the problem — not the algorithm.
- Auxiliary space shows the algorithm’s own efficiency and optimization.
'''
# Example:
# Two sorting algorithms on same input:
# → Bubble Sort: O(1) auxiliary space
# → Merge Sort: O(n) auxiliary space
# → Both use same input space, but different auxiliary needs.



'''
Q4. How can space complexity be reduced?
Ans:
✅ Reuse variables instead of creating new ones.  
✅ Prefer in-place algorithms.  
✅ Use generators/yield instead of lists for large data.  
✅ Avoid deep recursion when possible.
'''
# Example of space-efficient design
def square_in_place(arr):
    for i in range(len(arr)):
        arr[i] *= arr[i]
    return arr
# No extra list → O(1) auxiliary space



'''
Q5. Quick shorthand
✔ Space = Input + Auxiliary  
✔ Input → fixed by problem  
✔ Auxiliary → depends on algorithm  
✔ Recursive depth = hidden space cost  
✔ In-place = best space optimization
'''
