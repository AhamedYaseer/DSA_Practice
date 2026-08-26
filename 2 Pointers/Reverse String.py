Problem:
Reverse String (https://leetcode.com/problems/reverse-string/description/)

Approach:
Two Pointers / In-Place Reversal

Why this works:
We use two pointers, one starting from the beginning of the list
and the other from the end.

At each step, we swap the elements at the two pointers and move
both pointers toward the center.

The process continues until the pointers meet or cross.

The list is modified in place as required by the problem.

Time Complexity:
O(n)
Each element is processed at most once.

Space Complexity:
O(1)
Only constant extra space is used for the pointers and temporary
variable.

# ----------------------------------
# Two Pointers / In-Place Reversal
# ----------------------------------

class Solution:
    def reverseString(self, s: List[str]) -> None:

        l = 0
        r = len(s) - 1

        while l < r:
            temp = s[r]
            s[r] = s[l]
            s[l] = temp

            l += 1
            r -= 1
