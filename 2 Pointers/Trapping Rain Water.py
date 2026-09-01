Problem:
Trapping Rain Water (https://leetcode.com/problems/trapping-rain-water/description/)

Approach:
Prefix and Suffix Maximums

Why this works:
For every position, the amount of water that can be trapped
depends on the highest bar to its left and the highest bar to its
right.

The water trapped at index i is:

    min(max_left[i], max_right[i]) - height[i]

We first traverse the array from left to right and store the maximum
height encountered from the left for every index.

Then, we traverse from right to left and store the maximum height
encountered from the right for every index.

For each position, we take the smaller of the left and right maximum
heights and subtract the current height.

If the result is positive, that amount of water can be trapped at
that position.

Time Complexity:
O(n)
We traverse the array a constant number of times.

Space Complexity:
O(n)
The max_dict stores the left and right maximum heights for every
index.

# ----------------------------------
# Prefix and Suffix Maximums
# ----------------------------------

class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0

        max_dict = {0: [0]}
        max_ele = height[0]
        prev = height[0]

        # Maximum height to the left
        for i in range(1, len(height)):
            max_ele = max(max_ele, prev)
            max_dict[i] = [max_ele]
            prev = height[i]

        max_dict[len(height) - 1].append(0)

        max_ele = height[-1]
        prev = height[-1]

        # Maximum height to the right
        for j in range(len(height) - 1, -1, -1):
            max_ele = max(max_ele, prev)
            max_dict[j].append(max_ele)
            prev = height[j]

        # Calculate trapped water
        for i in max_dict:
            val = min(max_dict[i][0], max_dict[i][1]) - height[i]

            if val > 0:
                output += val

        return output
