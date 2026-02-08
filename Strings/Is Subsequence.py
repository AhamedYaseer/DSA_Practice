Problem:
Is Subsequence (https://leetcode.com/problems/is-subsequence/description/)

Approach:
Simulation using Search and Slicing

Why this works:
For each character in s, we check whether it appears in t.
If found, we move t forward to the position after the matched character,
ensuring the subsequence order is preserved.  
If any character is missing, the result is False.

Time Complexity:
O(m × n)
For each character in s, searching and slicing in t takes linear time.

Space Complexity:
O(n)
Slicing creates new substrings during processing.


# ----------------------------------
# Simulation using search and slicing
# ----------------------------------

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            if i in t:
                index = t.index(i)
                t = t[index + 1:]
            else:
                return False
        return True
