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


Approach:
Two Pointers / In-Place Character Checking

Why this works:
We use two pointers, one starting from the beginning of the string
and the other from the end.

Non-alphanumeric characters are ignored by moving the corresponding
pointer and continuing the loop.

For valid characters, we compare them after converting both to
lowercase.

If the characters are different, the string is not a palindrome.

If all valid characters match while the pointers move toward the
center, the string is a palindrome.

The continue statements ensure that when a non-alphanumeric
character is encountered, only that pointer moves and the character
is not compared with the character at the opposite pointer.

Unlike the initial approach, we do not create a separate cleaned
string.

Time Complexity:
O(n)
Each character is processed at most a constant number of times.

Space Complexity:
O(1)
Only two pointers are used as auxiliary space.

# ----------------------------------
# Two Pointers / In-Place Character Checking
# ----------------------------------

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:

            if not s[l].isalnum():
                l += 1
                continue

            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
