Problem:
Maximum Subarray (https://leetcode.com/problems/maximum-subarray/description/)

Approach:
Kadane's Algorithm / Running Subarray Sum

Why this works:
At each position, we decide whether to extend the current subarray
or start a new subarray from the current element.

We maintain two values:
- `current_sub` → maximum subarray sum ending at the current position.
- `max_sub` → maximum subarray sum found so far.

If `current_sub` is positive, adding the next element can help the
subarray, so we extend it.

If `current_sub` is zero or negative, keeping it would not improve
any future subarray. Therefore, we discard it and start a new
subarray from the current element.

At every step, we update `max_sub` with the best sum found so far.

This avoids checking every possible subarray and reduces the time
complexity from O(n²) to O(n).

Time Complexity:
O(n)
The array is traversed only once.

Space Complexity:
O(1)
Only `max_sub`, `current_sub`, and a few variables are used.

# ----------------------------------
# Kadane's Algorithm / Running Subarray Sum
# ----------------------------------

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        max_sub=nums[0]

        current_sub=nums[0]

        for i in range(1,len(nums)):

            if current_sub>0:

                current_sub+=nums[i]

                max_sub=max(max_sub,current_sub)

            else:

                current_sub=nums[i]

                max_sub=max(max_sub,current_sub)

        return max_sub
