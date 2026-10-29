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

Approach:
Two Pointers (One Pass) + Dummy Node

Why this works:
- Create a `dummy` node before `head` to handle the case where the head itself needs to be removed. [so incase of first element remval, dummy -> head.next] 
- Initialize `slow` and `fast` at the dummy node.
- Move `fast` `n+1` steps ahead to maintain a gap of `n` nodes between `slow` and `fast`.
- Move both pointers together until `fast` reaches `None`.
- At this point, `slow` is at the node just before the node that needs to be removed. [dummy in case of head removal]
- Skip the target node using `slow.next=slow.next.next`.
- Return `dummy.next` as the new head.

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
        dummy=ListNode(0)
        dummy.next=head
        slow=fast=dummy
        for i in range(n+1):    #to get n+1 gap
            fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next
```
