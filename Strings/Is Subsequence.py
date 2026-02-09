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


Approach:
Two Pointers

Why this works:
We move through string t one time and try to match the characters of s in the same order.
Whenever the current characters of s and t match, we move both pointers forward.
If they do not match, we move only the pointer of t to keep searching.

At the end, if we have matched all characters of s, then s is a subsequence of t.

Time Complexity:
O(n)
Single pass through t.

Space Complexity:
O(1)
Only pointer variables are used.

# ----------------------------------
# Two-pointer optimal solution
# ----------------------------------

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pt = 0
        t_pt = 0

        if len(s) > len(t):
            return False

        while t_pt < len(t) and s_pt < len(s): #exit atleast anyone of
            if s[s_pt] == t[t_pt]:   #if character match, move both pointer
                s_pt += 1
                t_pt += 1
            else:                    #else, only t pointer
                t_pt += 1

        if s_pt == len(s): #if s is traversed fully, then it is a substring
            return True
        return False

