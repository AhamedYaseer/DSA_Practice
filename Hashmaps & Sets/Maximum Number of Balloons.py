Problem:
Maximum Number of Balloons (https://leetcode.com/problems/maximum-number-of-balloons/description/)

Approach:
Hash Map / Frequency Counting

Why this works:
The word "balloon" requires:
- 1 'b'
- 1 'a'
- 2 'l'
- 2 'o'
- 1 'n'

We count the occurrences of the required characters in text.

For 'l' and 'o', we divide their frequencies by 2 because each
"balloon" requires two occurrences of these characters.

The maximum number of complete "balloon" strings is determined by
the character with the smallest available count after accounting
for its required frequency.

Time Complexity:
O(n)
We traverse text once to count the required characters.

Space Complexity:
O(1)
Only the five characters required to form "balloon" are stored.

# ----------------------------------
# Hash Map / Frequency Counting
# ----------------------------------

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        Bln = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for i in text:
            if i in Bln:
                Bln[i] += 1

        output = min(
            Bln['b'],
            Bln['a'],
            Bln['l'] // 2,
            Bln['o'] // 2,
            Bln['n']
        )

        return output
