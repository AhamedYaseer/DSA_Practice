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


Approach:
Hash Set / Sequence Start Detection

Why this works:
We first convert nums into a set to allow O(1) average-time
membership checks and automatically remove duplicates.

For each number, we only start counting a consecutive sequence if
its previous number (i - 1) is not present in the set.

This means the current number is the beginning of a sequence.

Once a starting number is found, we keep checking for the next
consecutive numbers (i + 1, i + 2, ...) and count the sequence length.

We do not start another sequence from numbers that already have a
predecessor, which prevents repeatedly traversing the same sequence.

The maximum sequence length is maintained using max_cons.

Time Complexity:
O(n)
Creating the set takes O(n), and each number is processed a constant
number of times overall. Although there is a while loop inside the
for loop, the consecutive sequence is only traversed from its starting
element, so the total work remains O(n) on average.

Space Complexity:
O(n)
The set stores up to n distinct elements.

# ----------------------------------
# Hash Set / Sequence Start Detection
# ----------------------------------

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_cons = 0
        numset = set(nums)

        for i in numset:
            if i - 1 not in numset:
                cons = 1

                while i + 1 in numset:   #even though, nested loops -> O(n) since while loop total operation is itself n, so n+n -> O(n) not n*n
                    cons += 1
                    i += 1

                max_cons = max(max_cons, cons)

        return max_cons
