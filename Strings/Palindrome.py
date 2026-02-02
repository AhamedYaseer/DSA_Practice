Problem:
Palindrome Number

Approach:
String Conversion and Reversal 

Why this works:
The number is converted to a string and reversed.
If the reversed string matches the original, the number is a palindrome.

Time Complexity:
O(n)

Space Complexity:
O(n)

# ----------------------------------
# String Conversion and reversal
# ----------------------------------

class Solution:
    def isPalindrome(self, x: int) -> bool:
        r=str(x)
        r=r[::-1]
        if r==str(x):
            return True
        else:
            return False

