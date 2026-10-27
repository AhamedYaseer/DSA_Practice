Problem:
Merge Two Sorted Lists (https://leetcode.com/problems/merge-two-sorted-lists/)

Approach:
Linked List Traversal (Dummy Node + In-Place Merging)

Why this works:
Both linked lists are already sorted, so we can compare the current nodes of the two lists and always attach the smaller node to the merged list.

We use:
- `current1` → traverses `list1`.
- `current2` → traverses `list2`.
- `temp` → keeps track of the last node in the merged list.
- `dummy` → a helper node that makes it easier to build the merged list without handling the first node separately. #dummy(val) -> first val (head) -> second val -> none 

At each step, we compare `current1.val` and `current2.val`.

The smaller node is attached using `temp.next`, then:
- `temp` moves to the newly added node.
- The pointer of the list from which the node was taken moves to its next node.

When either list becomes empty, the remaining nodes of the other list are already sorted, so they can be directly attached to the merged list.

Finally, `dummy.next` is returned because `dummy` itself is only a helper node. #which is the head of the merged list

Time Complexity:
O(n + m)
Each node from both linked lists is visited once.

Space Complexity:
O(1)
No new linked-list nodes are created apart from the constant-size dummy node. The existing nodes are reused and rearranged in-place.

# ----------------------------------
# Dummy Node / In-place merging
# ----------------------------------

class Solution(object):
    def mergeTwoLists(self, list1, list2):

        dummy = temp = ListNode(0)

        current1,current2=list1,list2

        while current1 and current2:

            if current1.val<current2.val:
                temp.next=current1
                temp=temp.next
                current1=current1.next

            else:
                temp.next=current2
                temp=temp.next
                current2=current2.next

        while current1:
            temp.next=current1
            temp=temp.next
            current1=current1
