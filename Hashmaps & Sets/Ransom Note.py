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
        ran_count={}
        mag_count={}
        for i in ransomNote:
            if i not in ran_count:
                ran_count[i]=1
            else:
                ran_count[i]+=1
        for i in magazine:
            if i in ran_count:
                if i not in mag_count:
                    mag_count[i]=1
                else:
                    mag_count[i]+=1
        for i in ran_count:
            if i not in mag_count or mag_count[i]<ran_count[i]:
                return False
        return True

Approach:
Hash Map / Required Character Counting

Why this works:
We first count the characters in ransomNote

Then, while traversing the magazine, whenever a character in ransomNote is found
we deduct it by 1

After completely traversing the magazine, if any character still has a positive
count in counter(ransomNote), we return False because in ransomNote that character
is appearing more than that of in magazine

Otherwise, the ransom note can be constructed and we return True.

This improves the brute-force version by using only one dictionary
instead of maintaining separate dictionaries for ransomNote and
magazine.

Time Complexity:
O(R + M)
We traverse ransomNote and magazine once. The final dictionary
traversal takes O(K), where K is the number of distinct characters,
so overall this remains O(R + M).

Space Complexity:
O(K)
The dictionary stores the required count for each distinct character.

# ----------------------------------
# Hash Map / Required Character Counting
# ----------------------------------

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_count = {}

        for i in ransomNote:
            if i not in ran_count:
                ran_count[i] = 1
            else:
                ran_count[i] += 1

        for i in magazine:
            if i in ran_count:
                ran_count[i] -= 1

        for i in ran_count:
            if ran_count[i] > 0:
                return False

        return True
