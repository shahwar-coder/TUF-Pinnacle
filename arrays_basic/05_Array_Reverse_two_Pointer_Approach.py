'''
Array Reverse Two Pointer approach.
'''

class Solution:
    def reverse(self, arr: list, n: int) -> None:
        """Reverse the array in place using two pointers."""
        left, right = 0, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


'''
⚙️ Two-Pointer Method vs arr.reverse()

1️⃣ arr.reverse()
   • Built-in C-optimized method.
   • Reverses the list **in place**.
   • Runs in O(n) time, O(1) space.
   • ✅ Fastest and most memory-efficient in almost all cases.
   • Highly recommended unless you’re writing your own reverse logic (e.g., interview or learning).

2️⃣ Two-Pointer Method
   • Also reverses **in place**.
   • O(n) time, O(1) space — same theoretical complexity.
   • Implemented in Python bytecode (slower than C’s built-in).
   • ✅ Useful for understanding or applying two-pointer logic to custom problems.

💡 Summary:
| Method             | In-place | Time  | Space | Speed | Use Case |
|--------------------|----------|-------|--------|--------|-----------|
| arr.reverse()      | ✅ Yes   | O(n)  | O(1)  | ⚡ Fast | Real-world code |
| Two-pointer loop   | ✅ Yes   | O(n)  | O(1)  | 🐢 Slower | Learning / logic building |

✅ Verdict:
Use `arr.reverse()` in production.
Use the **two-pointer method** to understand and apply the logic manually in algorithmic contexts.
'''
