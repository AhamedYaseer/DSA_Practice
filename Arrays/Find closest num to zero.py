Problem:
Find Closest Number to Zero

Approach:
Linear Scan

Why this works:
Iterates through the array and keeps track of the number with the smallest
absolute value. In case of a tie, the larger number is chosen.

Time Complexity:
O(n)

Space Complexity:
O(1)

# ------------
# Linear scan
# ------------

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest=nums[0]
        for i in range(len(nums)):
            if abs(nums[i])<abs(closest):
                closest=nums[i]
            elif abs(nums[i])==abs(closest):
                closest=max(nums[i],closest)
        return closest
