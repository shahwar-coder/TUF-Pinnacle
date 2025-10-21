'''
Q1. What is the difference between “time complexity” and “time taken”?
Ans:
- **Time complexity** → theoretical measure of *growth rate* of runtime as input size increases.  
- **Time taken** → actual runtime on a specific machine.
'''
# Example:
# Two O(n) algorithms may differ:
# A: runs 5n + 3 operations  
# B: runs 50n + 10 operations  
# → Both O(n), but A is faster in real life.



'''
Q2. Why can two O(n) algorithms have different execution speeds?
Ans:
- Big O hides constants and lower-order terms.
- Actual runtime depends on:
  1️⃣ Implementation efficiency  
  2️⃣ Hardware (CPU speed, cache)  
  3️⃣ Language and compiler optimizations
'''
# Both are O(n), but one has a smaller constant factor
sum_1 = sum(range(10**6))          # Built-in → optimized C code
sum_2 = 0
for i in range(10**6): sum_2 += i  # Slower pure Python



'''
Q3. What does time complexity actually tell us?
Ans:
- It predicts **how runtime scales** with input size (n → ∞).
- Used to compare **algorithm scalability**, not exact duration.
'''
# O(n) → doubles input → roughly doubles work.
# O(n²) → doubles input → ~quadruples work.




'''
Q4. Why is measuring real “time taken” still important?
Ans:
- Because theoretical scaling doesn’t account for constants or hardware.
- Benchmarks tell us which algorithm is faster *in practice* for realistic input sizes.
'''
# Example:
# QuickSort (O(n log n)) may outperform MergeSort (O(n log n))
# due to better cache locality or fewer swaps in real systems.



'''
Q5. What’s the correct way to evaluate an algorithm?
Ans:
✅ Use **time complexity** for scalability comparison.  
✅ Use **time taken** (profiling/benchmarking) for real-world performance.
✅ Combine both for well-rounded evaluation.
'''
import time
def test_runtime():
    start = time.time()
    sum(range(10**6))
    end = time.time()
    print("Time Taken:", end - start)



'''
Q6. Quick shorthand
✔ Complexity = theoretical growth  
✔ Time taken = real measured speed  
✔ Same O(n) ≠ same performance  
✔ Measure both to get full picture  
✔ Constants matter for small inputs
'''
