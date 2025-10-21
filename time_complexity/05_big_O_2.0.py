'''
Q1. Why are constants ignored in Big-O notation?
Ans:
- Big-O measures growth *as n → ∞*.  
- Constants only scale the runtime, not its growth rate.  
- O(2n + 5) → O(n), because doubling or adding a fixed cost doesn’t change the growth class.
# '''
# Example:
# Algorithm A → 2n + 3 operations
# Algorithm B → 100n + 7 operations
# → Both are O(n), though B is slower in real time.



'''
Q2. What are the different cases in time complexity analysis?
Ans:
- **Best Case** → Fastest possible input scenario.  
- **Average Case** → Expected runtime for random inputs.  
- **Worst Case** → Maximum possible runtime for any input.
'''
# Example: Linear Search in a list of size n
# - Best: Item found at index 0 → O(1)
# - Average: Item found near middle → O(n)
# - Worst: Item not found → O(n)



'''
Q3. Why do we mainly focus on the worst-case complexity?
Ans:
- It provides a **guaranteed upper bound** on runtime.
- Prevents unexpected delays or catastrophic performance in rare cases.
- Independent of input distribution → safer in critical systems.
'''
# Example:
# QuickSort → average O(n log n), but worst-case O(n²)
# → That’s why introsort (used in Python’s sort) switches strategy to avoid the worst case.



'''
Q4. How does the average case differ conceptually from the worst case?
Ans:
- Average case uses **probability** — it depends on how likely inputs are.
- Worst case assumes the **most difficult** input every time.
'''



'''
Q5. Can constants affect real runtime even if they don’t affect Big-O?
Ans:
✅ Yes — constants matter for **small input sizes** or real-world execution.  
🚫 No — they don’t affect the **asymptotic class** as n grows.
'''
# O(n) both, but constant factor differs
for _ in range(10*n): pass  # slower constant
for _ in range(n): pass      # faster constant



'''
Q6. Quick shorthand
✔ Drop constants → focus on growth rate  
✔ Analyze 3 cases → best, average, worst  
✔ Worst case = guaranteed bound  
✔ Average = expected behavior  
✔ Constants matter in practice, not theory
'''
