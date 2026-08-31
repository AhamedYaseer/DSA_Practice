"""
Problem:
3Sum (https://leetcode.com/problems/3sum/description/)

Approach:
Sorting + Two Pointers

Why this works:
We first sort the array. Sorting allows us to use the two-pointer
technique and also makes it possible to skip duplicate values.

For each element nums[i], we treat it as the first element of the
triplet and use two pointers:
- l starts immediately after i.
- r starts at the end of the array.

We need:
    nums[i] + nums[l] + nums[r] = 0

If the sum is smaller than 0, we move l to the right to increase
the sum.

If the sum is greater than 0, we move r to the left to decrease
the sum.

When the sum is 0, we add the triplet and move both pointers inward.

Duplicate values are skipped:
- Duplicate nums[i] values are skipped before starting the two-pointer
  search.
- After finding a valid triplet, duplicate values at l and r are
  skipped to avoid duplicate triplets.

Time Complexity:
O(n^2)
Sorting takes O(n log n), followed by an O(n^2) two-pointer traversal.

Space Complexity:
O(1) auxiliary space, excluding the output.
The array is sorted in place and only a constant number of pointers
and variables are used.

The output itself can require O(n^2) space in the worst case.

# ----------------------------------
# Sorting + Two Pointers
# ----------------------------------
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        output = []

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l != len(nums) and nums[l] == nums[l - 1]:
                        l += 1

                    while r >= 0 and nums[r] == nums[r + 1]:
                        r -= 1

                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    r -= 1

        return output
