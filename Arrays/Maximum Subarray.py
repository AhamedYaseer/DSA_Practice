Problem:
Maximum Subarray (https://leetcode.com/problems/maximum-subarray/description/)

Approach:
Brute Force / Subarray Sum

Why this works:
We consider every possible starting position of a subarray.

For each starting index `i`, we initialize `sub_sum` with the value
at that index. Then, we extend the subarray one element at a time
using the inner loop.

At each step:
- Add the current element to `sub_sum`.
- Compare the current subarray sum with `maxi`.
- Update `maxi` if the current sum is larger.

This ensures that every possible contiguous subarray is considered,
and the largest sum among them is returned.

Time Complexity:
O(n²)
For each starting index, we may traverse the remaining elements.

Space Complexity:
O(1)
Only a few variables are used regardless of the input size.

# ----------------------------------
# Brute Force / Subarray Sum
# ----------------------------------

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        maxi=nums[0]

        for i in range(len(nums)):

            sub_sum=nums[i]

            maxi=max(maxi,sub_sum)

            for j in range(i+1,len(nums)):

                sub_sum+=nums[j]

                maxi=max(maxi,sub_sum)

        return maxi
