Problem:
Check if a String Is an Acronym of Words

Approach:
String Traversal

Why this works:
Iterates through the list of words, collects the first character of each word and store it in a string(t)
and compares the string(t) with the given acronym.

Time Complexity:
O(n)

Space Complexity:
O(n)

# -------------------
# String traversal
# -------------------

  class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        t=''
        for i in words:
            t=t+i[0]
        if t==s:
            return True
        else:
            return False

Problem:
Check if a String Is an Acronym of Words

Approach:
String Traversal (Optimized - without creating a new string)

Why this works:
Iterates through the list of words and compares the first character simultaneously
if mismatch, return False

Time Complexity:
O(n)

Space Complexity:
O(1)  [optimized]

# ---------------------------
# String traversal (optmized)
# ---------------------------

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        pointer=0
        if len(words)!=len(s):
            return False
        for i in words:
            if i[0]==s[pointer]:
                pointer=pointer+1
                continue
            else:
                return False
        return True


