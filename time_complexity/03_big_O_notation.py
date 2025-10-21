'''
Q1. What does Big-O notation represent?
Ans:
- It represents the **upper bound** on the runtime growth rate of an algorithm.
- It shows how runtime increases with input size n — ignoring constants and small terms.
'''
# Example:
# If an algorithm takes 3n + 4 steps → O(n)
# → We care only about the growth trend (linear), not the exact step count.



'''
Q2. Why does Big-O ignore constants?
Ans:
- Constants don't affect how fast runtime *scales* with n.
- As n grows large, the proportional factor (growth shape) matters more than exact numbers.
# '''
# Example:
# 2n and 100n → both O(n)
# For large n, 100n is slower, but both scale linearly.



'''
Q3. What are common time complexities (from best to worst)?
Ans:
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
'''



'''
Q4. What does “upper bound” mean in Big-O?
Ans:
- It’s the **worst-case scenario** — the maximum growth rate the algorithm can have.
- Guarantees that runtime will not grow faster than the given rate.
'''
# Example:
# Linear search → O(n) because in the worst case, you check every element.



'''
Q5. How does Big-O help in real-world programming?
Ans:
- Lets you compare algorithms without running them.
- Helps predict scalability and performance bottlenecks.
- Guides design decisions early in development.
'''
# Example:
# For sorting 1 million items,
# → O(n log n) (like merge sort) is feasible,
# → O(n²) (like bubble sort) is too slow.



'''
Q6. Quick shorthand
✔ Big-O → upper bound on runtime growth  
✔ Ignores constants and small terms  
✔ Describes scalability, not actual time  
✔ Compare algorithms by growth trend  
✔ Worst-case, not average performance
'''
