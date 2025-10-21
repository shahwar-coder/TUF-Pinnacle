'''
Q1. What do Big-O, Big-Ω, and Big-Θ actually represent?
Ans:
- They describe **bounds on algorithm growth**, not input cases.
  - **O(f(n))** → Upper bound (worst it can grow)
  - **Ω(f(n))** → Lower bound (best it can grow)
  - **Θ(f(n))** → Tight bound (grows roughly at that rate)
'''
# Example:
# If T(n) = 3n² + 5n + 2,
# → O(n²)  (upper bound)
# → Ω(n²)  (lower bound)
# → Θ(n²)  (tight bound)



'''
Q2. What does it mean if an algorithm is Θ(f(n))?
Ans:
- It means f(n) is both an **upper and lower bound**.
- So the runtime grows asymptotically *at the rate of f(n)*.
'''
# Example:
# If T(n) = 2n + 3,
# then T(n) = Θ(n) because:
# → grows no faster than n (O(n))
# → and no slower than n (Ω(n))



'''
Q3. Why is Θ preferred when analyzing average behavior?
Ans:
- Because Θ expresses **tight bounds**, not just limits.
- It shows how the algorithm behaves *most of the time*, not just extremes.
'''



'''
Q4. Can an algorithm have O(n²) and also Θ(n)?
Ans:
✅ Yes, if its upper bound is O(n²) but actual runtime grows linearly.  
But ❌ if we mean “tight bound” — O(n²) is correct but loose; Θ(n) is the precise one.
'''
# Example: Counting elements in a list
# Actual runtime grows linearly → Θ(n)
# But saying O(n²) is technically true (looser upper bound)



'''
Q5. Quick shorthand
✔ O = at most this fast  
✔ Ω = at least this fast  
✔ Θ = grows about this fast  
✔ They’re bounds, not input cases  
✔ Best/avg/worst are situations, not symbols
'''
