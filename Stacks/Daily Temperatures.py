Problem:
Daily Temperatures (https://leetcode.com/problems/daily-temperatures/description/)

Approach:
Monotonic Stack / Next Greater Element

Why this works:
For each day, we need to find the next day with a higher
temperature.

We use a stack to store the indices of days whose warmer day has
not been found yet.

The stack maintains temperatures in decreasing order.

For each temperature at index `i`:
- While the current temperature is greater than the temperature at
  the index on top of the stack, we have found the warmer day for
  that previous index.
- Pop that index `j` from the stack.
- The number of days to wait is `i - j`, so we store it in
  `output[j]`.
- After resolving all possible previous days, add the current index
  to the stack.

Any indices remaining in the stack do not have a warmer day in the
future, so their values remain `0`.

The `else` belongs to the `while` loop. In Python, a `while-else`
block executes the `else` after the loop finishes normally, meaning
the current index is added to the stack after all possible warmer
days have been resolved.

Time Complexity:
O(n)
Each index is pushed onto the stack once and popped at most once.

Space Complexity:
O(n)
The stack can contain up to n indices, and the output array also
requires O(n) space.

# ----------------------------------
# Monotonic Stack / Next Greater Element
# ----------------------------------

class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        output=[0]*len(temperatures)

        stack=[0]

        for i in range(1,len(temperatures)):

            while stack and temperatures[i]>temperatures[stack[-1]]: #till there is an element in stack, check current number is greater than elements of stack

                j=stack.pop()

                output[j]=i-j #the next warmer day for particular day(j) is i. So, storing i-j on index j

            stack.append(i) #if no smaller value is found in stack, append it to stack

        return output
