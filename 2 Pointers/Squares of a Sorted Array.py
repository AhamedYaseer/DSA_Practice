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


Approach:
Two Pointers

Why this works:
The input array is already sorted, but after squaring the elements,
the order may change because negative numbers can have larger absolute
values.

The largest square must come from either the leftmost element or the
rightmost element.

We use two pointers:
- l starts at the beginning of the array.
- r starts at the end of the array.
- Compare the squares of nums[l] and nums[r].
- Place the larger square at the end of the output array.
- Move the pointer whose element was used.
- Continue until the two pointers meet.

We fill the output array from right to left because we always select
the largest remaining square.

Time Complexity:
O(n)
Each element is processed exactly once.

Space Complexity:
O(n)
The output array contains n elements.

# ----------------------------------
# Two Pointers
# ----------------------------------

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        i = -1
        output = [0] * len(nums)

        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                output[i] = nums[l] * nums[l]
                l += 1
            else:
                output[i] = nums[r] * nums[r]
                r -= 1

            i -= 1

        return output
