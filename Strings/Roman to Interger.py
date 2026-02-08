Problem:
Roman to Integer (https://leetcode.com/problems/roman-to-integer/description/)

Approach:
Simulation with Conditional Subtraction

Why this works:
Traverse the string from left to right.  
If the current Roman value is smaller than the next value,
subtract the pair; otherwise, add the current value.

Time Complexity:
O(n)

Space Complexity:
O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:    #checking (it is not last value coz s[last+1] -> error) and (current Roman value is smaller than the next value)
                total += roman_map[s[i + 1]] - roman_map[s[i]]
                i += 2                                                      #since in subtraction case, we have processed 2 characters
            else:
                total += roman_map[s[i]]
                i += 1

        return total

