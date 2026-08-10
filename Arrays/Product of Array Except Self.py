Problem:
Product of Array Except Self (https://leetcode.com/problems/product-of-array-except-self/description/)

Approach 1:
Brute Force (Using Total Product and Zero Handling)

Why this works:
First, we calculate the product of all elements.

For non-zero elements, we divide the total product by the current
element to get the product of all other elements.

If the current element is zero, division cannot be used. So we
calculate the product of all other elements separately using another
loop.

Time Complexity:
O(n²)
The total product takes O(n) time. In the worst case, the zero
handling requires another O(n) loop for each zero.

Space Complexity:
O(1)
(Excluding the output list)

# ----------------------------------
# Brute Force    (just for reference, but problem clearly states to do it without division operation)
# ----------------------------------

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        zero_case_prod = 1

        for i in nums:
            total_prod *= i

        output = []

        for i in range(len(nums)):
            if nums[i] != 0:
                output.append(total_prod // nums[i])
            else:
                for j in range(len(nums)):
                    if j != i:
                        zero_case_prod *= nums[j]

                output.append(zero_case_prod)
                zero_case_prod = 1

        return output


Approach 2:
Prefix and Suffix Products

Why this works:
For each index, we need the product of all elements to its left
and all elements to its right. Multiplying both products gives the
product of every element except the current element.

We create two arrays:
- L_prod stores the product of all elements to the left of each index.
- R_prod stores the product of all elements to the right of each index.

For each index, multiplying L_prod[i] and R_prod[i] gives the
required output for that index.

Time Complexity:
O(n)
We traverse the array a constant number of times.

Space Complexity:
O(n)
We use separate left-product, right-product, and output arrays.

# ----------------------------------
# Prefix and Suffix Products
# ----------------------------------

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        L_prod = [0] * len(nums)
        R_prod = [0] * len(nums)

        L_prod[0], R_prod[-1] = 0, 0    #as no left element & right element for left & right product respectively

        if len(nums) >=2:
            L_prod[1], R_prod[-2] = nums[0], nums[-1] 
            for i in range(2, len(nums)):
                L_prod[i] = L_prod[i - 1] * nums[i - 1]

            for j in range(-3, -(len(nums) + 1), -1):
                R_prod[j] = R_prod[j + 1] * nums[j + 1]

        output[0], output[-1] = R_prod[0], L_prod[-1]  #since for 0,nth position -> atleast one of L_prod or R_prod is zero, handling it

        for i in range(1, len(nums) - 1):
            output[i] = L_prod[i] * R_prod[i]

        return output
