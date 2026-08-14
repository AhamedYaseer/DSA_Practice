Problem:
Valid Anagram (https://leetcode.com/problems/valid-anagram/description/)

Approach:
Hash Map / Frequency Counting

Why this works:
Two strings are anagrams if they contain the same characters with
the same frequencies.

We first count the frequency of each character in s using a dictionary.

Then, while traversing t, we decrease the corresponding character
count.

If a character is not present in the dictionary, t contains a
character that does not exist in s, so we return False.

Finally, if any character has a non-zero count, the two strings do
not contain the same number of occurrences, so we return False.
Otherwise, they are anagrams.

We also check the lengths first because two strings with different
lengths cannot be anagrams.

Time Complexity:
O(n)
We traverse the strings and the frequency dictionary a constant
number of times.

Space Complexity:
O(k)
The dictionary stores the frequency of each distinct character,
where k is the number of distinct characters.

# ----------------------------------
# Hash Map / Frequency Counting
# ----------------------------------

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        visited_s = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i not in visited_s:
                visited_s[i] = 1
            else:
                visited_s[i] += 1

        for i in t:
            if i not in visited_s:
                return False
            else:
                visited_s[i] -= 1

        for i in visited_s:
            if visited_s[i] != 0:
                return False

        return True
