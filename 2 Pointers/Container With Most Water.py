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

Approach:
Two Pointers

Why this works:
The area between two lines is determined by:

    min(height[l], height[r]) * (r - l)

We start with the two pointers at the opposite ends of the array,
giving the maximum possible width.

At each step, we calculate the current area and update the maximum
area found.

The shorter line limits the height of the container. Since moving
either pointer inward always decreases the width, moving the taller
line cannot improve the area while the shorter line remains the
limiting factor.

Therefore:
- If height[l] < height[r], move l to the right.
- Otherwise, move r to the left.

We continue until the two pointers meet.

This eliminates the need to check every possible pair of lines.

Time Complexity:
O(n)
Both pointers move toward each other, and each position is processed
at most once.

Space Complexity:
O(1)
Only a constant amount of extra space is used.

# ----------------------------------
# Two Pointers
# ----------------------------------

class Solution:
    def maxArea(self, height: List[int]) -> int:

        area = 0
        c_area = 0
        l = 0
        r = len(height) - 1

        while l < r:
            c_area = min(height[l], height[r]) * (r - l)
            area = max(area, c_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return area
