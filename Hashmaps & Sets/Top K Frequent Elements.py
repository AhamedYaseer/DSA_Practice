Problem:
Top K Frequent Elements (https://leetcode.com/problems/top-k-frequent-elements/description/)

Approach:
Hash Map / Frequency Counting + Sorting

Why this works:
We first use a hash map to count how many times each number appears
in the array.

For each number:
- If it is already present in `counter`, increase its frequency.
- Otherwise, initialize its frequency to 1.

After building the frequency map, we sort its items based on the
frequency in descending order.

The first `k` elements after sorting are the k most frequent numbers,
so we add their keys to the output list.

Time Complexity:
O(n log n)
Building the frequency map takes O(n), and sorting the distinct
elements takes O(n log n) in the worst case.

Space Complexity:
O(n)
The frequency map and output list can store up to O(n) elements.

# ----------------------------------
# Hash Map / Frequency Counting + Sorting
# ----------------------------------

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        output=[]

        counter={}

        for i in nums:

            counter[i]=counter.get(i,0)+1

        counter=sorted(counter.items(),key=lambda x:x[1],reverse=True)

        for i in range(k):

            output.append(counter[i][0])

        return output
