Problem:
Two Sum

Approach:
Brute force (to be optimized)

Why this works:
Checks all pairs

Time Complexity:
O(n^2)

Space Complexity:
O(1)

# --------------------
# Brute Force Solution
# --------------------

def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(0,n):
            for j in range(1,n):
                if i!=j:
                    sum=nums[i]+nums[j]
                    if sum==target:
                        return [i,j]



