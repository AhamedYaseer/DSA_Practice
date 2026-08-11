
Problem:
Merge Intervals (https://leetcode.com/problems/merge-intervals/description/)

Approach:
Brute Force (Repeated Pairwise Merging)

Why this works:
We compare every pair of intervals to find overlapping intervals.

If two intervals overlap, we merge them by taking the smaller start
and the larger end. The merged interval is added to the list and 
The two original intervals are removed

After each merge, we restart the comparison because the newly merged
interval may overlap with another interval.

We repeat this process until no more intervals can be merged.

Time Complexity:
O(n³)
The merging function can take O(n²) time for pairwise comparisons,
and it may be called O(n) times as intervals are repeatedly merged.


Space Complexity:
O(n)
The list stores the intervals and newly created merged intervals.

# ----------------------------------
# Repeated Pairwise Merging
# ----------------------------------


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        PreFn = intervals
        PostFn = self.merging_arr(PreFn)

        while PostFn != PreFn:           #if PostFn == PreFn means, then merging is done so we can return output
            PreFn = PostFn
            PostFn = self.merging_arr(PreFn)   #restarting the comparison after the previous change

        return PostFn

    def merging_arr(self, array):
        first, second = 0, 0

        while first < len(array):
            while second < len(array):
                if first != second:
                    if (array[first][1] >= array[second][0] and array[second][1] >= array[first][0]): #checks like [8,10] & [1,2] -> 10>1 but not 1>8

                        AddElement = [
                            min(array[first][0], array[second][0]),          # min 1st element as first and max 2nd as second
                            max(array[first][1], array[second][1])
                        ]

                        array.append(AddElement)                            #adding the new elemnent and removing those 2 elements
                        array.pop(max(first, second))
                        array.pop(min(first, second))

                        first, second = 0, 0                               #Checking from first again
                        break

                second += 1

            first += 1
            second = 0

        return array
