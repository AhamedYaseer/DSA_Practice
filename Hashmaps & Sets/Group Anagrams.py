Problem:
Group Anagrams (https://leetcode.com/problems/group-anagrams/description/)

Approach:
Hash Map / Character Frequency Signature

Why this works:
Two strings are anagrams if they contain the same characters with
the same frequencies.

For each string, we count the frequency of every character and
convert the frequency dictionary into a sorted tuple of character-
frequency pairs.

The tuple acts as a hashable signature for the string.

Anagrams produce the same signature, so strings with the same
signature are grouped together using a dictionary. [eg: (((a,2),(b,2)) == (((a,2),(b,2))  ]

We store the indices of the strings for each signature and finally
use those indices to construct the grouped result.

Time Complexity:
O(N × K log K)
For each string, we count its characters in O(K) and sort the
distinct character-frequency pairs in O(K log K) in the worst case.

Space Complexity:
O(N × K)
The frequency signatures, grouping dictionary, and output require
space proportional to the total input size in the worst case.

# ----------------------------------
# Hash Map / Character Frequency Signature
# ----------------------------------

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        Count_strs = []

        for i in strs:
            Count_strs.append(self.Tuple_Counter(i))

        output_dict = {}

        for i in range(len(Count_strs)):
            if Count_strs[i] in output_dict:
                output_dict[Count_strs[i]].append(i)
            else:
                output_dict[Count_strs[i]] = [i]

        output_list = []

        for i in output_dict:
            output_list.append([strs[j] for j in output_dict[i]])

        return output_list

    def Tuple_Counter(self, string):
        Dict = {}

        for i in string:
            Dict[i] = Dict.get(i, 0) + 1

        return tuple(sorted(Dict.items()))


Approach:
Hash Map / Fixed-Size Frequency Signature

Why this works:
Two strings are anagrams if they contain the same characters with
the same frequencies.

For each string, we create a frequency dictionary containing all
26 lowercase English letters. The frequency values are then
converted into a tuple, which acts as a hashable signature.

Anagrams have identical frequency signatures, so strings with the
same signature are grouped together using a hash map.

Unlike the previous approach, we do not sort the character-frequency
pairs. Since the alphabet is fixed, the frequency tuple always has
the same order and can be used directly as the key.

Time Complexity:
O(N × K)
We traverse each string once to count its characters. Creating the
fixed-size 26-element tuple takes O(26), which is effectively O(1).

Space Complexity:
O(N × K)
The grouping dictionary and stored signatures require space
proportional to the input size. With a fixed 26-character alphabet,
the stored signature for each string is effectively O(1), making the
additional signature storage O(N).

# ----------------------------------
# Hash Map / Fixed-Size Frequency Signature
# ----------------------------------

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        Count_strs = []

        for i in strs:
            Count_strs.append(self.Tuple_Counter(i))

        output_dict = {}

        for i in range(len(Count_strs)):
            if Count_strs[i] in output_dict:
                output_dict[Count_strs[i]].append(i)
            else:
                output_dict[Count_strs[i]] = [i]

        output_list = []

        for i in output_dict:
            output_list.append([strs[j] for j in output_dict[i]])

        return output_list

    def Tuple_Counter(self, string):
        Dict = dict.fromkeys('abcdefghijklmnopqrstuvwxyz', 0)  #only change is here, here we r creating dictionary with all 26 characters..
                                                               #so if word is anagram, it will match even after conversion to tuple, no need to return sorted tuple

        for i in string:
            Dict[i] += 1

        return tuple(Dict.items())

