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


Approach:
Two Pointers / Left and Right Maximums

Why this works:
The amount of water trapped at a position depends on the smaller
of the maximum heights on its left and right.

Instead of storing the left and right maximum for every position,
we use two pointers and maintain only:
- max_left → maximum height encountered from the left.
- max_right → maximum height encountered from the right.

We start with l at the beginning and r at the end of the array.

At each step, we update max_left and max_right.

If max_left is less than or equal to max_right, the left side is
the limiting side. Therefore, we can calculate the water at l using
max_left and move l to the right.

Otherwise, the right side is the limiting side. We calculate the
water at r using max_right and move r to the left.

This allows us to calculate the trapped water without storing
separate left and right maximum arrays.

Time Complexity:
O(n)
Both pointers move toward each other, so each position is processed
at most once.

Space Complexity:
O(1)
Only two pointers, two maximum values, and a few variables are used.

# ----------------------------------
# Two Pointers / Left and Right Maximums
# ----------------------------------

class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0

        l = 0
        r = len(height) - 1

        max_left = 0
        max_right = 0

        while l < r:

            if height[l] > max_left:
                max_left = height[l]

            if height[r] > max_right:
                max_right = height[r]

            if max_left <= max_right:
                output = output + max_left - height[l] \
                    if max_left - height[l] > 0 else output
                l += 1

            else:
                output = output + max_right - height[r] \
                    if max_right - height[r] > 0 else output
                r -= 1

        return output
