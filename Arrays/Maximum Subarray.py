# Maximum Subarray

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
