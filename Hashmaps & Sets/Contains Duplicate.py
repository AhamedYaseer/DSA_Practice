Problem:
Contains Duplicate (https://leetcode.com/problems/contains-duplicate/description/)

Approach:
Hash Map / Membership Tracking

Why this works:
We traverse the array and keep track of the elements that have
already been encountered using a dictionary.

For each element:
- If it is not present in the dictionary, we add it.
- If it is already present, a duplicate has been found, so we
  immediately return True.

If the entire array is traversed without finding a duplicate, we
return False.

Time Complexity:
O(n)
Each element is checked once, with average O(1) dictionary
membership checking.

Space Complexity:
O(n)
In the worst case, all elements are unique and are stored in the
dictionary.

# ----------------------------------
# Hash Map / Membership Tracking
# ----------------------------------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = {}

        for i in nums:
            if i not in visited:
                visited[i] = 0
            else:
                return True

        return False
