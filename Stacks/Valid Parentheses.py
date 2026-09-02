Problem:
Valid Parentheses (https://leetcode.com/problems/valid-parentheses/description/)

Approach:
Stack / Matching Parentheses

Why this works:
A valid parentheses string must close brackets in the reverse order
of how they were opened. Therefore, we use a stack to keep track of
the opening brackets.

For each character:
- Opening bracket → Add it to the stack.
- Closing bracket → Check whether the most recent opening bracket
  matches it.
- If it matches, remove the opening bracket using pop().
- If it does not match, return False.

We also handle two invalid cases:
- A closing bracket appears when the stack is empty.
- Opening brackets remain in the stack after processing the string.

Finally, `return not output` returns True only when the stack is empty.

Time Complexity:
O(n)
Each character is processed once.

Space Complexity:
O(n)
In the worst case, all characters can be opening brackets and stored
in the stack.

# ----------------------------------
# Stack / Matching Parentheses
# ----------------------------------

class Solution:
    def isValid(self, s: str) -> bool:
        output=[]

        for i in s:

            if not output and i in ')}]':
                return False

            if i in '({[':
                output.append(i)

            elif i==')' and output[-1]=='(':
                output.pop()

            elif i==']' and output[-1]=='[':
                output.pop()

            elif i=='}' and output[-1]=='{':
                output.pop()

            else:
                return False

        return not output
