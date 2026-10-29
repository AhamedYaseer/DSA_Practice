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


Approach:
Floyd's Cycle Detection / Slow and Fast Pointers

Why this works:
We use two pointers starting from the head:

- `slow` moves one node at a time.
- `fast` moves two nodes at a time.

If there is no cycle, `fast` will eventually reach `None`.

If there is a cycle, both pointers will enter the cycle. Since `fast` moves one node faster than `slow` on every iteration, it will eventually catch up to `slow`.

When:

```python
fast == slow
```

both pointers refer to the exact same node, which confirms that a cycle exists.

The condition `fast and fast.next` ensures that `fast.next.next` is accessed only when both nodes exist.

Time Complexity:
O(n)
The list is traversed linearly. In a cyclic list, the two pointers eventually meet within the cycle.

Space Complexity:
O(1)
Only the `fast` and `slow` pointers are used.

# ----------------------------------
# Floyd's Cycle Detection / Slow and Fast Pointers
# ----------------------------------

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast = slow = head

        while fast and fast.next:

            fast=fast.next.next
            slow=slow.next

            if fast==slow:
                return True

        return False
