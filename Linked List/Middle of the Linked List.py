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
