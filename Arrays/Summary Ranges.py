Problem:
Summary Ranges (https://leetcode.com/problems/summary-ranges/description/)

Approach:
Range Detection using Membership Checks

Why this works:
For each number in the sorted array, we check whether the previous
number (i-1) and next number (i+1) exist in the list.
If the previous number does not exist, the current number is the
start of a new range.
If the next number does not exist, the current number is the end of
the range, and we store the range in the output list. If start=end (single element case), then store element

Time Complexity:
O(n²)
Each membership check (x in nums) takes O(n) time and is used inside
a loop over all elements.

Space Complexity:
O(1)

# ----------------------------------
# Membership-check based solution 1
# ----------------------------------

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        start = nums[0] #random val
        end = nums[-1]  #random val
        output = []

        for i in nums:
            if i - 1 not in nums:
                start = i
            if i + 1 not in nums:
                end = i
                if start != end:
                    output.append(f"{start}->{end}")
                else:    #start==end (i.e., single element case)
                    output.append(str(start))

        return output

# ----------------------------------
# Membership-check based solution 2
# ----------------------------------


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output=[]
        temp=""
        for n in nums:
            if n+1 in nums:
                if n-1 not in nums:
                    temp=temp+str(n)+"->"
            else:
                temp+=str(n)
                output.append(temp)
                temp=""
        return output
