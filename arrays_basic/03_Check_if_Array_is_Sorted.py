'''
Check if Array is Sorted.
'''
# SLIGHTLY BETTER SOLUTION
class Solution:
    def arraySortedOrNot(self, arr, n):
        return all(arr[i]<=arr[i+1] for i in range(n-1)) 


# '''
# Advantages of the all() + generator approach

# • No unnecessary work → only checks adjacent pairs, doesn’t sort or copy.
# • Short-circuits early → stops at first unsorted pair, saving time.
# • No temporary structures → generator expression avoids extra list creation.
# • Memory-efficient → constant O(1) additional space.
# • Idiomatic Python → cleanest, most readable way to check a universal condition.
# '''



# ORIGINAL GOOD SOLUTION
# class Solution:
#     def arraySortedOrNot(self, arr, n):
#         arr_copy=arr.copy()
#         if sorted(arr) == arr_copy:
#             return True
#         else:
#             return False


# COPY OF ARRAY NOT RQUIRED (as not manipulated)
# class Solution:
#     def arraySortedOrNot(self, arr, n):
#         if sorted(arr) == arr:
#             return True
#         else:
#             return False

# sorted(arr) does NOT mutate arr — it returns a new sorted list.
