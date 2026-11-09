Problem:
Copy List with Random Pointer [https://leetcode.com/problems/copy-list-with-random-pointer/]

Approach:
Hash Map (Two-Pass Linked List Traversal)

Why this works:
- First, create a new node for every original node with the same value.
- Store the mapping between each original node and its corresponding copied node in a dictionary (`OldToNew`).
- Initialize the dictionary with `{None: None}` to handle `next` or `random` pointers that are `None`.
- In the second traversal, use the dictionary to connect the copied nodes' `next` and `random` pointers.
- Return `OldToNew[head]`, which gives the head of the newly copied linked list.
- All copied nodes are new objects, so no original nodes are reused.

Time Complexity:
O(n)

Space Complexity:
O(n)

--- 

```python
# Definition for a Node.

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        OldToNew={None:None}  #to handle Old (None) = new (None)
        current=head
        while current:
            CopyNode=Node(current.val) #creating new node with same current value
            OldToNew[current]=CopyNode
            current=current.next
        
        current=head

        while current:
            OldToNew[current].next=OldToNew[current.next]   #newcurrent -> newnext
            OldToNew[current].random=OldToNew[current.random]
            current=current.next
        return OldToNew[head]
