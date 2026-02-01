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

Approach:
Hash Map

Why this works:
We are finding a required value (by target - current value)
If required value is in visited list, return its index
Else, add current value to visited list

Time Complexity:
O(n)

Space Complexity:
O(n)


# --------------------
# Optimized Solution
# --------------------

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        visited={}
        for i in range(n):
            required_val=target-nums[i]
            if required_val in visited:
                return [visited[required_val],i]
            visited[nums[i]]=i
