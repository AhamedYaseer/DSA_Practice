Problem:
Min Stack (https://leetcode.com/problems/min-stack/description/)

Approach:
Two Stacks / Minimum Tracking

Why this works:
We use two stacks:
- `stack` → stores all the values.
- `mini` → stores the minimum values encountered so far.

When pushing a value:
- Add it to `stack`.
- If `mini` is empty or the new value is less than or equal to
  the current minimum, add it to `mini`.

The `<=` condition is important because duplicate minimum values
must also be stored. This ensures that when one minimum is popped,
another identical minimum can still remain.

When popping:
- Remove the top value from `stack`.
- If the removed value is the current minimum, also remove it from
  `mini`.

Therefore, the top of `mini` always represents the current minimum,
allowing `getMin()` to return the minimum in O(1) time.

Time Complexity:
O(1)
`push`, `pop`, `top`, and `getMin` all take constant time.

Space Complexity:
O(n)
The two stacks can store up to n elements in the worst case.

# ----------------------------------
# Two Stacks / Minimum Tracking
# ----------------------------------

class MinStack:
    def __init__(self):
        self.stack=[]
        self.mini=[]

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.mini or value<=self.mini[-1]:
            self.mini.append(value)

    def pop(self) -> None:
        if self.mini and self.stack.pop()==self.mini[-1]:
            self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1] if self.mini else []
