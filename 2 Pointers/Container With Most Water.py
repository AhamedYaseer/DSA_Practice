Problem:
Container With Most Water (https://leetcode.com/problems/container-with-most-water/description/)

Approach:
Brute Force / Pairwise Comparison

Why this works:
We consider every possible pair of vertical lines.

For each pair of indices i and j:
- The width is j - i.
- The effective height is the smaller of height[i] and height[j].
- The area is calculated as:

    min(height[i], height[j]) * (j - i)

We keep track of the maximum area found among all possible pairs.

Time Complexity:
O(n²)
We check every possible pair of lines.

Space Complexity:
O(1)
Only a constant number of variables are used.

# ----------------------------------
# Brute Force / Pairwise Comparison
# ----------------------------------

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0

        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                c_area = min(height[i], height[j]) * (j - i)
                area = max(area, c_area)

        return area
