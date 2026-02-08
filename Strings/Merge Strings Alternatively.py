Problem:
Merge Strings Alternately

Approach:
String Concatenation (Simulation)

Why this works:
Iterates through both strings together using the length of the shorter
string as the loop range and appends characters alternately to a new string.
Remaining characters of the longer string are added at the end.

Time Complexity:
O((n + m)²)
Repeated string concatenation creates new strings and copies existing
characters each time, leading to quadratic total work.  [since strings are immutable]

Space Complexity:
O(n + m)

Note:
Because strings are immutable in Python, each concatenation copies the
current string. The total work follows the series
1 + 2 + 3 + ... + (n + m) = (n + m)(n + m + 1) / 2,
which simplifies to O((n + m)²).

# ----------------------------------
# String concatenation approach
# ----------------------------------

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        sol = ''

        for i in range(min(w1, w2)):
            # String is immutable → each concatenation creates a new string
            sol = sol + word1[i]
            sol = sol + word2[i]

        sol = sol + word1[w2:] if w1 > w2 else sol + word2[w1:]
        return sol


# ==================================
# Approach 2: Efficient List + Join
# ==================================

Approach:
Simulation with Efficient String Construction (List + Join)

Why this works:
Characters from both strings are appended alternately to a list.
Remaining characters of the longer string are extended at the end.
A single join operation converts the list into the final string in linear time.

Time Complexity:
O(n + m)

Space Complexity:
O(n + m)

# ----------------------------------
# Optimal list + join approach
# ----------------------------------

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        sol = []

        for i in range(min(w1, w2)):
            sol.append(word1[i])
            sol.append(word2[i])

        sol.extend(word1[w2:]) if w1 > w2 else sol.extend(word2[w1:])
        return "".join(sol)
