Problem:
Longest Consecutive Sequence (https://leetcode.com/problems/longest-consecutive-sequence/description/)

Approach:
Sorting + Hash Map

Why this works:
We first sort the array so that consecutive values appear next to
each other.

A dictionary is then created from nums to remove duplicate values, (if set instead of dictionary, sorted order will get lost)
since duplicate numbers should not increase the consecutive sequence 
and to make membership operation in O(1)

We traverse the unique values:
- If the next number exists in the dictionary, the current consecutive
  sequence is extended.
- Otherwise, the current sequence ends and its length is stored.

Finally, we find and return the maximum consecutive sequence length.

Time Complexity:
O(n log n)
Sorting takes O(n log n), while creating the dictionary and traversing
the unique elements take O(n) on average.

Space Complexity:
O(n)
The dictionary and consec list require O(n) additional space.

# ----------------------------------
# Sorting + Hash Map
# ----------------------------------

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        cons = 1
        consec = []

        nums.sort()

        dict_nums = {x: 0 for x in nums} #dictionary with all values as 0

        for i in dict_nums:
            if i + 1 in dict_nums:
                cons += 1
            else:
                consec.append(cons)
                cons = 1

        max_val = 1

        for i in consec:
            if i > max_val:
                max_val = i

        return max_val
