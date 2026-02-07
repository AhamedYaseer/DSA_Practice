Problem:

Remove Element (https://leetcode.com/problems/remove-element/description/)

Approach:

Filtering / (not brute force)

Why this works:

Iterates through the array once and keeps only elements that are not equal to the given value.
The filtered result is then written back to the original array.

Time Complexity:

O(n)

Space Complexity:

O(n)  (a temporary array is created during filtering, then copied back)

# --------------------
# Filtering method
# --------------------

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:]=[i for i in nums if i!=val]
        return len(nums)
        
Approach:
Two pointer (In place)

Why this works:

Maintains two pointers, one for reading (iterates throughout the list) and another for writing (maintains final output)
writing pointer moves only when a number ❌=val appears

Time Complexity:

O(n)

Space Complexity:

O(1) 

# --------------------
# two pointer method
# --------------------


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write=0
        read=0
        n=len(nums)
        while read<n:
            if nums[read]!=val:
                nums[write]=nums[read]
                write=write+1
            read=read+1
        #del nums[write:] here 2,2,_,_, underscore parts are not important
                        #.use above line if nums should contain only valid nos.
        return write

