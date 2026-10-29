Problem:
Remove Nth Node From End of List [https://leetcode.com/problems/remove-nth-node-from-end-of-list/]

Approach:
Two-Pass Linked List Traversal

Why this works:
- First, traverse the linked list and count the total number of nodes.
- The node to remove is at position `i-n` from the beginning.
- If `i == n`, the node to remove is the head, so return `head.next`.
- Otherwise, move to the node just before the node that needs to be removed.
- Skip the target node using `current.next=current.next.next`.

Time Complexity:
O(n)

Space Complexity:
O(1)

---

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        i=0
        current=head
        while current:
            i+=1
            current=current.next

        if i==n:
            return head.next

        prev_remov=i-n
        current=head

        for i in range(1,prev_remov):
            current=current.next       
        current.next=current.next.next
        return head
```
