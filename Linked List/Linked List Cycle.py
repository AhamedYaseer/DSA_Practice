Problem:
Linked List Cycle (https://leetcode.com/problems/linked-list-cycle/)

Approach:
Hash Set / Visited Nodes

Why this works:
A cycle exists if we encounter the exact same node again while traversing the linked list.

We use a `set` called `visited` to store the nodes that have already been visited.

For each node:
- If the node is already in `visited`, we have returned to the same node, so a cycle exists.
- Otherwise, we add the node to `visited` and move to the next node.

If `current` becomes `None`, the list ends normally and there is no cycle.

We compare the **node itself**, not its value, because different nodes can have the same value.

Time Complexity:
O(n)
Each node is visited at most once before either finding a repeated node or reaching the end.

Space Complexity:
O(n)
In the worst case, the set stores all nodes in the linked list.

# ----------------------------------
# Hash Set / Visited Nodes
# ----------------------------------

class Solution(object):
    def hasCycle(self, head):

        current=head
        visited=set()

        while current:

            if current in visited:
                return True

            visited.add(current)
            current=current.next

        return False
