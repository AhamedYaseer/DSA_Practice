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

Problem:
Palindrome Number

Approach:
Math (Reverse Half)

Why this works:
The last half of the number is reversed and compared with the remaining first half.
For odd-length numbers, the middle digit is ignored. (i.e, 12321 12==12)

Time Complexity:
O(n)

Space Complexity:
O(1)

# ----------------------------------
# Mathematical reverse (only 2nd half)
# ----------------------------------


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x==0:
            return True
        if x%10==0 and x!=0:
            return False

        rev=0
        while rev<x: #in the final iteration, rev will be greater than x
            rev=rev*10+x%10
            x=x//10
        
        if rev==x or rev//10==x: #for 1st condition for even digit (1221: 12 12), 2nd for odd digit (12321: 12 12)
            return True
        return False
