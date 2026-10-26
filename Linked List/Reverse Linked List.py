Problem:
Reverse Linked List (https://leetcode.com/problems/reverse-linked-list/)

Approach:
Linked List Traversal (In-Place Reversal)

Why this works:
We reverse the linked list by changing the direction of each node's `next` pointer.

We use three pointers:
- `current` → the node currently being processed.
- `prev` → the previous node, which becomes the new `next` of `current`.
- `nextnode` → temporarily stores the original next node so we don't lose the remaining list.

For each node:
1. Store the next node in `nextnode`.
2. Reverse the current node's pointer using `current.next=prev`.
3. Move `prev` to `current`.
4. Move `current` to `nextnode`.

When `current` becomes `None`, `prev` points to the new head of the reversed list.

Time Complexity:
O(n)
Each node is visited exactly once.

Space Complexity:
O(1)
Only three pointers are used, regardless of the size of the linked list.

# ----------------------------------
# In-place linked list reversal
# ----------------------------------

class Solution(object):
    def reverseList(self, head):

        current=head
        prev=None

        while current:

            nextnode=current.next
            current.next=prev
            prev=current
            current=nextnode

        return prev
