Problem:
Longest Common Prefix (https://leetcode.com/problems/longest-common-prefix/description/)

Approach:
Vertical Scanning (Prefix Comparison)

Why this works:
We first find the shortest string, because the common prefix
cannot be longer than it.

Then we compare characters at the same index across all strings.
If every string has the same character, we add it to the prefix.
As soon as a mismatch occurs, we return the prefix built so far.

Time Complexity:
O(n × m)
n = number of strings, m = length of the shortest string.

Space Complexity:
O(1) 

# ----------------------------------
# Vertical scanning solution
# ----------------------------------

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: 
            return ''

        index = 0
        shortest = strs[0]
        prefix = ''

        for word in strs:   #to find the shortest word
            if len(word) < len(shortest):
                shortest = word

        while index < len(shortest): #traverse through characters in shortest word and compare the character with other words
            for word in strs:
                if word[index] != shortest[index]:
                    return prefix
            prefix += shortest[index]
            index += 1

        return prefix

        
