Problem:
Evaluate Reverse Polish Notation (https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)

Approach:
Stack / Reverse Polish Notation

Why this works:
In Reverse Polish Notation, operators come after their operands.
Therefore, we can use a stack to store numbers until an operator is
encountered.

For each token:
- Integer → Convert it to an integer and push it onto the stack.
- Operator → Pop the last two numbers from the stack.
- Apply the operator to those two numbers.
- Push the result back onto the stack.

We store the second popped value as `b` and the first popped value as
`a` because the order matters for subtraction and division.

For example:
`6 2 -` → `a = 6`, `b = 2` → `6 - 2`

For division, `int(a/b)` truncates the result toward zero, which is
the required behavior for this problem.

After processing all tokens, the stack contains only the final result.

Time Complexity:
O(n)
Each token is processed once.

Space Complexity:
O(n)
In the worst case, the stack can contain O(n) numbers.

# ----------------------------------
# Stack / Reverse Polish Notation
# ----------------------------------

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        output=[]

        for i in tokens:

            if i not in '+-*/':
                output.append(int(i))

            else:
                b=output.pop()
                a=output.pop()

                if i=='+':
                    output.append(a+b)

                elif i=='-':
                    output.append(a-b)

                elif i=='*':
                    output.append(a*b)

                else:
                    output.append(int(a/b))

        return output[-1]
