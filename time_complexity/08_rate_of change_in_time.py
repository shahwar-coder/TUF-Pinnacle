'''
Q1. What does “rate of change in time” tell us?
Ans:
- It measures **how runtime increases** as input size grows.
- Formula → (input₂ − input₁) / (time₂ − time₁)
- Helps visualize *scalability*: how much slower an algorithm gets as input doubles.
'''
# Example:
# n₁=1000 → 0.01s, n₂=2000 → 0.02s  
# Rate = (2000−1000)/(0.02−0.01) = 100,000 ops/s → linear growth (O(n))



'''
Q2. How does Big O relate to rate of change?
Ans:
- Big O abstracts this *growth rate* mathematically.  
- It ignores machine details and focuses on how time increases with input size.
'''
# Example:
for i in range(n): pass   # O(n)
# Double n → roughly doubles time.
for i in range(n):
    for j in range(n): pass   # O(n²)
# Double n → roughly quadruples time.



'''
Q3. Why do constant loops have O(1) complexity?
Ans:
- Their runtime doesn’t depend on input size.
- Rate of change ≈ 0 → flat line (no growth).
'''
for i in range(5): pass  # Always 5 steps → O(1)



'''
Q4. How does doubling input help identify growth type?
Ans:
- O(n): doubling → ~2× slower  
- O(n²): doubling → ~4× slower  
- O(log n): doubling → +1 step (very small change)
'''



'''
Q5. Why does Big O describe scalability, not raw speed?
Ans:
- Two O(n) algorithms can differ in absolute time due to constants,
  but they’ll *scale similarly* as n grows.
'''
# Example:
sum(range(n))   # O(n), optimized in C → fast
manual_sum = 0
for i in range(n): manual_sum += i   # O(n), slower Python loop



'''
Q6. Quick shorthand
✔ Rate of change shows growth experimentally  
✔ Big O models growth theoretically  
✔ Constant loops → O(1)  
✔ Linear → double input = double time  
✔ Quadratic → double input = quadruple time
'''

