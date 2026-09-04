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


# ----------------------------------
# Kadane's Algorithm / Running Subarray Sum
# ----------------------------------

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
