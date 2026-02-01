Problem:

Remove Element

Approach:

Filtering / (not brute force)

Why this works:

Iterates through the array once and keeps only elements that are not equal to the given value.
The filtered result is then written back to the original array.

Time Complexity:

O(n)

Space Complexity:

O(n)  (a temporary array is created during filtering, then copied back)

# --------------------
# Filtering method
# --------------------

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:]=[i for i in nums if i!=val]
        return len(nums)
