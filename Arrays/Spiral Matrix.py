Problem:
Spiral Matrix (https://leetcode.com/problems/spiral-matrix/description/)

Approach:
Boundary Traversal

Why this works:
We maintain four boundaries to represent the unvisited portion
of the matrix:

- top    → topmost unvisited row
- bottom → bottommost unvisited row
- left   → leftmost unvisited column
- right  → rightmost unvisited column

For each layer, we traverse the matrix in four directions:

1. Left → Right across the top row
2. Top → Bottom down the right column
3. Right → Left across the bottom row
4. Bottom → Top up the left column

After traversing each side, the corresponding boundary is moved
inward.

The third traversal is performed only if a row still exists
(top <= bottom), and the fourth traversal is performed only if
a column still exists (left <= right). These checks prevent
elements from being visited more than once when only a single
row or column remains.

Time Complexity:
O(m × n)
Every element in the matrix is visited exactly once.

Space Complexity:
O(m × n)
The output list stores all elements.

Auxiliary Space:
O(1)
Only boundary variables and loop variables are used apart from
the output list.

# ----------------------------------
# Boundary Traversal
# ----------------------------------

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        output = []

        while top <= bottom and left <= right:

            # Left → Right
            for i in range(left, right + 1):
                output.append(matrix[top][i])
            top += 1

            # Top → Bottom
            for i in range(top, bottom + 1):
                output.append(matrix[i][right])
            right -= 1

            # Right → Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    output.append(matrix[bottom][i])
                bottom -= 1

            # Bottom → Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    output.append(matrix[i][left])
                left += 1

        return output
