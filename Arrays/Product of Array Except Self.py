"""
Problem:
Product of Array Except Self (https://leetcode.com/problems/product-of-array-except-self/description/)

Approach:
Prefix and Suffix Products

Why this works:
For each index, we need the product of all elements to its left
and all elements to its right. then multiplying both left[i] & right[i] to get output[i]

We create two arrays:
- L_prod stores the product of all elements to the left of each index.
- R_prod stores the product of all elements to the right of each index.

For each index, multiplying L_prod[i] and R_prod[i] gives the
product of every element except nums[i].

Time Complexity:
O(n)
We traverse the array a constant number of times.

Space Complexity:
O(n)
We use separate left-product, right-product, and output arrays.

# ----------------------------------
# Prefix and Suffix Products
# ----------------------------------
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        L_prod = [0] * len(nums)
        R_prod = [0] * len(nums)

        L_prod[0], R_prod[-1] = 0, 0
        L_prod[1], R_prod[-2] = nums[0], nums[-1]

        if len(nums) > 2:
            for i in range(2, len(nums)):
                L_prod[i] = L_prod[i - 1] * nums[i - 1]

            for j in range(-3, -(len(nums) + 1), -1):
                R_prod[j] = R_prod[j + 1] * nums[j + 1]

        output[0], output[-1] = R_prod[0], L_prod[-1]

        for i in range(1, len(nums) - 1):
            output[i] = L_prod[i] * R_prod[i]

        return output
