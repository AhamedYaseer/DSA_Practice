Problem:
Squares of a Sorted Array (https://leetcode.com/problems/squares-of-a-sorted-array/description/)

Approach:
Squaring + Sorting

Why this works:
Since the input array is sorted, we first square every element.

However, squaring can change the order because negative numbers
with larger absolute values produce larger squares.

Therefore, after squaring all elements, we sort the resulting array
to obtain the squares in non-decreasing order.

Time Complexity:
O(n log n)
Squaring all elements takes O(n), and sorting takes O(n log n).

Space Complexity:
O(n)
The sorted() function creates a new list for the result.

# ----------------------------------
# Squaring + Sorting
# ----------------------------------

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        return sorted(nums)
