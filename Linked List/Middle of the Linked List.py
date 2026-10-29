Problem:
Middle of the Linked List [https://leetcode.com/problems/middle-of-the-linked-list/]

Approach:
Two-Pass Linked List Traversal

Why this works:
- First, traverse the entire linked list and count the number of nodes.
- The middle index is `length // 2`.
- Reset `current` to `head`.
- Move `current` forward `length // 2` times to reach the middle node.
- For an even-length list, `length // 2` points to the second middle node.

Time Complexity: O(n)
Space Complexity: O(1)

----------------------------------

Two-Pass Linked List Traversal

----------------------------------


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        i=0
        current=head
        while current:
            i+=1
            current=current.next
        
        current=head
        for i in range((i//2)):
            current=current.next
        return current
```


Approach:
Slow and Fast Pointers

Why this works:
Use two pointers:
- `slow` moves one node at a time.
- `fast` moves two nodes at a time.
- When `fast` reaches the end, `slow` will be at the middle.
- For an even-length list, `slow` reaches the second middle node.
- `while fast and fast.next` ensures that `fast.next.next` can be accessed safely.

Time Complexity:
O(n)

Space Complexity:
O(1)

---

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
```
