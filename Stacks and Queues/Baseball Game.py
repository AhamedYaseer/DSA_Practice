Problem:
Baseball Game ([https://leetcode.com/problems/baseball-game/description/](https://leetcode.com/problems/baseball-game/description/))

Approach:
Stack Simulation

Why this works:
Each operation depends on the most recent scores, so we can use a
stack to keep track of the valid scores.

For each operation:

* Integer → Add the score to the stack.
* `C` → Remove the previous score using `pop()`.
* `D` → Add double the previous score.
* `+` → Add the sum of the previous two scores.

We use `output[-1]` to access the most recent score and
`output[-2]` to access the second most recent score.

After processing all operations, we sum all the scores in the stack
to get the final score.

Time Complexity:
O(n)
Each operation is processed once, and the final scores are traversed
once to calculate the total.

Space Complexity:
O(n)
The stack can store up to n scores.

# ----------------------------------
# Stack Simulation
# ----------------------------------

class Solution:

    def calPoints(self, operations: List[str]) -> int:

        output = []

        score = 0

        for i in operations:

            if i != 'C' and i != 'D' and i != '+':

                output.append(i)

            elif i == 'C':

                output.pop()

            elif i == 'D':

                output.append(2 * int(output[-1]))

            else:

                output.append(int(output[-1]) + int(output[-2]))

        for i in output:

            score += int(i)

        return score
```

# ----------------------------------
# Stack Simulation (cleaned version to avoid loop in the last)
# ----------------------------------


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output=[]
        score=0
        for i in operations:
            if i!='C' and i!='D' and i!='+':
                output.append(i)
                score+=int(i)
            elif i=='C':
                score-=int(output.pop())

            elif i=='D':
                output.append(2*int(output[-1]))
                score+=int(output[-1])
            else:
                output.append(int(output[-1])+int(output[-2]))
                score+=int(output[-1])
        return score
