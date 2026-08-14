Problem:
Ransom Note (https://leetcode.com/problems/ransom-note/description/)

Approach:
Hash Map / Frequency Counting

Why this works:
We first count the characters present in ransomNote using a dictionary.

Then, while traversing magazine, we count only the characters that
are required by ransomNote.

Finally, for every character required by ransomNote, we check whether
the magazine contains enough occurrences of that character.

If a required character is missing or its count is insufficient, we
return False. Otherwise, we return True.

Time Complexity:
O(R + M)
We traverse ransomNote and magazine once, followed by a traversal of
the distinct characters in ransomNote.

Space Complexity:
O(K)
The dictionaries store the distinct characters encountered, where
K is the number of distinct characters.

# ----------------------------------
# Hash Map / Frequency Counting
# ----------------------------------

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_count = {}
        mag_count = {}

        for i in ransomNote:
            if i not in ran_count:
                ran_count[i] = 0
            else:
                ran_count[i] += 1

        for i in magazine:
            if i in ran_count:
                if i not in mag_count:
                    mag_count[i] = 0
                else:
                    mag_count[i] += 1

        for i in ran_count:
            if i not in mag_count or mag_count[i] < ran_count[i]:
                return False

        return True
