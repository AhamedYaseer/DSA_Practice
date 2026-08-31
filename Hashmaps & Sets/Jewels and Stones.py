Problem:
Jewels and Stones (https://leetcode.com/problems/jewels-and-stones/description/)

Approach:
Hash Map / Frequency Counting

Why this works:
We first count the frequency of every character in stones using a
dictionary.

Then, for each character in jewels, we check whether it exists in
the dictionary. If it exists, its frequency is added to the result.

This gives the total number of stones that are jewels.

Time Complexity:
O(S + J)
We traverse stones once to build the frequency dictionary and
jewels once to calculate the result.

Space Complexity:
O(k)
The dictionary stores the frequency of each distinct character
in stones, where k is the number of distinct characters.

# ----------------------------------
# Hash Map / Frequency Counting
# ----------------------------------

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        visited = {}
        output = 0

        for i in stones:
            if i not in visited:
                visited[i] = 1
            else:
                visited[i] += 1

        for i in jewels:
            if i in visited:
                output += visited[i]

        return output

Approach:
Hash Set / Membership Checking

Why this works:
We only need to know whether each stone is a jewel. We do not need
to store the frequency of each character.

We first convert jewels into a set, which allows average O(1)
membership checks.

Then we traverse stones once. If a stone exists in the set of jewels,
we increment the result.

Time Complexity:
O(J + S)
Creating the set takes O(J), and traversing stones takes O(S).
Set membership checking takes O(1) on average.

Space Complexity:
O(J)
The set stores the distinct characters from jewels.

# ----------------------------------
# Hash Set / Membership Checking
# ----------------------------------

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        set_jewels = set(jewels)                #changed to set to make membership operation at O(1) in line 79
        output = 0

        for i in stones:
            if i in set_jewels:
                output += 1

        return output
