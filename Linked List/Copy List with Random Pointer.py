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


Approach:
Interweaving Nodes (Three-Pass Linked List Traversal)

Why this works:
- First, create a copy of every original node and insert it immediately after the corresponding original node.
- The original and copied nodes are now interwoven: `A → A' → B → B'`.
- Second, assign the random pointers of copied nodes. Since every copied node is next to its original node, `current.random.next` gives the corresponding copied random node.
- Third, separate the interwoven list into two independent lists, restoring the original list and extracting the copied list.
- Return `copyhead`, which points to the newly created linked list.
- All copied nodes are new objects; no original nodes are reused.

Time Complexity:
O(n) — Three traversals of the linked list.

Space Complexity:
O(1) — No hash map or additional data structure is used. Only a constant number of pointers are maintained (excluding the newly created copied nodes).

---

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        current=head
        while current:
            CopyCurrent=Node(current.val) #creating new node with same value
            temp=current.next             #saving next node with temp
            current.next=CopyCurrent      #now copy node becomes next node
            CopyCurrent.next=temp         #next original becomes next of copy
            current=temp

        current=head
        while current:
            current.next.random=current.random.next if current.random else None
            current=current.next.next    

        current=head
        copyhead=head.next
        while current:  #to traverse only original
            copy=current.next #copy of that original
            nextoriginal=copy.next  #getting next original
            current.next=nextoriginal #now current points to next original
            if nextoriginal:
                copy.next=nextoriginal.next
            current=nextoriginal
        return copyhead
```
