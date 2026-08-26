Problem:
Two Sum II - Input Array Is Sorted (https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

Approach:
Two Pointers

Why this works:
The input array is sorted in non-decreasing order, so we can use
two pointers starting from both ends of the array.

If the sum of the two elements is greater than the target, we move
the right pointer to the left to reduce the sum.

If the sum is smaller than the target, we move the left pointer to
the right to increase the sum.

If the sum equals the target, we return the 1-indexed positions of
the two elements.

Time Complexity:
O(n)
Each pointer moves toward the other pointer at most n times.

Space Complexity:
O(1)
Only two pointers are used.

# ----------------------------------
# Two Pointers
# ----------------------------------

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        while l < r:

            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]

            elif numbers[l] + numbers[r] > target:
                r -= 1

            else:
                l += 1
