Problem:
Valid Palindrome (https://leetcode.com/problems/valid-palindrome/description/)

Approach:
String Normalization + Two Pointers

Why this works:
We first normalize the string by:
- Converting uppercase characters to lowercase.
- Removing all non-alphanumeric characters.

After normalization, we use two pointers:
- l starts from the beginning.
- r starts from the end.

We compare the characters at both pointers and move them toward
the center.

If any pair of characters is different, the string is not a
palindrome.

If all pairs match, the string is a palindrome.

Time Complexity:
O(n)
The string is traversed while creating the normalized string and
again during the two-pointer comparison.

Space Complexity:
O(n)
A new normalized string is created.

# ----------------------------------
# String Normalization + Two Pointers
# ----------------------------------

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(c.lower() for c in s if c.isalnum())

        l = 0
        r = len(s) - 1

        while l < r:

            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True
