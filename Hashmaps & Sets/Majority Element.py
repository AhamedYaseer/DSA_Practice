Problem:
Majority Element (https://leetcode.com/problems/majority-element/description/)

Approach:
Hash Map / Frequency Counting

Why this works:
We count the frequency of every element in nums using a hash map.

Then, we reverse the frequency dictionary so that the frequency
becomes the key and the corresponding element becomes the value.

Finally, we find the maximum frequency and return the element
associated with it.

The problem guarantees that a majority element exists, meaning
one element appears more than n/2 times. Therefore, the majority
element has a unique maximum frequency, so reversing the dictionary
does not affect the final result.

Time Complexity:
O(n)
We traverse the array to build the frequency dictionary, then
process the distinct frequencies a constant number of times.

Space Complexity:
O(n)
In the worst case, all elements are distinct and are stored in the
dictionaries.

# ----------------------------------
# Hash Map / Frequency Counting
# ----------------------------------

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counter = {}

        for i in nums:
            counter[i] = counter.get(i, 0) + 1

        rev_counter = {v: k for k, v in counter.items()}  #only one majority element, so no issues. Else, 2 element may have same frequency so the 2nd 
                                                          # one will be removed during reversing as key should be unique in dictionary

        max_val = 0

        for i in rev_counter:
            if i > max_val:
                max_val = i

        return rev_counter[max_val]
